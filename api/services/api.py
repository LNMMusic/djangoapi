from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models.response import NewResponse


# services
@api_view(['GET'])
def API(request):
    return Response(NewResponse(
        statusOk=True,
        message="Here goes all api endpoints!",
        data=None
    ).parse())