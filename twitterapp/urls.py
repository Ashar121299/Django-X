from django.urls import path
from .views import FeatureListView, FeatureDetailView, FeatureCreateView, FeatureUpdateView,FeatureDeleteView,About_Us
urlpatterns = [
    path('', FeatureListView.as_view(), name='list'),
    path('<int:pk>/', FeatureDetailView.as_view(), name='detail'),
    path('create/', FeatureCreateView.as_view(), name='create'),
    path('<int:pk>/update/', FeatureUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', FeatureDeleteView.as_view(), name='delete'),
    path('about',About_Us.as_view(),name='about')
]