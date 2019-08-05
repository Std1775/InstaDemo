from django.contrib import admin
from Insta.models import Post, InstaUser, Like, UserConnection
# Register your models here.
admin.site.register(Post)
# self defined user model
# need to update forms for users
admin.site.register(InstaUser)
admin.site.register(Like)
admin.site.register(UserConnection)
