from django.shortcuts import render
from django.views.generic import TemplateView


class HelloWorldView(TemplateView):
    """
    Hello world view for the app.
    """
    template_name = 'test.html'
