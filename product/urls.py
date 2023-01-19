from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductListView.as_view()),
]
#################################################
#                This is legacy                 #
#################################################
# urlpatterns = [
#     path("/<int:pk>", views.ProductDetailView.as_view()),
#     path("", views.ProductListView.as_view()),
#     # path("/test", views.ProductTestView.as_view()),

# ]