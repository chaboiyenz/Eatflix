from django.forms import ModelForm
from .models import Subscription

class Subs(ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'
        