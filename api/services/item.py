from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from ..models.response import NewResponse
from ..models import item


# services
# READ
@api_view(["GET"])
def get(request):
    # request
    # ...

    # process
    items = item.Item.objects.all()
    items_response = item.ItemSerializer(items, many=True)

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to get all items!",
        data=items_response.data
    ).parse())

@api_view(["GET"])
def get_id(request, id): #parsed from url
    # request
    # ...

    # process
    items = item.Item.objects.get(id=id)
    items_response = item.ItemSerializer(items, many=False)

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to get item!",
        data=items_response.data
    ).parse())


# WRITE
@api_view(["POST"])
def create(request):
    # request
    req = item.ItemSerializer(data=request.data)    # item schema to later work with database

    # process
    if req.is_valid():      # due to its intagrated to the model db it can call methods directly to execute db transaction
        req.save()

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to create item!",
        data=req.data
    ).parse())

@api_view(["PUT"])
def update(request, id):
    # request
    # ...

    # process
    items = item.Item.objects.get(id=id)
    req = item.ItemSerializer(instance=items, data=request.data) # update data of found item and execute the update db transaction

    if req.is_valid():
        req.save()

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to update item!",
        data=req.data
    ).parse())

@api_view(["DELETE"])
def delete(request, id):
    # request
    # ...

    # process
    items = item.Item.objects.get(id=id)
    items.delete()

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to delete item!",
        data=None
    ).parse())