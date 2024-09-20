from rest_framework.generics import *
from api.models import *
from .serializers import *
from rest_framework.generics import *

class SanctionApiView(ListAPIView):
    queryset = Sanction.objects.all()
    serializer_class = Sanctionserializer

class SanctionApiCreate(ListCreateAPIView):
    queryset = Sanction.objects.all()
    serializer_class = Sanctionserializer

class SanctionApiUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Sanction.objects.all()
    serializer_class = Sanctionserializer