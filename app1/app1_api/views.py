from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import TransactionSerializer
from rest_framework import status
from rest_framework.response import Response

def welcome(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def fetch_bank_accounts(request):
    response = requests.get("http://localhost:8001/api/bank/accounts")
    
    if response.status_code == 200:  
        data = response.json()  
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data from the API'}, status=response.status_code)

@api_view(['POST'])
def send_transaction(request):
    # Validate incoming data using the TransactionSerializer
    serializer = TransactionSerializer(data=request.data)

    if serializer.is_valid():
        try:
            # Send a POST request to project2's API to save the transaction
            response = requests.post("http://localhost:8001/api/bank/transactions", data=request.data)

            if response.status_code == 201:
                return JsonResponse({"message": "Transaction sent successfully"}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({"error": "Transaction failed to send"}, status=response.status_code)
        except Exception as e:
            # Handle any errors that occur during the request
            print(f"Error during save: {e}")
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # If serializer is not valid, return validation errors
        return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

