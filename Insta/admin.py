from django.contrib import admin
from Insta.models import Post, InstaUser
# Register your models here.
admin.site.register(Post)
# self defined user model
# need to update forms for users
admin.site.register(InstaUser)

