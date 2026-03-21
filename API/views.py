from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from accounts.serializers import UserSerializer
from kkprofiles.models import ProfilingInformations, KKAddress, YouthStatus
from kkprofiles.serializers import (
    ProfilingInformationsSerializer,
    KKAddressSerializer,
    YouthStatusSerializer
)
from events.models import Event
from events.serializers import EventSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


class ProfilingInformationsViewSet(viewsets.ModelViewSet):
    queryset = ProfilingInformations.objects.all()
    serializer_class = ProfilingInformationsSerializer
    


class KKAddressViewSet(viewsets.ModelViewSet):
    queryset = KKAddress.objects.all()
    serializer_class = KKAddressSerializer
    


class YouthStatusViewSet(viewsets.ModelViewSet):
    queryset = YouthStatus.objects.all()
    serializer_class = YouthStatusSerializer
    


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
   