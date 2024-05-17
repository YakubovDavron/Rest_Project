from django.urls import path
from .views import ContactAPIView,ContactInfoApiView

urlpatterns = [
    path('', ContactAPIView.as_view(), name='contact'),
    path('info/', ContactInfoApiView.as_view(), name='contact-information')
]
