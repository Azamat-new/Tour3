from django.db.models import Avg
from rest_framework import serializers
from .models import Banner, Tour, Feedback, Rating, RegionTour, DateTour, TourImage


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['title', 'banner_image']


class RegionTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionTour
        fields = ['title', 'description', 'slug', 'image']


class DateTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTour
        fields = ['start_date', 'end_date', 'tour_type', 'season']


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = ['image']


class TourSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    date_tour = DateTourSerializer(many=True)  # Для отображения связанных дат тура
    region = RegionTourSerializer(many=True)  # Для отображения регионов тура
    images = TourImageSerializer(many=True)  # Для отображения изображений тура

    class Meta:
        model = Tour
        fields = ['title', 'description', 'price', 'average_rating', 'date_tour', 'region', 'images']

    def get_average_rating(self, obj):
        return obj.ratings.aggregate(average=Avg('score'))['average'] or None


class FeedbackSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = ['user_name', 'comment', 'children']

    def get_children(self, obj):
        # Используем "self" для рекурсивного вызова сериализатора
        return FeedbackSerializer(obj.children.all(), many=True).data if obj.children.exists() else None


class DetailSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = ['title', 'description', 'image', 'start_date', 'end_date', 'rating', 'participants_price', 'max_participants']

    def get_rating(self, obj):
        average_rating = obj.ratings.aggregate(Avg('score'))['score__avg']
        return average_rating if average_rating is not None else 0
