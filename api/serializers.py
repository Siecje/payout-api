from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Project, Issue, Tip, Comment


class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='user-detail'
    )
    issues = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='issue-detail'
    )

    class Meta:
        model = Project
        fields = ('pk', 'name', 'description', 'creator', 'members', 'issues', 'created', 'updated')


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ('pk', 'name', 'text', 'project', 'payee', 'created', 'updated')


class TipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tip
        fields = ('pk', 'amount', 'user', 'issue')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('pk', 'text', 'issue', 'user')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('url', 'username',)
