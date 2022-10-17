from django.shortcuts import render
from qa_app.models import Questions
from qa_app.serializers import UserSerializer,QuestionSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response

# Create your views here.
class UsersView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class QuestionView(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()

    def create(self,request,*args,**kwargs):
        user=request.user
        serializer=QuestionSerializer(data=request.data,context={"user":user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

