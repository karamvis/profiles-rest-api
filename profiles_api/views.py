from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions



class HelloAPIView(APIView):
    """Hello APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview=[
        'Uses HTTP methods as function(get,post,patch,put,delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello world with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating n object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle patching of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handle delete of an object"""

        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset=[
        'Uses actions (list,create,retrieve,update,partial_update and destroy)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """Create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handle etting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating an object by its ID"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handling part of the object"""
        return Response({'http_post':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle remove an object"""
        return Response({'http_post':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Hanndle creating and updating profile"""
    serializer_class=serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
