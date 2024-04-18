from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from main.models import AboutModel, BlogModel, ProjectModel, ContactModel, SocialModel


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super(HomeView, self).get_context_data(**kwargs)
        obj = AboutModel.objects.first()
        data['name'] = obj.name_en
        data['description'] = obj.short_description_en
        return data


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        data = super(AboutView, self).get_context_data(**kwargs)
        obj = AboutModel.objects.first()
        data['ava'] = obj.ava.url
        data['description'] = obj.long_description_en
        return data


class BlogListView(ListView):
    template_name = 'blog_list.html'
    model = BlogModel
    context_object_name = 'blogs'
    paginate_by = 9


class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = BlogModel
    context_object_name = 'blog'
    pk_url_kwarg = 'slug'


class ProjectListView(ListView):
    template_name = 'project_list.html'
    model = ProjectModel
    context_object_name = 'projects'
    paginate_by = 9


class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = ProjectModel
    context_object_name = 'project'
    pk_url_kwarg = 'slug'


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    model = ContactModel
    fields = ['name', 'email_or_phone', 'message']
    success_url = 'contact'

    def get_context_data(self, **kwargs):
        data = super(ContactCreateView, self).get_context_data(**kwargs)
        obj = SocialModel.objects.first()
        data['email'] = obj.email
        data['phone'] = obj.phone
        data['github'] = obj.github
        data['linkedin'] = obj.linkedin
        data['telegram'] = obj.telegram
        data['instagram'] = obj.instagram
        data['twitter'] = obj.twitter
        data['facebook'] = obj.facebook
        return data
