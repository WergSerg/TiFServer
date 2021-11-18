from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import  viewsets,pagination
from rest_framework.permissions import AllowAny


from .models import User, Message, Text,Comment
from .serializers import  TextNestedSerilizer



class TextModeViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextNestedSerilizer

