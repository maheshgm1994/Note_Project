from rest_framework import serializers

from .models import Notes


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('name', 'text','added_on','updated_on')

# class UserNoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserNote
#         fields = ('name', 'text','added_on','updated_on')
