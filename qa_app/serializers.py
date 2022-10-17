from rest_framework import serializers
from qa_app.models import Questions,Answers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        user=serializers.CharField(read_only=True)
        asked_date=serializers.DateTimeField(read_only=True)

        model =Questions
        fields ="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        return Questions.objects.create(**validated_data,user=user)
