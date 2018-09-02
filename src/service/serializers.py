from .models import *
from rest_framework import serializers

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'

    def create(self, validated_data):
        data = validated_data
        register = Receipt.objects.create(**data)

        return register