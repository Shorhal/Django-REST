from rest_framework import serializers
from apiProj.models import *


class AbonentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonent
        fields = '__all__'


class AbonentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonent
        fields = '__all__'

class AbonentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonent
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'



class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'



class TarifListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = '__all__'

class TarifCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = '__all__'

class TarifDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = '__all__'


