from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import PostSerializer
from blog.models import Post


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

