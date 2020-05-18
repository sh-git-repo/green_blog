from django.views.generic import ListView, TemplateView, DetailView
from .models import Blog
from .helper import page_title, set_active

class HomePageView(ListView):
    model = Blog
    title, active = page_title(), set_active()
    template_name = "blog_home.html"

class AboutPageView(TemplateView):
    title, active = page_title(1), set_active(1)
    template_name = "blog_about.html"

class DetailPageView(DetailView):
    model = Blog
    title = 'TesT_Only'
    template_name = 'blog_detail.html'

# Create your views here.
