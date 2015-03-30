import uuid
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Common(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(Common):
    name = models.TextField()
    description = models.TextField()
    creator = models.ForeignKey(User, related_name='created_projects')
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'id': self.id})


class Issue(Common):
    name = models.TextField()
    text = models.TextField()
    project = models.ForeignKey(Project, related_name='issues')
    payee = models.ForeignKey(User, related_name='paid_issues', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('issue-detail', kwargs={'id': self.id})


class Tip(Common):
    amount = models.IntegerField()
    user = models.ForeignKey(User, related_name='tips')
    issue = models.ForeignKey(Issue, related_name='tips')

    def __str__(self):
        return self.amount + self.issue

    def get_absolute_url(self):
        return reverse('tip-detail', kwargs={'id': self.id})


class Comment(Common):
    text = models.TextField()
    issue = models.ForeignKey(Issue, related_name='comments')
    user = models.ForeignKey(User, related_name='comments')

    def __str__(self):
        return self.text[:10]

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'id': self.id})


from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
