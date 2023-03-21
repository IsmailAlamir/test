from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from accounts.api.serializers import RegistrationSerializer,ChangePasswordSerializer,UpdateUserSerializer,UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

from rest_framework.generics import UpdateAPIView,RetrieveAPIView
from accounts.models import CustomUser

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


@api_view(['POST', ])
@permission_classes([AllowAny])
def registration_view(request):

    if request.method == 'POST':

        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name

        else:
            data = serializer.errors
        return Response(data)

# for update the password

class ChangePasswordView(UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


#for update the user information
class UpdateProfileView(UpdateAPIView):


    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


#get user information

class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    lookup_field = 'username'

    def list(self, request):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, username=None):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
