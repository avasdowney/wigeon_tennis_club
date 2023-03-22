from django.forms import ModelForm
from .models import AddNews


class AddNewsForm(ModelForm):
    class Meta:
        model = AddNews
        fields = '__all__'