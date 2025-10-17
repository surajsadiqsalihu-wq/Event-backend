from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions

from Events.models import Event
from Events.serializers import EventSerializer


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated]) 
def api_home(request, *args, **kwargs):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        event = serializer.save(user=request.user)
        return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

