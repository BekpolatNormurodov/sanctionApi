from django.urls import path
from .views import *

urlpatterns = [
    path('',SanctionApiView.as_view()),
    path('create/',SanctionApiCreate.as_view()),
    path('<int:pk>',SanctionApiUpdate.as_view()),
]