from rest_framework import serializers
from qa_app.models import Questions,Answers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        user=serializers.CharField(read_only=True)
        asked_date=serializers.DateTimeField(read_only=True)

        model =Questions
        fields ="__all__"

