from django import template

register = template.Library()

@register.inclusion_tag('accounts/_inc/_form.html')
def account_form(title: str, form, url_name: str):
    return {
        'title': title,
        'form': form,
        'url_name': url_name
    }
