from rest_framework.authentication import BasicAuthentication

from .models import Notes
from .serializers import  NoteSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class UserTodoList(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # get notes related current user
    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)

    # set user to current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
