from typing import Any

def paginate_elided(context: dict[str, Any]):
    if context.get('is_paginated'):
        page_obj = context.get('page_obj')
        page_obj.adjusted_elided_pages = page_obj.paginator.get_elided_page_range(page_obj.number)
