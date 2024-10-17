from rest_framework.serializers import ModelSerializer

from shops.models import Address, Country


class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


from rest_framework import serializers
from .models import Address

class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'first_name', 'last_name','address_line_1', 'address_line_2','', 'city',
                  'state', 'postal_code', 'phone_number', 'shipping_address',
                  'billing_address', 'country', 'user']
        read_only_fields = ['is_default_billing', 'is_default_shipping']
