from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from .serializers import ContactUsSerializer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class ContactUsViewset(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        cont_us_inst = serializer.save()

        email_subject = "Confirmation Of Your Contact Submission"
        email_body = render_to_string('contact_email.html',{
            'name': cont_us_inst.name,
        })
        email = EmailMultiAlternatives(
            subject = email_subject,
            body='',
            to = [cont_us_inst.email]
        )
        email.attach_alternative(email_body,"text/html")
        email.send()

        return Response({'message': 'Your message has been sent! Check your email for confirmation.'},status=status.HTTP_201_CREATED)
