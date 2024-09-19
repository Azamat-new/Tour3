from django.urls import path
from .views import BannerIndexlView, BannerDetailView, TourListView, TourSeasonView, FeedbackListView, TourSearchView

urlpatterns = [
    path('banners/', BannerIndexlView.as_view(), name='banner-list-create'),
    path('banners/<int:pk>/', BannerDetailView.as_view(), name='banner-detail'),
    path('tours/', TourListView.as_view(), name='tour-list'),
    path('tours/season/', TourSeasonView.as_view(), name='tour-season'),
    path('feedbacks/', FeedbackListView.as_view(), name='feedback-list'),
    path('tours/search/', TourSearchView.as_view(), name='tour-search'),

]
