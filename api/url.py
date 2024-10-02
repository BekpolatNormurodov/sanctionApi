from django.urls import path
from .views import *

urlpatterns = [
    # Oper
    path('',SanctionOperView.as_view()),
    path('create/',SanctionOperCreate.as_view()),
    path('<int:pk>',SanctionOperUpdate.as_view()),

    # Oper Star
    path('star/',SanctionStarView.as_view()),
    path('star/create/',SanctionStarCreate.as_view()),
    path('star/<int:pk>',SanctionStarUpdate.as_view()),

    # IIB
    path('iib/',SanctionIIBView.as_view()),
    path('iib/create/',SanctionIIBCreate.as_view()),
    path('iib/<int:pk>',SanctionIIBUpdate.as_view()),

    # Prokuratura
    path('prokuratura/',SanctionProkuraturaView.as_view()),
    path('prokuratura/create/',SanctionProkuraturaCreate.as_view()),
    path('prokuratura/<int:pk>',SanctionProkuraturaUpdate.as_view()),
]