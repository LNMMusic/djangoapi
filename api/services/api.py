from rest_framework.decorators import api_view
from rest_framework.response import Response


# services
@api_view(['GET'])
def API(request):
    data = {
        'status': 200,
        'message': "here goes all endpoints"
    }
    return Response(data)