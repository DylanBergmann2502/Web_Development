from rest_framework import serializers

from core.models import Post
import json

class PostSerializer(serializers.Serializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_comments(self, post):
        return json.loads(post.comments) # connvert to json