from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializers


class ActorListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class ActorCreateView(generics.CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class ActorDetailView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class ActorUpdateView(generics.UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class ActorDeleteView(generics.DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers
