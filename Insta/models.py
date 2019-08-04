from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        """
        To solve: ImproperlyConfigured at /insta/post/new/
        No URL to redirect to.
        Either provide a url or define a get_absolute_url method on the Model.
        :return: URL for redirect
        """
        # reverse the URL
        # "helloworld" -> URL
        # search urls.py for URL name=post_detail, parameter post id
        return reverse("post_detail", args=[str(self.id)])


class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )