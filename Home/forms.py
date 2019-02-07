from django.forms import ModelForm
from .models import Contact,Profile,User,Help,Feedback
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','content']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email',]

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','location','tel','gender','birth_date','img',]

class HelpForm(ModelForm):
    class Meta:
        model = Help
        fields = ['content',]

        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Your Query'})
        }

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['content','user']
