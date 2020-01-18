from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from .models import Bidder
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    #Return the index html file
    return render(request, 'home.html')



@login_required
def logout(request):
    #Log the user out
    auth.logout(request)
    messages.success(request, "You have successfuly been logged out")
    return redirect(reverse('home'))
  
  
    

def login(request):
    # Return a login page
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
                                     
            
            if user:
                auth.login(user=user, request=request)
                
                messages.success(request, "You have successfuly logged in!")
                return redirect(reverse('home'))
                
            else:
                login_form.add_error(None, "Your username of password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
    



def registration(request):
    # Returns a registration page that allows user/bidder information saved 
    # The bidders info stored here can be viewed in bidders profile
    
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            bidding_user = registration_form.save()
            bidding_user.refresh_from_db() 
            bidding_user.bidder.phone = registration_form.cleaned_data.get('phone')
            bidding_user.bidder.street_address1 = registration_form.cleaned_data.get('street_address1')
            bidding_user.bidder.street_address2 = registration_form.cleaned_data.get('street_address2')
            bidding_user.bidder.county = registration_form.cleaned_data.get('county')
            bidding_user.bidder.eircode = registration_form.cleaned_data.get('eircode')
            bidding_user.bidder.country = registration_form.cleaned_data.get('country')
            bidding_user.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
                                     
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to register your account at this time")
            
    else:
        registration_form = UserRegistrationForm()
    
    return render(request, 'registration.html', { 
        "registration_form": registration_form})
    
    
    
def user_profile(request):
    # The bidders profile page that shows all sign up info
    user = get_object_or_404(Bidder, user__email=request.user.email)
    return render(request, 'profile.html', {"profile": user})