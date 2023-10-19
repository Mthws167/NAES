import decimal
from django import template
from django.utils.formats import localize

register = template.Library()


@register.filter(name='desconto3')
def desconto3(valor):
    if (valor > 60000.00):
        return round(valor * decimal.Decimal((3/100)), 2)

    return valor

@register.simple_tag(name="custofrete")
def custofrete(valor,custo,dia):
    if (valor > 0.00):
        return round((valor + decimal.Decimal((custo * dia))), 2)

    return valor
