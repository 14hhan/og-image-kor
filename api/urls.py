from django.urls import path
from .views import *

urlpatterns = [
    path('open-graph-image/', OpenGraphImageView.as_view()),
]
