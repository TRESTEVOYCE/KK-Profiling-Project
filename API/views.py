from rest_framework import response
from accounts.serializers import UserSerializer
from accounts.models import User
from kkprofiles.serializers import ProfilingInformationsSerializer, KKAddressSerializer,KKAddressSerializer, YouthStatusSerializer
from kkprofiles.models import ProfilingInformations,KKAddress,YouthStatus
from events.serializers import EventSerializer
from events.models import Event
from rest_framework.decorators import api_view
from rest_framework.views import APIView


#used functions to return data in json format for now will be changed to class based views in the future

class UserList(APIView):

    def get(self, request,pk = None):
        if pk:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        return response.Response(serializer.data)
    
    def post(self, request,pk = None):
        
        if pk:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=200)
        else:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=201)
            return response.Response(serializer.errors, status=400)
        
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return response.Response(status=204)
    
    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=200)
        return response.Response(serializer.errors, status=400)
    
    

class ProfilingInformationsList(APIView):

    def get(self, request,pk = None):
        if pk:
            profiling_informations = ProfilingInformations.objects.get(pk=pk)
            serializer = ProfilingInformationsSerializer(profiling_informations)
        else:
            profiling_informations = ProfilingInformations.objects.all()
            serializer = ProfilingInformationsSerializer(profiling_informations, many=True)
        return response.Response(serializer.data)
    
    def post(self, request,pk = None):
        
        if pk:
            profiling_informations = ProfilingInformations.objects.get(pk=pk)
            serializer = ProfilingInformationsSerializer(profiling_informations, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=200)
        else:
            serializer = ProfilingInformationsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=201)
            return response.Response(serializer.errors, status=400)
        
    def delete(self, request, pk):
        profiling_informations = ProfilingInformations.objects.get(pk=pk)
        profiling_informations.delete()
        return response.Response(status=204)
    
    def put(self, request, pk):
        profiling_informations = ProfilingInformations.objects.get(pk=pk)
        serializer = ProfilingInformationsSerializer(profiling_informations, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=200)
        return response.Response(serializer.errors, status=400)


class KKAddressList(APIView):

    def get(self, request,pk = None):
        if pk:
            kk_address = KKAddress.objects.get(pk=pk)
            serializer = KKAddressSerializer(kk_address)
        else:
            kk_addresses = KKAddress.objects.all()
            serializer = KKAddressSerializer(kk_addresses, many=True)
        return response.Response(serializer.data)
    
    def post(self, request,pk = None):
        
        if pk:
            kk_address = KKAddress.objects.get(pk=pk)
            serializer = KKAddressSerializer(kk_address, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=200)
        else:
            serializer = KKAddressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=201)
            return response.Response(serializer.errors, status=400) 
        
    def delete(self, request, pk):
        kk_address = KKAddress.objects.get(pk=pk)
        kk_address.delete()
        return response.Response(status=204)    
    
    def put(self, request, pk):
        kk_address = KKAddress.objects.get(pk=pk)
        serializer = KKAddressSerializer(kk_address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=200)
        return response.Response(serializer.errors, status=400)

class YouthStatusList(APIView):

    def get(self, request,pk = None):
        if pk:
            youth_status = YouthStatus.objects.get(pk=pk)
            serializer = YouthStatusSerializer(youth_status)
        else:
            youth_statuses = YouthStatus.objects.all()
            serializer = YouthStatusSerializer(youth_statuses, many=True)
        return response.Response(serializer.data)
    
    def post(self, request,pk = None):
        
        if pk:
            youth_status = YouthStatus.objects.get(pk=pk)
            serializer = YouthStatusSerializer(youth_status, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=200)
        else:
            serializer = YouthStatusSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=201)
            return response.Response(serializer.errors, status=400) 
        
    def delete(self, request, pk):
        youth_status = YouthStatus.objects.get(pk=pk)
        youth_status.delete()
        return response.Response(status=204)    
    
    def put(self, request, pk):
        youth_status = YouthStatus.objects.get(pk=pk)
        serializer = YouthStatusSerializer(youth_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=200)
        return response.Response(serializer.errors, status=400)

class EventList(APIView):

    def get(self, request,pk = None):
        if pk:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
        else:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
        return response.Response(serializer.data)   
    
    def post(self, request,pk = None):
        
        if pk:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=200)
        else:
            serializer = EventSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=201)
            return response.Response(serializer.errors, status=400)
        
    def delete(self, request, pk):  
        event = Event.objects.get(pk=pk)
        event.delete()
        return response.Response(status=204) 
    
    