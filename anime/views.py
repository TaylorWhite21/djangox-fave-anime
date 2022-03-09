from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Anime


class AnimeListView(ListView):
   template_name ='anime/anime-list.html'
   model = Anime

class AnimeDetailView(DetailView):
  template_name = 'anime/anime-detail.html'
  model = Anime
  content_object_name = 'anime-detail'

class AnimeCreateView(CreateView):
	template_name = 'anime/anime-create.html'
	model = Anime
	fields = ['name', 'description','owner']
class AnimeUpdateView(UpdateView):
	template_name = 'anime/anime-update.html'
	model = Anime
	fields = ['name', 'description','owner']

class AnimeDeleteView(DeleteView):
	template_name = 'anime/anime-delete.html'
	model = Anime
	success_url = reverse_lazy('anime-list')

