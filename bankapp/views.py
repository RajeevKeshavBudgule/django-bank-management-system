from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Account
from .forms import AccountForm


def home(request):
    return render(request,'bankapp/home.html')


def account_list(request):
    accounts = Account.objects.all()
    return render(request,'bankapp/account_list.html',{'accounts':accounts})


def add_account(request):
    form = AccountForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('account_list')

    return render(request,'bankapp/add_account.html',{'form':form})


def update_account(request,id):
    account = Account.objects.get(id=id)
    form = AccountForm(request.POST or None,instance=account)

    if form.is_valid():
        form.save()
        return redirect('account_list')

    return render(request,'bankapp/update_account.html',{'form':form})


def delete_account(request,id):
    account = Account.objects.get(id=id)
    account.delete()
    return redirect('account_list')
