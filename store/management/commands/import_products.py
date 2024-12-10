import ast
from django.core.management.base import BaseCommand
from store.models import Product
import pandas as pd

class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        data = pd.read_csv(csv_file)
        for i in range(len(data)):
            name = data.iloc[i]['name']
            price_list = ast.literal_eval(data.iloc[i]['price'])
            price_string = price_list[0]
            price = float(price_string.replace('Rs.', '').replace(',', ''))
            highlights = data.iloc[i]['highlights']
            description = data.iloc[i]['description'].split(':')[0].strip()

            Product.objects.create(
                name=name,
                price=price,
                highlights=highlights,
                description=description
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported products'))
