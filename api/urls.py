from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


project_list = views.ProjectViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

project_detail = views.ProjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

issue_list = views.IssueViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

issue_detail = views.IssueViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

tip_list = views.TipViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

tip_detail = views.TipViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_list = views.CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comment_detail = views.CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^projects/?$',
        project_list,
        name='project-list'),
    url(r'^projects/(?P<id>[^/]+)/?$',
         project_detail,
         name='project-detail'),
    url(r'^issues/?$',
        issue_list,
        name='issue-list'),
    url(r'^issues/(?P<id>[^/]+)/?$',
         issue_detail,
         name='issue-detail'),
    url(r'^tips/?$',
        tip_list,
        name='tip-list'),
    url(r'^tips/(?P<id>[^/]+)/?$',
         tip_detail,
         name='tip-detail'),
    url(r'^comments/?$',
        comment_list,
        name='comment-list'),
    url(r'^comments/(?P<id>[^/]+)/?$',
        comment_detail,
        name='comment-detail'),
    url(r'^users/?$',
        user_list,
        name='user-list'),
    url(r'^users/(?P<id>[0-9]+)/?$',
        user_detail,
        name='user-detail')
])

urlpatterns += [
    url(r'^auth/token/?$', auth_views.obtain_auth_token),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
]
