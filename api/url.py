from django.urls import path
from .views import *

urlpatterns = [
    # Oper
    path('',SanctionOperView.as_view()),
    path('create/',SanctionOperCreate.as_view()),
    path('<int:pk>',SanctionOperUpdate.as_view()),

    # IIB
    # path('iib/',SanctionIIBView.as_view()),
    # path('iib/create/',SanctionIIBCreate.as_view()),
    # path('iib/<int:pk>',SanctionIIBUpdate.as_view()),
]