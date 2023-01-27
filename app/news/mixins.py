from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response


class StatusMixin:
    status_model = None
    object_name = None

    def status(self, request, status):
        obj = self.get_object()
        author = request.user
        kwargs = {
            self.object_name: obj,
            'author': author,
            'status': status
        }
        try:
            new_status = self.status_model(**kwargs)
            new_status.save()
        except IntegrityError:
            this_status = self.status_model.objects.filter(**kwargs).first()
            this_status.delete()
        data = {
            "massage": f'Status успешно присвоен id = {status.id} пользователем id {request.user.id}'
        }
        return Response(data, status=200)


class NewsStatusMixin:
    news_status_model = None
    object_name = None

    def news_status(self, request, news_status):
        obj = self.get_object()
        author = request.user
        kwargs = {
            self.object_name: obj,
            'author': author,
            'news_status': news_status
        }
        try:
            new_news_status = self.news_status_model(**kwargs)
            new_news_status.save()
        except IntegrityError:
            this_news_status = self.news_status.objects.filter(**kwargs).first()
            this_news_status.delete()
        data = {
            "massage": f'News_Status успешно присвоен id = {news_status.id} пользователем id {request.user.id}'
        }
        return Response(data, status=200)


class CommentStatusMixin:
    comment_status_model = None
    object_name = None

    def news_status(self, request, comment_status):
        obj = self.get_object()
        author = request.user
        kwargs = {
            self.object_name: obj,
            'author': author,
            'comment_status': comment_status
        }
        try:
            new_comment_status = self.comment_status_model(**kwargs)
            new_comment_status.save()
        except IntegrityError:
            this_comment_status = self.comment_status.objects.filter(**kwargs).first()
            this_comment_status.delete()
        data = {
            "massage": f'Comment_Status успешно присвоен id = {comment_status.id} пользователем id {request.user.id}'
        }
        return Response(data, status=200)