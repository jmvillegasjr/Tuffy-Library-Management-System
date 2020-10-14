import django_filters
from django_filters import DateFilter
from .models import *


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['date_received']


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = '__all__'


class IssueOrderFilter(django_filters.FilterSet):
    class Meta:
        model = IssueOrder
        fields = '__all__'


class ReturnOrderFilter(django_filters.FilterSet):
    class Meta:
        model = ReturnOrder
        fields = '__all__'