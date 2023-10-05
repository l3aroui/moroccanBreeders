from django.shortcuts import render, get_object_or_404,redirect
from .models import Product, ItemPanier
from .models import Cart,Orders_Confirm




# Create your views here.
def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity:
            user = request.user  # Utilisateur associé (à ajuster selon votre modèle d'authentification)

            cart, created = Cart.objects.get_or_create(user=user)
            item_panier = ItemPanier(cart=cart, product=product, quantity=quantity)
            item_panier.save()

            # Afficher un message de confirmation ou rediriger l'utilisateur vers une autre page
            return redirect('cart')

    return render(request, 'products/product.html', context)


def products(request):
    products = Product.objects.all()  
    context = {'prod': products}
    return render(request, 'products/products.html', context)



def cart(request):
    cart = get_object_or_404(Cart, user=request.user)

    if request.method == 'POST' and 'confirm' in request.POST:
        if cart.itempanier_set.exists():
            orders_confirm = Orders_Confirm.objects.create(cart=cart)
            orders_confirm.save()
            cart.itempanier_set.all().delete()
        else:
            # Handle the case when the cart is empty
            return redirect('cart')  # Replace 'empty_cart' with the appropriate URL or view name

    context = {'cart': cart}
    return render(request, 'products/cart.html', context)

def update_item(request, item_id):
    item = get_object_or_404(ItemPanier, id=item_id)
    
    if 'quantity' in request.POST:
        quantity = int(request.POST['quantity'])
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
    
    # Redirect the user back to the cart page or another appropriate page
    return redirect('cart')
       
    
    # Redirect the user back to the cart page or another appropriate page
    return redirect('cart')  # Redirect back to the cart page

def delete_item(request, item_id):
    item = get_object_or_404(ItemPanier, id=item_id)
    
    item.delete()
    return redirect('cart')  # Redirect back to the cart page