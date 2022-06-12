from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from ..models.response import NewResponse
from ..models import user


# services
# READ
@api_view(["GET"])
def get(request):
    # request
    # ...

    # process
    users = user.User.objects.all()
    users_response = user.UserSerializer(users, many=True)

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to get all users!",
        data=users_response.data
    ).parse())

@api_view(["GET"])
def get_id(request, id): #parsed from url
    # request
    # ...

    # process
    users = user.User.objects.get(id=id)
    users_response = user.UserSerializer(users, many=False)

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to get user!",
        data=users_response.data
    ).parse())


# WRITE
@api_view(["POST"])
def create(request):
    # request
    req = user.UserSerializer(data=request.data)    # user schema to later work with database

    # process
    if req.is_valid():      # due to its intagrated to the model db it can call methods directly to execute db transaction
        req.save()

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to create user!",
        data=req.data
    ).parse())

@api_view(["PUT"])
def update(request, id):
    # request
    # ...

    # process
    users = user.User.objects.get(id=id)
    req = user.UserSerializer(instance=users, data=request.data) # update data of found user and execute the update db transaction

    if req.is_valid():
        req.save()

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to update user!",
        data=req.data
    ).parse())

@api_view(["DELETE"])
def delete(request, id):
    # request
    # ...

    # process
    users = user.User.objects.get(id=id)
    users.delete()

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to delete user!",
        data=None
    ).parse())