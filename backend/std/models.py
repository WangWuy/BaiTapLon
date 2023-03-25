from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
    avatar_url = models.ImageField(upload_to='avt/%Y/%m', null=True, default=None)
    # gender = models.SmallIntegerField(null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True)
    phone_number = models.CharField(max_length=11)
    address = models.TextField(null=True)

class Post_category(models.Model):
    class Meta:
        ordering = ['-id']  # sắp giảm theo id

    title = models.CharField(max_length=255, null=False, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255, null=False, unique=True)
    content = models.TextField(null=False)
    post_category = models.ForeignKey(Post_category, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def _str_(self):
        return self.title



class Comments(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.content
    
class Livestream_info(models.Model):
    discription = models.TextField(null=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    start_question_time = models.DateTimeField(null=False)
    end_question_time = models.DateTimeField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.discription 

class Questions(models.Model):
    livestream_info = models.ForeignKey(Livestream_info, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.content

class Falcuty(models.Model):
    falcuty_name = models.CharField(max_length=50, null=False)
    falcuty_gpa = models.FloatField(null=False)
    discription = models.TextField(null=True)
    website_url = models.TextField(null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.falcuty_name 

class Major(models.Model):
    major_name = models.TextField(null=True)
    discription = models.TextField(null=False)
    falcuty = models.ForeignKey(Falcuty, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.major_name 

class University_info(models.Model):
    university_name = models.CharField(max_length=255, null=False, unique=True)
    logo_url = models.ImageField(upload_to='avt/%Y/%m', default=None, null=True)
    website_url = models.TextField(null=True)
    address = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.university_name
    
class Slider(models.Model):
    title = models.TextField()
    banner_url = models.ImageField(upload_to='avt/%Y/%m', default=None, null=True)
    discription = models.TextField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title 
    
