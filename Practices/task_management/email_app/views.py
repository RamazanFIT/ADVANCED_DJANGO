from django.core.mail import send_mail

from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages

from django.conf import settings
from rest_framework import generics

from .models import CV
from .serializers import CVSerializer


class CVListCreateView(generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class CVRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


def share_cv_email(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)

    recipient_email = request.POST.get('email')

    if recipient_email:

        subject = f"{cv.name}'s CV"

        message = f"Check out {cv.name}'s CV at {request.build_absolute_uri(cv.profile_picture.url)}"

        sender_email = settings.EMAIL_HOST_USER

        send_mail(subject, message, sender_email, [recipient_email])

        messages.success(request, "CV shared successfully via email.")

    else:

        messages.error(request, "Please provide a valid email.")

    return redirect('cv_list')


def cv_list(request):
    cvs = CV.objects.all()  # Получаем все резюме
    return render(request, 'cv_list.html', {'cvs': cvs})  # Передаем в шаблон список резюме
