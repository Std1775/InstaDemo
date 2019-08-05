from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )

    def get_connections(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])

    def __str__(self):
        return self.username

# UserConnection Example
# connection1 -> A follows B
# connection2 -> A follows C
# connection3 -> D follows A

# A -> creator, get friend list of A: connection1 and connection2
# A.friend_set -> connection 3


class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friendship_creator_set")
    following = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friend_set")

    def __str__(self):
        return self.creator.username + ' follows ' + self.following.username


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='my_posts'
    )
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )

    def get_like_count(self):
        return self.likes.count()

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


# example of how related_name works
# like1 -> std1775.like post1
# like2 -> test like post1
# post1.likes -> (like1, like2)
# std1775.like -> like1
# test.like -> like2


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        # when post is deleted, Like will be deleted as well like a CASCADE
        on_delete=models.CASCADE,
        related_name='likes'
    )

    user = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        # (post, user) pair is unique
        unique_together = ("post", "user")

    def __str__(self):
        return "Like: " + self.user + ' likes ' + self.post

# TODO: Implement comment model