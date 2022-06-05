from django.forms import ModelForm
from .models import Message, Profile

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'



class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        