from django.urls import path
from . import services


# Routes [URL - Service]
urlpatterns = [
    # Root
    path('', services.root.root, name="root"),

    # Api
    path('routes', services.api.API, name="api"),

    # Models [user]
    path('user/get', services.user.get, name="user_get"),
    path('user/get/<str:id>', services.user.get_id, name="user_get_id"),
    path('user/create', services.user.create, name="user_create"),
    path('user/update/<str:id>', services.user.update, name="user_update"),
    path('user/delete/<str:id>', services.user.delete, name="user_delete"),
]