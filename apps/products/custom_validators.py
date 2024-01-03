from django.core.exceptions import ValidationError


def validate_non_negative_price(price):
    if price < 0:
        raise ValidationError('price must be greater than or equal to 0.00')

def validate_discount(discount):
    if discount > 100:
        raise ValidationError('Discount cannot be more than 100%')
