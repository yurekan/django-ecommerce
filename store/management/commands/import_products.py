import ast
import pandas as pd
from django.core.management.base import BaseCommand
from store.models import Product 

def safe_literal_eval(value):
    if value is None:
        return None
    else:
        ast.literal_eval(value)

class Command(BaseCommand):
    help = 'Update products with data from a CSV file using pandas'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            # Try to find an existing Product instance by name
            product, created = Product.objects.get_or_create(name=row['name'])
            
            price_list = ast.literal_eval(row.get('price', None))
            price = [float(price_string.replace('Rs.', '').replace(',', '')) for price_string in price_list]
            product.price = price
            product.highlights = row.get('highlights', None)
            product.digital = row.get('digital', False)
            product.images = ast.literal_eval(row.get('images', None))
            product.rating = float(row.get('rating', None))
            product.review_count = row.get('review_count', None)
            product.model = ast.literal_eval(row.get('model', None))
            product.combo = safe_literal_eval(row.get('combo', None))
            product.description = ast.literal_eval(row.get('description', None))
            product.features = safe_literal_eval(row.get('features', None))
            product.sub_category = ast.literal_eval(row.get('sub_category', None))
            product.category = row.get('category', None)
            product.specifications = safe_literal_eval(row.get('specifications', None))
            # print(row.get('size', None))
            # print(safe_literal_eval(row.get('size', None)))
            product.size = ast.literal_eval(row.get('size', None))

            # Save the updated product
            product.save()

        self.stdout.write(self.style.SUCCESS('Products updated successfully!'))