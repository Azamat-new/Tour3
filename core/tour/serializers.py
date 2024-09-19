from django.db.models import Avg
from rest_framework import serializers
from .models import Banner, Tour, Feedback, Rating


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['title', 'banner_image']


class TourSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = ['title', 'description', 'images', 'price', 'average_rating']

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
