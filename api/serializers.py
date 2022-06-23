from pyexpat import model
from rest_framework import serializers
from tickets.models import Firma, Ariza


class ArizaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Ariza
        exclude = [
            'id',
            'slug',
            'CozumVarMı',
            'Arsivmi',
            'firma_bilgi',
        ]
