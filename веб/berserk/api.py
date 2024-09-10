from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from berserk.models import Berserk
from berserk.serializers import BerserkSerializer

class BerserkViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Berserk.objects.all()
    serializer_class = BerserkSerializer