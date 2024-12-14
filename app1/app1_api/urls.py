from django.urls import path
from .views import welcome,login, register, fetch_bank_accounts,send_transaction


urlpatterns = [
    path('welcome/',welcome,name='welcome_page'),
    path('register/',register,name='welcome_page'),
    path('login/',login,name='welcome_page'),
    path('bank/accounts/',fetch_bank_accounts, name="fetch_bank_accounts"),
    path('bank/transaction/',send_transaction, name="send_transaction" ),
]