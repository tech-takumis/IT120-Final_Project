from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        account_number = serializers.CharField(max_length=100)
        amount = serializers.DecimalField(max_digits=10, decimal_places=2)
        transaction_type = serializers.CharField(max_length=100)
        sender_username = serializers.CharField(max_length=150)
        receiver_username = serializers.CharField(max_length=150)