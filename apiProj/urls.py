from django.urls import path, include
from apiProj.views import *

urlpatterns = [
    path('abonent/all/', AbonentListView.as_view()),
    path('abonent/create/', AbonentCreateView.as_view()),
    path('abonent/detail/<int:pk>/',AbonentDetailView.as_view()),
    path('event/all/', EventListView.as_view()),
    path('event/create/', EventCreateView.as_view()),
    path('event/detail/<int:pk>/', EventDetailView.as_view()),
    path('tarif/all/', TarifListView.as_view()),
    path('tarif/create/', TarifCreateView.as_view()),
    path('tarif/detail/<int:pk>/', TarifDetailView.as_view()),
]