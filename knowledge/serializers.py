from rest_framework.serializers import ModelSerializer
from knowledge.models import knowledge


class KnoeledgeSerializer(ModelSerializer):

    class Meta:
        model = knowledge
        fields = '__all__'
