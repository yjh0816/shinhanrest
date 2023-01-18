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
    def delete(self, request, pk, *args, **kwargs):
        if Product.objects.filter(pk=pk).exists():
            product = Product.objects.get(pk=pk)
            product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    def get(self, request, pk, *args, **kwargs):
        # 1. get 하기 전에 existx()로 확인하고 가져오기
        # 2. get 할 때 예외처리 하기
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        ret = {
            "name": product.name,
            "price": product.price,
            "product_type": product.product_type,
        }
        return Response(ret, status=status.HTTP_200_OK)