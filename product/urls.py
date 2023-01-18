from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductTempView.as_view()),
]