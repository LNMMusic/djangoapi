from rest_framework.decorators import api_view
from rest_framework.response import Response


# services
# READ
@api_view(["GET"])
def get():
    pass

@api_view(["GET"])
def get_id():
    pass


# WRITE
@api_view(["POST"])
def create():
    pass

@api_view(["PUT"])
def update():
    pass

@api_view(["DELETE"])
def delete():
    pass