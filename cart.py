from django import template

register = template.Library()
@register.filter(name='cart_count')
def cart_count(carts,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == carts.id:
            quantity=cart.get(id)
          
            
            return quantity
            
    return ('')
@register.filter(name='is_in_cart')
def is_in_cart(p,cart):
    keys=cart.keys()
    for id in keys:
        if (id) == p.id:
            return True
        else:
            return False    
           
@register.filter(name='price')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
        else:
           pass    
        
@register.filter(name='total')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
             total=cart.get(id)*product.price
             return total

    
  
