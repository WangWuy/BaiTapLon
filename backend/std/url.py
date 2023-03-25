from django.urls import path, re_path, include
from .import views
from .admin import admin_site
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('post-category', views.PostCategoryViewSet)
router.register('posts', views.PostViewSet)
router.register('comments', views.CommentsViewSet)
router.register('livestream', views.LivestreamViewSet)
router.register('questions', views.QuestionsViewSet)
router.register('falcuty', views.FalcutyViewSet)
router.register('major', views.MajorViewSet)
router.register('slider', views.SliderViewSet)
router.register('university', views.UniversityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls)
]