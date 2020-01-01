from django.shortcuts import render, reverse, redirect
from django.utils import timezone

# Create your views here.

def view_basket(request):
    # View that renders the basket contents
    return render(request, "basket.html")
     

def add_to_basket(request, id):
    # Add a specified product
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    basket[id] = basket.get(id, quantity)
    
    request.session['basket'] = basket
    return redirect(reverse('home'))
    
    
def update_basket(request, id):
    # Update the quantity of a specific product
    
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    
    if quantity > 0:
        basket[id] = quantity
    else:
        basket.pop(id)
        
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
    
    