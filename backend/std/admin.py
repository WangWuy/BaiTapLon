from django.contrib import admin
from django.utils.html import mark_safe
from .models import User, Post, Post_category, Slider, Falcuty, Major, University_info, Questions, Livestream_info
from django.urls import path
from django.template.response import TemplateResponse
from django.contrib.auth.models import Permission

# Custom lại trang admin 
class StdAppAdminSite(admin.AdminSite):
    site_title = 'Quản lý'
    site_header = 'HỆ THỐNG QUẢN LÝ TUYỂN SINH'
    index_title = 'Trang quản trị'
    def get_urls(self):
        return [
            path('std-stats/', self.std_stats)
        ]  + super().get_urls()
    
    def std_stats(self, request):
        user_count = User.objects.count()

        return TemplateResponse(request, 'admin/std-stats.html', {
            'user_count': user_count
        })

admin_site = StdAppAdminSite('mystd')


class UsersAmin(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "last_name", "is_active"]  # Các trường hiển thị trên web
    list_display_links = ["username"]   # Các trường có gắn link dẫn đến trang detail
    search_fields = ["username", "first_name", "last_name"]
    list_filter = ["username", "first_name", "last_name"]
    readonly_fields = ["avatar"] # Chỉ cho phép đọc

    def avatar(self, user):
        return mark_safe("<img src='/static/avt/{avatar_url}' alt='{alt}' />".format(avatar_url=user.avatar_url.name, alt=user.first_name))
    

class PostAmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "post_category", "status"]
    list_display_links = ["title"]   # Các trường có gắn link dẫn đến trang detail

class Post_categoryAmin(admin.ModelAdmin):
    list_display = ["id", "title", "status"]
    list_display_links = ["title"]

class SliderAmin(admin.ModelAdmin):
    list_display = ["id", "title", "banner_url", "discription", "status"]
    list_display_links = ["title"]

class FalcutyAmin(admin.ModelAdmin):
    list_display = ["id", "falcuty_name", "falcuty_gpa", "discription", "website_url"]
    list_display_links = ["falcuty_name"]

class MajorAmin(admin.ModelAdmin):
    list_display = ["id", "major_name", "discription", "falcuty", "status"]
    list_display_links = ["major_name"]

class University_infoAmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('/static/css/main.css',)
        }
    list_display = ["id", "university_name", "logo_url", "phone_number"]
    list_filter = ["university_name", "phone_number"]
    list_display_links = ["university_name"]
    # readonly_fields = ["logo"]

    # def logo_url(self, uni):
    #     return mark_safe("<img src='/static/{logo_url} alt='{alt}'/>".format(logo_url=uni.avatar.logo_url, alt=uni.university_name))


class QuestionsAmin(admin.ModelAdmin):
    list_display = ["id", "content", "user", "livestream_info"]
    list_display_links = ["content"]

class Livestream_infoAmin(admin.ModelAdmin):
    list_display = ["id", "discription", "start_time", "end_time", "start_question_time", "end_question_time", "status"]

# Register your models here.
admin_site.register(User, UsersAmin)
admin_site.register(Post, PostAmin)
admin_site.register(Post_category, Post_categoryAmin)
admin_site.register(Slider, SliderAmin)
admin_site.register(Falcuty, FalcutyAmin)
admin_site.register(Major, MajorAmin)
admin_site.register(University_info, University_infoAmin)
admin_site.register(Questions, QuestionsAmin)
admin_site.register(Livestream_info, Livestream_infoAmin)
admin_site.register(Permission)
