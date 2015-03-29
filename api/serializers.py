from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Project, Issue, Tip, Comment


class ShortSerializer(serializers.Serializer):
    # __str__ = serializers.CharField()
    get_absolute_url = serializers.CharField()


class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='user-detail',
        lookup_field='id'
    )
    issues = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='issue-detail',
        lookup_field='id'
    )
    # issues = ShortSerializer()

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'creator', 'members', 'issues', 'created', 'updated')


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ('id', 'name', 'text', 'project', 'payee', 'created', 'updated')


class TipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tip
        fields = ('id', 'amount', 'user', 'issue')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text', 'issue', 'user')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username',)
