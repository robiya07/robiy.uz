from django.urls import path
from main.views import HomeView, AboutView, BlogListView, BlogDetailView, ProjectListView, ProjectDetailView, \
    ContactCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('blogs', BlogListView.as_view(), name='blogs'),
    path('blogs/<slug:slug>', BlogDetailView.as_view(), name='blog_det'),
    path('portfolio', ProjectListView.as_view(), name='portfolio'),
    path('portfolio/<slug:slug>', ProjectDetailView.as_view(), name='portfolio_det'),
    path('contact', ContactCreateView.as_view(), name='contact'),
]
