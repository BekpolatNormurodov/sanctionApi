from rest_framework import serializers
from api.models import *
from config import settings

# Oper
class SanctionOperserializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField(required=False)

    class Meta:
        model = SanctionOper
        fields = ('id', 'date', 'hackType', 'region', 'shakl1', 'pdf', 'pdf_url')

    def get_pdf_url(self, obj):
        if obj.pdf:
            pdf_url = f"{settings.MEDIA_URL}{obj.pdf}"
            pdf_fied_url = f"{settings.BASE_URL}/sanctionApi{pdf_url}"
            return pdf_fied_url
        return None
    

# IIB
class SanctionIIBserializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField(required=False)

    class Meta:
        model = SanctionIIB
        fields = ('id', 'date', 'region', 'shakl1', 'pdf', 'pdf_url')

    def get_pdf_url(self, obj):
        if obj.pdf:
            pdf_url = f"{settings.MEDIA_URL}{obj.pdf}"
            pdf_fied_url = f"{settings.BASE_URL}/sanctionApi{pdf_url}"
            return pdf_fied_url
        return None