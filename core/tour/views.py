from rest_framework import generics, filters
from django.db.models import Avg, Prefetch
from django_filters.rest_framework import DjangoFilterBackend  # [1] Добавлен импорт для DjangoFilterBackend
from .models import Banner, Tour, Feedback, Rating, RegionTour, DateTour
from .serializers import BannerSerializer, TourSerializer, FeedbackSerializer, RegionTourSerializer
from .filters import TourFilter  # [2] Добавлен импорт для фильтрации Tour


# Получение списка баннеров и создание нового баннера
class BannerIndexView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


# Получение, обновление и удаление конкретного баннера
class BannerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class TourSearchView(generics.ListAPIView):
    serializer_class = TourSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]  # [3] Добавлен DjangoFilterBackend для фильтрации
    search_fields = ['title', 'description', 'route_tour']
    filterset_class = TourFilter  # [4] Подключен класс фильтра TourFilter

    def get_queryset(self):
        queryset = Tour.objects.prefetch_related(
            Prefetch('ratings', queryset=Rating.objects.all())
        ).annotate(average_rating=Avg('ratings__score'))
        return queryset


class TourListView(generics.ListAPIView):
    serializer_class = TourSerializer
    filter_backends = [DjangoFilterBackend]  # [5] Добавлен DjangoFilterBackend для фильтрации
    filterset_class = TourFilter  # [6] Подключен фильтр для списка туров

    def get_queryset(self):
        queryset = Tour.objects.prefetch_related(
            Prefetch('ratings', queryset=Rating.objects.all())
        ).annotate(average_rating=Avg('ratings__score')).order_by('-average_rating')[:4]
        return queryset


class TourSeasonView(generics.ListAPIView):
    serializer_class = TourSerializer
    filter_backends = [DjangoFilterBackend]  # [7] Добавлен DjangoFilterBackend для фильтрации
    filterset_class = TourFilter  # [8] Подключен фильтр для фильтрации по сезону

    def get_queryset(self):
        season = self.request.query_params.get('season', None)
        queryset = Tour.objects.prefetch_related(
            Prefetch('ratings', queryset=Rating.objects.all())
        ).filter(is_published=True)

        if season:
            queryset = queryset.filter(datetour__season=season)

        return queryset.distinct()


class FeedbackListView(generics.ListAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        tour_id = self.request.query_params.get('tour', None)
        if tour_id:
            return Feedback.objects.filter(tour__id=tour_id).select_related('tour')
        return Feedback.objects.all().select_related('tour')


# Представление для списка всех областей
class RegionTourListView(generics.ListAPIView):
    queryset = RegionTour.objects.all()
    serializer_class = RegionTourSerializer


# Представление для отображения конкретной области по ее ID
class RegionTourDetailView(generics.RetrieveAPIView):
    queryset = RegionTour.objects.all()
    serializer_class = RegionTourSerializer


class TourDetailView(generics.RetrieveAPIView):
    queryset = Tour.objects.prefetch_related(
        Prefetch('ratings', queryset=Rating.objects.all())
    ).annotate(average_rating=Avg('ratings__score'))
    serializer_class = TourSerializer
    lookup_field = 'id'  # Будем искать тур по ID
