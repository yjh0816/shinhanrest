from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class ProductListView(APIView):
    def post(self, request, *args, **kwargs):
        product = Product(
            name = request.data.get('name'),
            price = request.data.get('price'),
            product_type = request.data.get('product_type'),
        )
        product.save()
        return Response({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "product_type": product.product_type,
        },status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        ret = []

        products = Product.objects.all().order_by('id')

        for product in products:
            temp = {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "product_type": product.product_type,
            }
            ret.append(temp)
        
        return Response(ret)

class ProductDetailView(APIView):

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=request.path_info.split('/')[-1])

        ret = {
            "name": product.name,
            "price": product.price,
            "product_type": product.product_type,
        }
        return Response(ret)