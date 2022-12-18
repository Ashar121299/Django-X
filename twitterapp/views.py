from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.urls import reverse_lazy
from .models import feature 

class LIST(ListView):
    template_name = "twitterapp/list.html"
    model = feature 
    context_object_name = 'F'


class FeatureListView(ListView):
    template_name = "twitterapp/feature-list.html"
    model = feature 


class FeatureDetailView(DetailView):
    template_name = "twitterapp/feature-detail.html"
    model = feature


class FeatureCreateView(CreateView):
    template_name = "twitterapp/feature-create.html"
    model = feature
    fields = ['name','purchaser','discription']


class FeatureUpdateView(UpdateView):
    template_name = "twitterapp/feature-update.html"
    model = feature
    fields = ['name','purchaser','discription']


class FeatureDeleteView(DeleteView):
    template_name = "twitterapp/feature-delete.html"
    model = feature
    success_url = reverse_lazy("home")
class About_Us(TemplateView):
    template_name="twitterapp/About.html"






