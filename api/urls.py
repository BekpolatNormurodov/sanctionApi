from django.urls import path
from .views import *

urlpatterns = [
    # Test urls
    path('',TestApiView.as_view()),
    path('create/',TestApiCreate.as_view()),
    path('<int:pk>',TestApiUpdate.as_view()),
]