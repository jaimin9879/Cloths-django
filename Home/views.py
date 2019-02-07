from django.shortcuts import render,redirect,get_object_or_404
from .forms import ContactForm,UserForm,ProfileForm,HelpForm,FeedbackForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User
from Cloths import settings

# Create your views here.
def home(request):
    template = 'index.html'
    return render(request, template, {})

def contact(request):
    cform = ContactForm(request.POST)
    if request.method == 'POST':
        if cform.is_valid():
            contact_name = cform.cleaned_data['name']
            contact_email = cform.cleaned_data['email']
            content = cform.cleaned_data['content']
            cform.save()
            subject = 'Hello '+ contact_name + ' From Cloths!'
            message = 'Stay Connected. We whould love to here from you!'
            email_from = settings.EMAIL_HOST_USER
            email_to = [contact_email, ]
            send_mail(subject,message,email_from,email_to)
            return render(request, 'account/msg1.html',
                          {'title':subject, 'content':'We got your message.We will get back to you soon.'})

        else:
            cform = ContactForm()
    template = 'contact.html'
    return render(request,template, {'form' : cform})



def profile(request):
    template = 'profile.html'
    return render(request,template, {})


@login_required
@transaction.atomic
def editprofile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST or None, request.FILES or None, instance = request.user)
        profile_form = ProfileForm(request.POST or None , request.FILES or None, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was succesfully updated')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return  render(request, 'profileform.html', {
        'user_form': user_form,
        'profile_form':profile_form
    })



def deleteProfile(request, pk):
    template = 'profiledelete.html'
    instance = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('home')
    return render(request,template, {'object': instance})


def help(request):
    hform = HelpForm(request.POST)
    if request.method == 'POST':
        if hform.is_valid():
            hform.save()
            messages.success(request, 'We received your query.')
            return redirect('help')
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        hform = HelpForm()
    template = 'help.html'
    return render(request, template, {'form': hform})



def feedback(request):

    fform = FeedbackForm(request.POST)
    if request.method == 'POST':

        if fform.is_valid():
            f = fform.save(commit=False)
            f.user = request.user.profile
            f.save()
            fform.save()
            messages.success(request, 'Thanks for your feedback!')
            return redirect('feedback')
        else:
            messages.warning(request, 'Please give valid input.')
    else:
        fform = FeedbackForm()
    template = 'feedback.html'
    return render(request, template, {'form': fform})

def howitworks(request):
    template = 'howitworks.html'
    return render(request, template, {})

def aboutus(request):
    template = 'aboutus.html'
    return render(request, template, {})

def faq(request):
    template = 'faq.html'
    return render(request, template, {})


def location(request):
    template = 'Location.html'
    return render(request, template, {})