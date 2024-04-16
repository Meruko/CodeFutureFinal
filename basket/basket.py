from django.conf import settings
from magazine.models import Product

# {
#     'basket': {
#         '5': {
#             'quantity': 10,
#             'price': 320
#         },
#         '2': {
#             'quantity': 3,
#             'price': 300
#         }
#     }
# }

# COPY
# {
#     'basket': {
#         '5': {
#             'quantity': 10,
#             'price': 320,
#             'product': Product,
#             'total_price': 3200
#         },
#         '2': {
#             'quantity': 3,
#             'price': 300,
#             'product': Product,
#             'total_price': 900
#         }
#     }
# }

class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        product_ids = self.basket.keys()
        product_list = Product.objects.filter(pk__in=product_ids)
        basket = self.basket.copy()

        for product in product_list:
            basket[str(product.id)]['product'] = product
        for item in basket.values():
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    def save(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def add(self, product: Product, quantity: int = 1, update_quantity: bool = False):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {
                'quantity': 0,
                'price': product.price
            }
        if update_quantity:
            self.basket[product_id]['quantity'] = quantity
        else:
            self.basket[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product: Product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        return sum(item['quantity'] * item['price'] for item in self.basket.values())