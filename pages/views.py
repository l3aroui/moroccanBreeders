from django.contrib.auth import authenticate, login as auth_login,logout
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
import re
from django.contrib.auth.decorators import login_required
from .models import Breeders, Delivery
from datetime import datetime
from products.models import Cart,Product
from products.models import Product,Cart


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            
            if remember_me:
                request.session.set_expiry(None)
                 
            return redirect('index')  
        else:            
            error_message = "Invalid email or password"
            return render(request, 'pages/login.html', {'error_message': error_message})
    
    return render(request, 'pages/login.html')







def user_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        user_name = request.POST.get('user_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        
        # Create the user object
        user = User.objects.create_user(
            username=user_name,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        # Create the profile object and associate it with the user
        profile = Profile.objects.create(user=user, phone_number=phone_number)
        
        # Create a new cart for the user
        cart = Cart.objects.create(user=user)
        
        # Associate products with the cart
        product = get_object_or_404(Product, id=1)  # Replace '1' with the desired product ID
        cart.products.add(product)
        
        # Redirect to the login page
        return redirect('login')
    
    return render(request, 'pages/register.html')




def user_logout(request):
    logout(request)
    return redirect('index')



def breeders_dashboard(request):
    if request.user.is_authenticated:
        try:
            breeder = Breeders.objects.get(user=request.user)
            search_date = request.GET.get('search_date')
            deliveries = Delivery.objects.filter(breeders=breeder)
            if search_date:
                # Convertir la date de recherche en objet datetime
                search_date = datetime.strptime(search_date, '%Y-%m-%d').date()
                # Filtrer les livraisons par date
                deliveries = deliveries.filter(date_time__date=search_date)
                context = {'deliveries': deliveries, 'breeder': breeder}
                return render(request, 'pages/breeders_dashboard.html', context)
            else:
                context = {'breeder': breeder}
                return render(request, 'pages/breeders_dashboard.html', context)
        except Breeders.DoesNotExist:
            pass
    return render(request, 'pages/breeders_dashboard.html') 
    


def user_profile(request):
    user = request.user  # Get the current authenticated user
    
    context = {
        'user': user  # Pass the user object to the template
    }
    return render(request,'pages/profile.html', context)
