from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def hello(request):
    """Health-check endpoint to confirm the API is alive."""
    return Response({"message": "Hello from undangan-nikah-ghulam-backend!"})
