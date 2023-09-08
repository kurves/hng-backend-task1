from django.urls import path
from .views import EndPointAPIView

urlpatterns=[
    #Homepage
    path('', EndPointAPIView.as_view()),
]