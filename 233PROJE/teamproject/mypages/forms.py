from django import forms
from mypages.models import Messages
from mypages.models import FormName


class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = FormName
        fields = '__all__'