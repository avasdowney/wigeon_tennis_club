from django.forms import ModelForm
from .models import CreateMember

class MembersForm(ModelForm):
    class Meta:
        model = CreateMember
        fields = '__all__'
