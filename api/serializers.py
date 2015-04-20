from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Project, Issue, Tip, Comment


class RelatedIssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'url', 'name')
        lookup_field = 'id'


class RelatedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'url')
        lookup_field = 'id'


class RelatedCommentSerializer(serializers.HyperlinkedModelSerializer):
    user = RelatedUserSerializer(
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'user')
        lookup_field = 'id'


class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='user-detail',
        lookup_field='id'
    )
    issues = RelatedIssueSerializer(
        many=True,
        read_only=True
    )
    creator = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'creator', 'members', 'issues', 'created', 'updated')


class IssueSerializer(serializers.ModelSerializer):
    comments = RelatedCommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Issue
        fields = ('id', 'name', 'text', 'project', 'comments', 'payee', 'created', 'updated')


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
