from django_filters import rest_framework as filters
from .models import Tour


class TourFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')  # Минимальная цена
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')  # Максимальная цена
    min_rating = filters.NumberFilter(field_name="average_rating", lookup_expr='gte')  # Минимальный рейтинг
    max_rating = filters.NumberFilter(field_name="average_rating", lookup_expr='lte')  # Максимальный рейтинг
    season = filters.CharFilter(field_name="datetour__season")  # Фильтрация по сезону

    class Meta:
        model = Tour
        fields = ['min_price', 'max_price', 'min_rating', 'max_rating', 'season']  # Параметры для фильтрации
