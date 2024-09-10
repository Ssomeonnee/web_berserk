from rest_framework import serializers

from berserk.models import Group, Berserk

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class BerserkSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    class Meta:
        model = Berserk
        fields = ['id', 'name', 'group']