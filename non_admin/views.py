from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    template_name = "non_admin/index.html"
    
    def get(self, request, *args, **kwargs):
        context = { 'title': 'Home', 'scroll': True }
        return render(request, self.template_name, context=context)

class Login(View):
    template_name = "non_admin/login.html"
    
    def get(self, request, *args, **kwargs):
        context = { 'title': 'Login', 'scroll': False }
        return render(request, self.template_name, context=context)
