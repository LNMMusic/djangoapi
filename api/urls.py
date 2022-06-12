from django.urls import path
import services



# Routes [URL - Service]
urlpatters = [
    # Root
    path('', services.root.root, name="root"),

    # Api
    path('/routes', services.api.API, name="api"),

    # Models
    path('/user', name="user_get"),
    path('/user/<str:id>', name="user_get_id"),
    path('/user/create', name="user_create"),
    path('/user/update/<str:id>', name="user_update"),
    path('/user/delete/<str:id>', name="user_delete"),
]