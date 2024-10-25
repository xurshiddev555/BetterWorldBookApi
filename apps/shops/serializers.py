from rest_framework.serializers import ModelSerializer
from shops.models import Book
from rest_framework import serializers
from users.models import Address
from users.models import Address, Country
from users.serializers import AuthorModelSerializer


class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'first_name', 'last_name', 'address_line_1', 'address_line_2', 'city',
                  'state', 'postal_code', 'phone_number', 'address_line_1',
                  'address_line_2', 'country', 'user']
        # read_only_fields = ['is_default_billing', 'is_default_shipping']


class BookDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        exclude = ()


class BookListModelSerializer(ModelSerializer):
    author = AuthorModelSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'slug', 'author', 'image')
