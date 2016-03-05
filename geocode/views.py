from geocode.models import ZipGeocode
from rest_framework import viewsets
from responders.permissions import IsAccountAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination
from serializers import ZipCodeSerializer


class SmallResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ZipGeocodeViewset(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ZipGeocode.objects.all()
    serializer_class = ZipCodeSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
    pagination_class = SmallResultsSetPagination
