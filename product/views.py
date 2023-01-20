from rest_framework import (
    generics, 
    mixins, 
    status,
)
from .models import Product, Comment, Like
from .serializers import (
    ProductSerializer, 
    CommentSerializer, 
    CommentCreateSerializer,
    LikeSerializer,
    LikeCreateSerializer,
)
from .paginations import ProductLargePagination
from rest_framework.response import Response

class ProductListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = ProductSerializer
    pagination_class = ProductLargePagination

    def get_queryset(self):
        products = Product.objects.all()

        if 'name' in self.request.query_params:
            name = self.request.query_params['name']
            products = products.filter(name__contains=name)
        if 'price' in self.request.query_params:
            price = self.request.query_params['price']
            products = products.filter(price__lte=price)   

        return products.order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class ProductDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)

class CommentListView(
    mixins.ListModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        if product_id:
            return Comment.objects.filter(product_id=product_id).order_by('-id')
        return Comment.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class CommentCreateView(
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all().order_by('id')

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class LikeListView(
    mixins.ListModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class LikeCreateView(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    serializer_class = LikeCreateSerializer

    def get_queryset(self):
        return Like.objects.all().order_by('id')

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        if Like.objects.filter(member=request.user, product_id=product_id).exists():
            Like.objects.filter(member=request.user, product_id=product_id).delete()
            return Response(status.HTTP_204_NO_CONTENT)

        return self.create(request, args, kwargs)