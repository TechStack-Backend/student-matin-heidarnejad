from django.urls import path
from . import views

app_name = "developers"

urlpatterns = [
    path("", views.developers_list, name="list"),
    path("<str:username>/", views.developer_cv, name="detail"),
]
