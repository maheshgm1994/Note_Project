from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Notes
from .serializers import NoteSerializer


class NoteList(generics.ListCreateAPIView):
    #Returns queryset to be used by class
    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)

    # Called before a new entry is inserted
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class NoteDetails(generics.RetrieveUpdateDestroyAPIView):
    # # Returns queryset to be used by class
    # def get_queryset(self):
    #     return Notes.objects.filter()

    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
