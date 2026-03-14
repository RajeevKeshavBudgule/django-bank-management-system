from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('accounts/',views.account_list,name='account_list'),
    path('add/',views.add_account,name='add_account'),
    path('update/<int:id>/',views.update_account,name='update_account'),
    path('delete/<int:id>/',views.delete_account,name='delete_account'),

]