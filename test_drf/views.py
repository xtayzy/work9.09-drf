from django.db.models import Model
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from adrf.serialisers import TestModelSerializer
from test_drf.models import TestModel


# Create your views here.


class ModelListView(ListAPIView):
    serializer_class = TestModelSerializer
    queryset = TestModel.objects.all()


class ModelDetailView(RetrieveAPIView):
    serializer_class = TestModelSerializer
    queryset = TestModel.objects.all()


class ModelCreateView(CreateAPIView):
    serializer_class = TestModelSerializer
    queryset = TestModel.objects.all()


class ModelUpdateView(RetrieveUpdateAPIView):
    serializer_class = TestModelSerializer
    queryset = TestModel.objects.all()


class ModelDeleteView(RetrieveDestroyAPIView):
    serializer_class = TestModelSerializer
    queryset = TestModel.objects.all()

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()

        return Response('удалено')





