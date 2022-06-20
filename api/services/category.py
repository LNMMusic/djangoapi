from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from ..models.response import NewResponse
from ..models import category


# services
# READ
@api_view(["GET"])
def get(request):
    # request
    # ...

    # process
    categories = category.Category.objects.all()
    categories_response = category.CategorySerializer(categories, many=True)

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to get all categories!",
        data=categories_response.data
    ).parse())

@api_view(["GET"])
def get_id(request, id): #parsed from url
    # request
    # ...

    # process
    categories = category.Category.objects.get(id=id)
    categories_response = category.CategorySerializer(categories, many=False)

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to get category!",
        data=categories_response.data
    ).parse())


# WRITE
@api_view(["POST"])
def create(request):
    # request
    req = category.CategorySerializer(data=request.data)    # category schema to later work with database

    # process
    if req.is_valid():      # due to its intagrated to the model db it can call methods directly to execute db transaction
        req.save()

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to create category!",
        data=req.data
    ).parse())

@api_view(["PUT"])
def update(request, id):
    # request
    # ...

    # process
    categories = category.Category.objects.get(id=id)
    req = category.CategorySerializer(instance=categories, data=request.data) # update data of found category and execute the update db transaction

    if req.is_valid():
        req.save()

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to update category!",
        data=req.data
    ).parse())

@api_view(["DELETE"])
def delete(request, id):
    # request
    # ...

    # process
    categories = category.Category.objects.get(id=id)
    categories.delete()

    # response
    return Response(NewResponse(
        statusOk=True,
        message="Succeed to delete category!",
        data=None
    ).parse())