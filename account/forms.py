from django.forms import ModelForm
from members.models import CustomUser
   
class PaymentFlagForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('payment_flag', )