from django_filters.rest_framework import FilterSet
from .models import Sport

class SportFilter(FilterSet):
    class Meta:
        model = Sport
        fields = {
            'price': ['lt' , 'gt']
        }