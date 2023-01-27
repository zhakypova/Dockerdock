
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from account.views import AuthorRegisterView
from news import views as news_views
from account import views as account_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


account_router = DefaultRouter()
account_router.register('register', AuthorRegisterView)

news_router = DefaultRouter()
news_router.register('news', news_views.NewsListCreateAPIView)

schema_view = get_schema_view(
    openapi.Info(
        title="exam API",
        default_version='v0.1',
        description="API для новостного сайта",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('api/news/', include('news.urls')),
    # path('api/account/token', obtain_auth_token),
    # path('', include('account.urls')),
    # # path('api/account/', include(account_router.urls)),
    # # path('api/news/', include(news_router.urls)),
    #
    # # path('api/account/register/', account_views.AuthorRegisterView.as_view()),
    # path('/api/news/', news_views.NewsListCreateAPIView.as_view()),
    # path('/api/news/<news_id>', news_views.NewsRetrieveUpdateDestroyAPIView.as_view()),
    # path('/api/news/<news_id>/comments/', news_views.CommentListCreateAPIView.as_view()),
    # path('/api/news/<news_id>/comments/<pk>/', news_views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    # path('/api/statuses/', news_views.StatusListCreateAPIView.as_view()),
    # path('/api/statuses/<pk>', news_views.StatusRetrieveUpdateDestroyAPIView.as_view()),
    # path('/api/news/<news_id>/<slug>/', news_views.NewsStatusRetrieveUpdateDestroyAPIView.as_view()),
    # path('/api/news/<news_id>/comments/<comment_id>/<slug>/',
    #      news_views.CommentStatusRetrieveUpdateDestroyAPIView.as_view()),
    #
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui'),
    # path('json_doc/', schema_view.without_ui(cache_timeout=0), name='json_doc'),

]
