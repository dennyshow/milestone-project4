from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.

def user_balance(request):
    
    # allows user to view thier balance
    
    try:
        if request.session['username']:
            user = User.objects.filter(username=request.session['username'])
            return render(request, 'balance.html', {'user': user[0]})
    except KeyError:
        return render(request('home'))
    
    return render(request, 'home.html')
    

def user_topup(request):
    # allows user to topup thier balance
    
    if request.method == "POST":
        form = TopUpForm(request.POST)
        if form.is_valid():
            try:
                if request.session['username']:
                    user = User.objects.get(username=request.session['username'])
                    userProfile = UserProfile.objects.get(user_id=user.id)
                    userProfile.balance += form.cleaned_data['amount']
                    userProfile.save()
            except KeyError:
                return render(redirect('home'))
                
        