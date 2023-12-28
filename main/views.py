from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from main.models import NetworkUnit
from main.serializers import NetworkUnitSerializer, MyTokenObtainPairSerializer


# Create your views here.

class NetworkUnitListAPIView(ListAPIView):
    serializer_class = NetworkUnitSerializer
    queryset = NetworkUnit.objects.all()
    filter_backends = [SearchFilter, ]
    search_fields = ['contact__country', ]
    permission_classes = [IsAuthenticated]



class NetworkUnitDetailAPIView(RetrieveAPIView):
    serializer_class = NetworkUnitSerializer
    queryset = NetworkUnit.objects.all()
    permission_classes = [IsAuthenticated]



class NetworkUnitCreateAPIView(CreateAPIView):
    serializer_class = NetworkUnitSerializer
    permission_classes = [IsAuthenticated]



class NetworkUnitUpdateAPIView(UpdateAPIView):
    serializer_class = NetworkUnitSerializer
    queryset = NetworkUnit.objects.all()
    permission_classes = [IsAuthenticated]



class NetworkUnitDestroyAPIView(DestroyAPIView):
    queryset = NetworkUnit.objects.all()
    permission_classes = [IsAuthenticated]



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer