import random

import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Comment
from core.serializers import CommentSerializer


# Create your views here.
class PostCommentAPIView(APIView):
    def get(self, _,pk=None):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentAPIView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        comment = serializer.data

        if random.randint(1, 10) <= 9:
            r = requests.post('http://127.0.0.1:8000/api/posts/%d/comments' % comment['post_id'],
                              data={'text': comment['text']})

            if not r.ok:
                pass

        return Response(comment)


    def formatPost(self, post):
        comments = requests.get('http://127.0.0.1:8000/api/posts/%d/comments' % post.id).json()
        return {
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'comments':comments
        }