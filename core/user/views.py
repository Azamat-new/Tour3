from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MyUser
from .serializers import UserRegisterSerializer, UserProfileListSerializer, MyUserSerializer


class MyUserViewSet(APIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

class UserRegisterView(APIView):
    @swagger_auto_schema(request_body=UserRegisterSerializer)
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Пользователь успешно зарегистрирован.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Ошибка при регистрации.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(responses={200: UserProfileListSerializer()})
    def get(self, request):
        user_object = get_object_or_404(MyUser, id=request.user.id)
        serializer = UserProfileListSerializer(user_object)
        return Response({
            'message': 'Информация о пользователе успешно получена.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserProfileListSerializer)
    def patch(self, request):
        user_object = get_object_or_404(MyUser, id=request.user.id)
        serializer = UserProfileListSerializer(user_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Профиль успешно обновлен.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Ошибка при обновлении профиля.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user_object = get_object_or_404(MyUser, id=request.user.id)
        user_object.delete()
        return Response({
            'message': 'Профиль успешно удален.'
        }, status=status.HTTP_204_NO_CONTENT)