from django import template

register = template.Library()

@register.inclusion_tag('chat/_inc/chat_message.html')
def show_message(message):
    return {'message': message}