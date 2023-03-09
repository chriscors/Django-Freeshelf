from django import template

register = template.Library()


@register.filter
def add_class(field, cl):
    """
    Adds class to fields in Redux templates
    """
    return field.as_widget(attrs={"class": cl})
