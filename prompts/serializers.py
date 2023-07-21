from rest_framework.serializers import ModelSerializer

from .models import PromptLog


class PromptLogSerializer(ModelSerializer):
    class Meta:
        model = PromptLog
        fields = "__all__"
