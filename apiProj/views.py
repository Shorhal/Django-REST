from django.shortcuts import render
from rest_framework import generics
from apiProj.Serializers import *
from apiProj.models import *


# Create your views here.

class AbonentListView(generics.ListAPIView):
    serializer_class = AbonentListSerializer
    queryset = Abonent.objects.all()


class AbonentCreateView(generics.CreateAPIView):
    serializer_class = AbonentCreateSerializer
    queryset = Abonent.objects.all()


class AbonentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AbonentDetailSerializer
    queryset = Abonent.objects.all()


class EventListView(generics.ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()


class TarifListView(generics.ListAPIView):
    serializer_class = TarifListSerializer
    queryset = Tarif.objects.all()


class TarifCreateView(generics.CreateAPIView):
    serializer_class = TarifCreateSerializer
    queryset = Tarif.objects.all()

class TarifDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TarifDetailSerializer
    queryset = Tarif.objects.all()

