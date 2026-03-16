
# Create your views here.
from django.shortcuts import render,redirect
from .models import Account
from .forms import AccountForm

# this is the home function 
def home(request):
    return render(request,'bankapp/home.html')

# this is the account list function
def account_list(request):
    accounts = Account.objects.all()
    return render(request,'bankapp/account_list.html',{'accounts':accounts})

# this is the add account detail
def add_account(request):
    form = AccountForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('account_list')

    return render(request,'bankapp/add_account.html',{'form':form})

# this is the update account 
def update_account(request,id):
    account = Account.objects.get(id=id)
    form = AccountForm(request.POST or None,instance=account)

    if form.is_valid():
        form.save()
        return redirect('account_list')

    return render(request,'bankapp/update_account.html',{'form':form})

# this is the delete account 
def delete_account(request,id):
    account = Account.objects.get(id=id)
    account.delete()
    return redirect('account_list')
