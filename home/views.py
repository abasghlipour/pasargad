from django.contrib.sites.models import Site
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import sitemaps


class HomeView(TemplateView):
    template_name = 'home/index.html'



class MySitemap(sitemaps.Sitemap):
    def items(self):
        return [Site.objects.get_current()]

    def lastmod(self, obj):
        return obj.last_modified

