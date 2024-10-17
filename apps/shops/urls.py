
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shops.views import AddressListCreateAPIView, CountryListAPIView, AddressListCreateView, \
    AddressUpdateDeleteView

router = DefaultRouter()
# router.register(r'wishlists', WishListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('address', AddressListCreateAPIView.as_view()),
    path('country', CountryListAPIView.as_view()),
    path('addresses/', AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:id>/', AddressUpdateDeleteView.as_view(), name='address-update-delete'),

]
