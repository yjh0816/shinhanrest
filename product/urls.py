from django.urls import path
from . import views

urlpatterns = [
    path("/<int:product_id>/comment", views.ProductCommentListView.as_view()),
    path("/<int:pk>", views.ProductDetailView.as_view()),
    path("/comment", views.ProductCommentListView.as_view()),
    path("", views.ProductListView.as_view()),
]