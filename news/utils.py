from django.core.paginator import Paginator, Page
from django.http import HttpRequest
from typing import Any

def paginate(request: HttpRequest, items: list, per_page: int = 1, is_elided: bool = False) -> Page:
    paginator = Paginator(items, per_page)
    page_num = int(request.GET.get(key='page', default=1))
    page_obj = paginator.get_page(page_num)

    if is_elided:
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_num)
    return page_obj

class PaginatePage:
    def paginate_elided(self, context: dict[str, Any]):
        if context.get('is_paginated'):
            page_obj = context.get('page_obj')
            page_obj.adjusted_elided_pages = page_obj.paginator.get_elided_page_range(page_obj.number)

class CalculateMoney:
    def sum_price_count(self, price: [int, float], count: int, discount: int = None, nds: int = None):
        result = round(price*count, 2)
        if discount:
            result = round(result * (1 - (discount/100)), 2)
        if nds:
            result = round(result * (1 - (nds/100)), 2)
        return result

    def sum_price(self, prices: list, discount: int = None, nds: int = None):
        result = round(sum(prices), 2)
        if discount:
            result = round(result * (1 - (discount/100)), 2)
        if nds:
            result = round(result * (1 - (nds/100)), 2)
        return result

def sum_price_count(price: [int, float], count: int, discount: int = None, nds: int = None):
    return CalculateMoney().sum_price_count(price=price, count=count, discount=discount, nds=nds)