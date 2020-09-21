from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import CustomUser
from .forms import CustomUserCreateForm, CustomUserUpdateForm

# Create your views here.
class CustomerDashboardView(View):
    template_name = 'customer/customer.html'
    
    def get(self, request):
        # customer = CustomUser.objects.filter(is_superuser=False)
        # context = { 'customer_list': customer, 'title': 'Dashboard', 'type': 'customer' }
        # return render(request, self.template_name, context)
        return render(request, self.template_name)
    
    # def post(self, request):
    #     id = request.POST.get('object_id')
    #     type_of_form = request.POST.get('type_of_form')
    #     custom_user = get_object_or_404(CustomUser, id = id)
    #     if type_of_form == 'reg':    
    #         form = CustomUserUpdateForm(request.POST, instance=custom_user)
    #         if form.is_valid():
    #             form.save()
    #     else:
    #         custom_user.delete()
    #     return redirect('/admin/customer/')
        
class CustomerRegisterView(View):
    template_name = 'customer/customerReg.html'
    context = { 'title': 'Register', 'type': 'Customer' }

    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        form = CustomUserCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/admin/customer/')
        else:
            self.context['errors'] = form.error_messages
            for key, val in request.POST.dict().items():
                if key not in ('csrfmiddlewaretoken', 'password1', 'password2'):
                    self.context[key] = val
            return render(request, self.template_name, self.context)
    
    