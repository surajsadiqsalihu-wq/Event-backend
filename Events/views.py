from django.contrib.auth.models import User
from rest_framework import generics, permissions
from django.utils.timezone import now

from .models import Event
from .serializers import EventSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  


class EventListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]   

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]


class EventUpdateAPIView(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly]


class EventDestroyAPIView(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly]


class PublicEventListView(generics.ListAPIView):
    queryset = Event.objects.filter(date_and_time__gte=now()).order_by("date_and_time")
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]