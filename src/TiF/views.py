from rest_framework import viewsets,  status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import  IsAdminUser, IsAuthenticated

from src.TiF.models import  Text,  Category,  User
from src.TiF.serializers import TextNestedSerilizer, \
    CategoryReverseSerialize, \
    CreateTextSerializer, \
    CategorySerialize, \
    UserRegistrSerializer





class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [IsAdminUser]


    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class TextModeViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextNestedSerilizer
    permission_classes = [IsAuthenticated]


class CategoryTree(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryReverseSerialize
    permission_classes = [IsAuthenticated]


class CreateText(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = CreateTextSerializer
    permission_classes = [IsAuthenticated]


class FoundationTree(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialize
    permission_classes = [IsAdminUser]
