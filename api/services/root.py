from rest_framework.decorators import api_view
from rest_framework.response import Response


# services
@api_view(["GET"])
def root(request):
    data = {
        'status': 200,
        'message': "Welcome to the root of the API"
    }
    return Response(data)