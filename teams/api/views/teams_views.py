from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from teams.api.serializers.teams_serializers import TeamSerializer
from teams.models import Teams


class TeamAPIList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Teams.objects.all().order_by('-created_on')
    serializer_class = TeamSerializer


class CreateTeam(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer


class UpdateTeam(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer


class RetrieveTeam(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer


class DestroyTeam(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer
