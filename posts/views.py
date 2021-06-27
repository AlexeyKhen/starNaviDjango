from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from posts.models import Post, Likes
from posts.serializers import PostSerializer, LikesSerializer, LikesStatisitcsSerializer


class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        many = True if isinstance(request.data, list) else False
        serializer = self.get_serializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def like_post(request):
    serialized = LikesSerializer(data=request.data, many=False)
    if serialized.is_valid():
        post_id = serialized.validated_data['post']
        post = Post.objects.filter(id=post_id).first()
        if post:
            like = Likes.objects.filter(post=post, liked_by=request.user).first()
            if not like:
                new_like = Likes(post=post, liked_by=request.user)
                new_like.save()
                return Response({'message': 'Post was Liked'}, status=status.HTTP_200_OK)
            else:
                like.delete()
                return Response({'message': 'The post was Unliked'},
                                status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No such post'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Not Valid UUID'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def bulk_post_like(request):
    serialized = LikesSerializer(data=request.data, many=True)
    posts_to_create = []
    if serialized.is_valid():
        post_ids_list = [item['post'] for item in serialized.validated_data]
        post_list = Post.objects.filter(id__in=post_ids_list)
        for item in post_list:
            like = Likes.objects.filter(post=item, liked_by=request.user).first()
            if not like:
                posts_to_create.append(Likes(post=item, liked_by=request.user))
        likes_created = Likes.objects.bulk_create(posts_to_create)
        post_liked_list = [item.id for item in likes_created]
        return Response({'message': f"Posts with ids {post_liked_list} were liked"}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Not Valid UUID'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_like_statistics(request):
    serialized = LikesStatisitcsSerializer(data=request.GET)
    if serialized.is_valid():
        date_from = serialized.validated_data['date_from']
        date_to = serialized.validated_data['date_to']
        likes = Likes.objects.filter(like_date__range=[date_from, date_to]).values('like_date').annotate(
            number_of_likes=Count('id')).order_by('like_date')
        data = {item['like_date'].strftime("%Y-%m-%d"): item['number_of_likes'] for item in likes}
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Not Valid UUID'}, status=status.HTTP_400_BAD_REQUEST)
