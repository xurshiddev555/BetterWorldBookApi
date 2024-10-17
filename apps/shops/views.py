from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from shops.models import Address, Country
from shops.serializers import AddressModelSerializer, CountryModelSerializer


@extend_schema(tags=['users'])
class AddressListCreateAPIView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressModelSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@extend_schema(tags=['users'])
class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
    authentication_classes = ()


from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Address
from .serializers import AddressModelSerializer

class AddressListCreateView(generics.ListCreateAPIView):
    serializer_class = AddressModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user).order_by('-is_default_shipping', '-is_default_billing', 'name')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddressUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        address = self.get_object()

        if address.is_default_billing or address.is_default_shipping:
            return Response({'error': 'Cannot delete a default address'}, status=status.HTTP_400_BAD_REQUEST)

        return super().delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        address = self.get_object()

        if address.is_default_billing:
            return Response({'error': 'Cannot edit the default billing address'}, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)


