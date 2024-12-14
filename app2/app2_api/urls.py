from django.urls import path
from .views import get_users,get_bank_accounts, create_transaction

urlpatterns = [
    path('users/',get_users,name='get_users'),
    path('bank/accounts/',get_bank_accounts,name='get_bank_accounts'),
     path('bank/transaction/', create_transaction, name='create_transaction'),
]