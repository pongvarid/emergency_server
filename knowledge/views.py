from rest_framework.viewsets import ModelViewSet
from knowledge.serializers import KnoeledgeSerializer
from knowledge.models import knowledge


class KnoeledgeViewSet(ModelViewSet):
    queryset = knowledge.objects.order_by('pk')
    serializer_class = KnoeledgeSerializer
