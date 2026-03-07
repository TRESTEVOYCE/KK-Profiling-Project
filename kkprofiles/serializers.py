from rest_framework import serializers
from .models import ProfilingInformations, KKAddress,YouthStatus



class KKAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = KKAddress
        fields = '__all__'

class YouthStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouthStatus
        fields = '__all__'

class ProfilingInformationsSerializer(serializers.ModelSerializer):
    address = KKAddressSerializer(many=True, read_only=True)
    youth_status = YouthStatusSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProfilingInformations
        fields = '__all__'