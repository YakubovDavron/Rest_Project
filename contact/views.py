from rest_framework import generics
from .models import Contact, ContactInfo
from .seri import ContactSerializer, ContactInfoSerializer


# Create your views here.

class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoApiView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
