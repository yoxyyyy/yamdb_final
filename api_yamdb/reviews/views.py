from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from reviews.models import Comments, Review, Title
from users.permissions import IsSuperUserIsAdminIsModeratorIsAuthor

from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSuperUserIsAdminIsModeratorIsAuthor
    )

    def get_title(self):
        return get_object_or_404(Title, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        return Review.objects.filter(title=title_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSuperUserIsAdminIsModeratorIsAuthor
    )

    def get_review(self):
        return get_object_or_404(Review, id=self.kwargs.get('review_id'))

    def get_queryset(self):
        review_id = self.kwargs.get("review_id")
        return Comments.objects.filter(review=review_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())
