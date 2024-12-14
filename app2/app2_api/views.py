from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .models import BankAccount, Transaction
from rest_framework import status
from .serializer import BankAccountSerializer, UserSerializer, TransactionSerializer



def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True),

    return JsonResponse(serializer.data,status=status.HTTP_302_FOUND)

def get_bank_accounts(request):
    accounts = BankAccount.objects.all()
    serializer = BankAccountSerializer(accounts,many=True)
    return JsonResponse(serializer.data, safe=False ,status=status.HTTP_200_OK)


@api_view(['POST'])
def create_transaction(request):
    # Use the TransactionSerializer to validate and serialize the data
    serializer = TransactionSerializer(data=request.data)

    if serializer.is_valid():
        try:
            # Retrieve the account object using the account number
            account = BankAccount.objects.get(account_number=serializer.validated_data['account_number'])
            
            # Retrieve the sender and receiver users using the username
            sender = User.objects.get(username=serializer.validated_data['sender_username'])
            receiver = User.objects.get(username=serializer.validated_data['receiver_username'])

            # Create the transaction using the validated data
            transaction = Transaction.objects.create(
                account=account,
                amount=serializer.validated_data['amount'],
                transaction_type=serializer.validated_data['transaction_type'],
                sender=sender,
                receiver=receiver
            )

            # Return a success response with the transaction ID
            return JsonResponse({
                "message": "Transaction created successfully", 
                "transaction_id": transaction.id
            }, status=status.HTTP_201_CREATED)

        except BankAccount.DoesNotExist:
            return JsonResponse({"error": "Bank account not found"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # If the data is invalid, return the validation errors
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)