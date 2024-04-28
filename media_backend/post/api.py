from django.shortcuts import render
from django.http import JsonResponse
from post.models import Post
from rest_framework.decorators import api_view
from post.serializers import PostSerializer
# Create your views here.


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()

    serializer = PostSerializer(posts, many = True)

    return JsonResponse({'data' : serializer.data})