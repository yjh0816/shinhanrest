from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class ProductListView(APIView):

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