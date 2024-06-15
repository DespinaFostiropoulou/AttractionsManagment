from attractions.models import Attractions
from attractions.serializers import AttractionsSerializer, UserSerializer
from rest_framework import generics, permissions, filters
from django.contrib.auth.models import User
from attractions.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AttractionsList(generics.ListCreateAPIView):
    """
    Returns a list of all Attractions
    """
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('title', 'category', 'country', 'city', 'owner')
    search_fields = ['title', 'category', 'country', 'city']
    ordering_fields = ('title', 'category')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttractionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ('title', 'category', 'country', 'city', 'owner')
    search_fields = ['title', 'category', 'country', 'city']
    ordering_fields = ('title', 'category')