from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .models import User, University_info, Post_category, Post, Comments, Livestream_info, Questions, Falcuty, Major, Slider
from .serializers import UniversitySerializer, UserSerializer, PostCategorySerializer, PostSerializer, CommentsSerializer, LivestreamSerializer, QuestionsSerializer, FalcutySerializer, MajorSerializer, SliderSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

# Thi sinh, user
class UserViewSet(viewsets.ViewSet,
                  generics.ListAPIView,
                  generics.CreateAPIView,
                  generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    # Set quyen xem thong tin user:
    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return [permissions.IsAuthenticated()]
        
    #     return [permissions.AllowAny()]
        
        

# Thong tin truong
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University_info.objects.filter(status=True)
    serializer_class = UniversitySerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated()]

    # viet schema cho redoc
    @swagger_auto_schema(
        operation_description='Tắt trạng thái 1 thông tin của trường',
        responses={
            status.HTTP_200_OK: UniversitySerializer()
        }
    )
    # api thay doi trang thai
    @action(methods=['post'], detail=True, url_path="change-status", url_name="change-status")
    
    def hide_university(self, request, pk):
        try:
            u = University_info.objects.get(pk=pk)
            u.status = False
            u.save()
        except University_info.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=UniversitySerializer(u, context={'request': request}).data,
                        status=status.HTTP_200_OK)

# Danh muc bai post
class PostCategoryViewSet(viewsets.ModelViewSet):
    queryset = Post_category.objects.filter(status=True)
    serializer_class = PostCategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
        
    #     return [permissions.IsAuthenticated()]
    # api thay doi trang thai
    @action(methods=['post'], detail=True, url_path="change-status", url_name="change-status")
    
    def hide_post_category(self, request, pk):
        try:
            u = Post_category.objects.get(pk=pk)
            u.status = False
            u.save()
        except Post_category.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=PostCategorySerializer(u, context={'request': request}).data,
                        status=status.HTTP_200_OK)
    
# Bai post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # api thay doi trang thai
    @action(methods=['post'], detail=True, url_path="change-status", url_name="change-status")
    
    def hide_post(self, request, pk):
        try:
            u = Post.objects.get(pk=pk)
            u.status = False
            u.save()
        except Post.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=PostSerializer(u, context={'request': request}).data,
                        status=status.HTTP_200_OK)

# Binh luan cua thi sinh
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    
# Thong tin cua livestream
class LivestreamViewSet(viewsets.ModelViewSet):
    queryset = Livestream_info.objects.filter(status=True)
    serializer_class = LivestreamSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # api thay doi trang thai
    @action(methods=['post'], detail=True, url_path="change-status", url_name="change-status")
    
    def hide_livestream(self, request, pk):
        try:
            u = Livestream_info.objects.get(pk=pk)
            u.status = False
            u.save()
        except Livestream_info.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=LivestreamSerializer(u, context={'request': request}).data,
                        status=status.HTTP_200_OK)
    
# Tong hop cau hoi
class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = [permissions.IsAuthenticated]

# Thong tin cua khoa
class FalcutyViewSet(viewsets.ModelViewSet):
    queryset = Falcuty.objects.filter(status=True)
    serializer_class = FalcutySerializer
    # permission_classes = [permissions.IsAuthenticated]

    # api thay doi trang thai
    @action(methods=['post'], detail=True, url_path="change-status", url_name="change-status")
    
    def hide_falcuty(self, request, pk):
        try:
            u = Falcuty.objects.get(pk=pk)
            u.status = False
            u.save()
        except Falcuty.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=FalcutySerializer(u, context={'request': request}).data,
                        status=status.HTTP_200_OK)
    
# Thong tin cua lop
class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.filter(status=True)
    serializer_class = MajorSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # api thay doi trang thai
    @action(methods=['post'], detail=True, url_path="change-status", url_name="change-status")
    
    def hide_major(self, request, pk):
        try:
            u = Major.objects.get(pk=pk)
            u.status = False
            u.save()
        except Major.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=MajorSerializer(u, context={'request': request}).data,
                        status=status.HTTP_200_OK)
    
# Thong tin cua lop
class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.filter(status=True)
    serializer_class = SliderSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # api thay doi trang thai
    @action(methods=['post'], detail=True, url_path="change-status", url_name="change-status")
    
    def hide_slider(self, request, pk):
        try:
            u = Slider.objects.get(pk=pk)
            u.status = False
            u.save()
        except Slider.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=SliderSerializer(u, context={'request': request}).data,
                        status=status.HTTP_200_OK)