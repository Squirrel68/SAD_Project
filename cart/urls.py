from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("add/<int:book_id>/", views.add_to_cart, name="add_to_cart"),
    path("update/<int:book_id>/", views.update_cart, name="update_cart"),
    path("remove/<int:book_id>/", views.remove_from_cart, name="remove_from_cart"),
]
