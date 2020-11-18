from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import CreateView

# Create your views here.

class SignUpView(CreateView):
    pass


# Create your views here.

class HomePageView(TemplateView):

    template_name = 'registration/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Mi Super Web'})