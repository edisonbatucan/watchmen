from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Watch
from .forms import WatchForm

# Create your views here.
class WatchDashboardView(View):
    template_name = 'watch/watch.html'

    def get(self, request):
        watch = Watch.objects.all()
        context = { 'watch_list': watch, 'title': 'Dashboard', 'type': 'watch' }
        return render(request, self.template_name, context)
    
    def post(self, request):
        id = request.POST.get('object_id')
        watch = get_object_or_404(Watch, id = id)
        form = WatchForm(request.POST, instance=watch)
        
        if form.is_valid():
            form.save()
        return redirect('/admin/watch/')
    
class WatchRegisterView(View):
    template_name = 'watch/watchReg.html'
    context = { 'title': 'Register', 'type': 'Watch' }

    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        form = WatchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/admin/watch/')
        else:
            self.context['errors'] = form.error_messages
            for key, val in request.POST.dict().items():
                if key not in ('csrfmiddlewaretoken'):
                    self.context[key] = val
            return render(request, self.template_name, self.context)
    
    
