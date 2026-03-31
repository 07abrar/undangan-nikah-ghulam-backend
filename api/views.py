from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Couple, Event
from .serializers import CoupleSerializer, EventSerializer


@api_view(["GET"])
def hello(request):
    """Health-check endpoint to confirm the API is alive."""
    return Response({"message": "Hello from undangan-nikah-ghulam-backend!"})

@api_view(["GET"])
def couple(request):
    try:
        instance = Couple.objects.first()
        if instance is None:
            return Response({"error": "Couple not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CoupleSerializer(instance)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["GET"])
def event(request):
    try:
        instance = Event.objects.first()
        if instance is None:
            return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(instance)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)