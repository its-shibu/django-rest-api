from django.shortcuts import render
from rest_framework import generics, permissions
from . models import *
from . serializer import *

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

class VoteSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']
        

        
