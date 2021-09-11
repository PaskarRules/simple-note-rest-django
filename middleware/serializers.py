from rest_framework import serializers

from .models import IpAddress


class IpAddressesSerializer(serializers.ModelSerializer):

    class Meta:
        model = IpAddress
        fields = '__all__'
        extra_kwargs = {'ip_address': {'read_only': True}}
