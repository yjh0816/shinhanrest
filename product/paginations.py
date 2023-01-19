from rest_framework import pagination

class ProductLargePagination(pagination.PageNumberPagination):
    page_size = 100000