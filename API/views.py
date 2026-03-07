from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import UserSerializer




# Create your views here.

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)