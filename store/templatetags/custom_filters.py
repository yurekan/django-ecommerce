from django import template
import decimal

register = template.Library()

@register.filter(name='get_by_index')
def get_by_index(value, index):
    try:
        return value[int(index)]  # Convert the index to an integer
    except (IndexError, ValueError):
        return None  # Return None if index is out of range or invalid

@register.filter
def range_filter(value):
    """Generates a range from 0 to value."""
    # Ensure the value is an integer before passing to range
    if isinstance(value, decimal.Decimal):
        value = int(value)  # Convert Decimal to int
    return range(value)