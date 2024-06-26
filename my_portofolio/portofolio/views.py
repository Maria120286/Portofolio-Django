from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from .models import Project, Education


# Create your views here.


def index(request):
    projects = Project.objects.all().order_by('-order')
    educations = Education.objects.all()
    ctx = {'projs': projects, 'edus': educations}
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        msg = request.POST['message']
        ctx['name'] = name
        # print(name,subject,email,message)
        alert = send_mail(
            subject,  # subject
            'Message: ' + msg + '\nFrom: ' + email + '\nName: ' + name,  # message
            email,  # from_email
            ['meetdaxini10@gmail.com'],  # to_email
            fail_silently=True,
        )
        if alert:
            messages.success(request, 'Hey ' + name +
                             ', thanks for reaching out. I will get back to you soon ')
        else:
            messages.error(request, 'error sending message')

        return HttpResponseRedirect(reverse('portfolio:home'))

    return render(request, 'portofolio/index.html', ctx)
