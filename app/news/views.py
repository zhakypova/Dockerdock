from rest_framework import generics
from rest_framework import views
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import News, NewsStatus, Comment, Status
from .permissions import IsAuthorPermission
from .serializers import NewsSerializer, CommentSerializer, StatusSerializer




class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthorPermission, ]
    # pagination_class = NewsNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', ]
    ordering_fields = ['created', ]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author
        )


class NewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthorPermission, ]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs.get('news_id'))

    def perform_create(self, serializer):
        serializer.save(
            news_id=self.kwargs.get('news_id'),
            author=self.request.user.author
        )


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs.get('news_id'))


class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser, ]


class StatusRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser, ]


class StatusNewsCreateAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        news = News.objects.get(id=kwargs.get('news_id'))
        status = Status.objects.get(slug=kwargs.get('slug'))
        news_status = NewsStatus.objects.create(
            status=status,
            news=news,
            author=request.user.author
        )
        return Response({'message': 'Status added'}, status=201)
