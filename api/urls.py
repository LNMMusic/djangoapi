from django.urls import path
from . import services


# Routes [URL - Service]
urlpatterns = [
    # Root
    path('', services.root.root, name="root"),

    # Api
    path('routes', services.api.API, name="api"),

    # Models    [user]
    path('user/get', services.user.get, name="user_get"),
    path('user/get/<str:id>', services.user.get_id, name="user_get_id"),
    path('user/create', services.user.create, name="user_create"),
    path('user/update/<str:id>', services.user.update, name="user_update"),
    path('user/delete/<str:id>', services.user.delete, name="user_delete"),

    #           [item]
    path('item/get', services.item.get, name="item_get"),
    path('item/get/<str:id>', services.item.get_id, name="item_get_id"),
    path('item/create', services.item.create, name="item_create"),
    path('item/update/<str:id>', services.item.update, name="item_update"),
    path('item/delete/<str:id>', services.item.delete, name="item_delete"),

    #           [category]
    path('category/get', services.category.get, name="category_get"),
    path('category/get/<str:id>', services.category.get_id, name="category_get_id"),
    path('category/create', services.category.create, name="category_create"),
    path('category/update/<str:id>', services.category.update, name="category_update"),
    path('category/delete/<str:id>', services.category.delete, name="category_delete"),
]