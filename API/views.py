from rest_framework import response
from accounts.serializers import UserSerializer
from accounts.models import User
from kkprofiles.serializers import ProfilingInformationsSerializer, KKAddressSerializer,KKAddressSerializer, YouthStatusSerializer
from kkprofiles.models import ProfilingInformations,KKAddress,YouthStatus
from events.serializers import EventSerializer
from events.models import Event
from rest_framework.decorators import api_view


#used functions to return data in json format for now will be changed to class based views in the future


@api_view(['GET'])
def UserList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return response.Response(serializer.data)

@api_view(['GET'])
def ProfilingInformationsList(request):     
    profiling_informations = ProfilingInformations.objects.all()
    serializer = ProfilingInformationsSerializer(profiling_informations, many=True)
    return response.Response(serializer.data)
    
@api_view(['GET'])
def KKAddressList(request):
    kk_addresses = KKAddress.objects.all()
    serializer = KKAddressSerializer(kk_addresses, many=True)
    return response.Response(serializer.data)

@api_view(['GET'])
def YouthStatusList(request):
    youth_statuses = YouthStatus.objects.all()
    serializer = YouthStatusSerializer(youth_statuses, many=True)
    return response.Response(serializer.data)

@api_view(['GET'])
def EventList(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return response.Response(serializer.data)   

