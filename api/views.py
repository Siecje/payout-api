from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Project, Issue, Tip, Comment
from .serializers import ProjectSerializer, IssueSerializer, TipSerializer, \
                         CommentSerializer, UserSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'projects': reverse('project-list', request=request, format=format),
        'issues': reverse('issue-list', request=request, format=format),
        'tips': reverse('tip-list', request=request, format=format),
        'comments': reverse('comment-list', request=request, format=format),
    })


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TipViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = TipSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
