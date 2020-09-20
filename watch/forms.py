from django.forms import ModelForm
from .models import Watch
# from .models import Watch, Brand

# class BrandForm(ModelForm):
#     class Meta:
#         model = Brand
#         fields = '__all__'

class WatchForm(ModelForm):
    class Meta:
        model = Watch
        fields = ('name', 'brand', 'price', 'description')