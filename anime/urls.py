from django.urls import path
from django.shortcuts import render
from .views import *

urlpatterns = [
  path('', AnimeListView.as_view(), name='anime-list'),
  path('<int:pk>/', AnimeDetailView.as_view(), name='anime-detail'),
  path('new/',AnimeCreateView.as_view(), name='anime-create'),
	path('<int:pk>/delete',AnimeDeleteView.as_view(), name='anime-delete'),
	path('<int:pk>/edit',AnimeUpdateView.as_view(), name='anime-update')
]
