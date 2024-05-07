from django.conf import settings
from shop.models import Product


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

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {
                'quantity': 0,
                'price': product.price
            }
        self.basket[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        return sum(item['quantity'] * item['price'] for item in self.basket.values())
