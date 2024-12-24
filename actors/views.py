from rest_framework import generics, status, response, views
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializers import ActorSerializers, ActorNationalitiesSerializers
from app.permissions import GlobalDefaultPermission


class ActorListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class ActorNationalitiesView(views.APIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorNationalitiesSerializers

    def get(self, request):
        return response.Response(data={
            "nationalities": ActorNationalitiesSerializers.get_nationalities(),
        }, status=status.HTTP_200_OK)
        return response.Response(data={}, status=status.HTTP_200_OK)
