from rest_framework.generics import *
from api.models import *
from .serializers import *
from rest_framework.generics import *


# Oper
class SanctionOperView(ListAPIView):
    queryset = SanctionOper.objects.all()
    serializer_class = SanctionOperserializer

class SanctionOperCreate(ListCreateAPIView):
    queryset = SanctionOper.objects.all()
    serializer_class = SanctionOperserializer

class SanctionOperUpdate(RetrieveUpdateDestroyAPIView):
    queryset = SanctionOper.objects.all()
    serializer_class = SanctionOperserializer


# IIB
class SanctionIIBView(ListAPIView):
    queryset = SanctionIIB.objects.all()
    serializer_class = SanctionIIBserializer

class SanctionIIBCreate(ListCreateAPIView):
    queryset = SanctionIIB.objects.all()
    serializer_class = SanctionIIBserializer

class SanctionIIBUpdate(RetrieveUpdateDestroyAPIView):
    queryset = SanctionIIB.objects.all()
    serializer_class = SanctionIIBserializer



# Prokuratura
class SanctionProkuraturaView(ListAPIView):
    queryset = SanctionProkuratura.objects.all()
    serializer_class = SanctionProkuraturaserializer

class SanctionProkuraturaCreate(ListCreateAPIView):
    queryset = SanctionProkuratura.objects.all()
    serializer_class = SanctionProkuraturaserializer

class SanctionProkuraturaUpdate(RetrieveUpdateDestroyAPIView):
    queryset = SanctionProkuratura.objects.all()


# Oper Star
class SanctionStarView(ListAPIView):
    queryset = SanctionStar.objects.all()
    serializer_class = SanctionStarserializer

class SanctionStarCreate(ListCreateAPIView):
    queryset = SanctionStar.objects.all()
    serializer_class = SanctionStarserializer

class SanctionStarUpdate(RetrieveUpdateDestroyAPIView):
    queryset = SanctionStar.objects.all()
    serializer_class = SanctionStarserializer
    serializer_class = SanctionProkuraturaserializer