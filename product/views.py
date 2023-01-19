from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from .paginations import ProductLargePagination

class ProductListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = ProductSerializer
    pagination_class = ProductLargePagination

    def get_queryset(self):
        products = Product.objects.all()
        
        # name = self.request.query_params['name']
        # price = self.request.query_params['price']

        # if name:
        #     products = products.filter(name__contains=name)
        # if price:
        #     products = products.filter(price__lte=price)

        ## This code is more safety

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

#################################################
#                This is legacy                 #
#################################################
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Product
# class ProductListView(APIView):
#     def post(self, request, *args, **kwargs):
#         product = Product(
#             name = request.data.get('name'),
#             price = request.data.get('price'),
#             product_type = request.data.get('product_type'),
#         )
#         product.save()
#         return Response({
#             "id": product.id,
#             "name": product.name,
#             "price": product.price,
#             "product_type": product.product_type,
#         },status=status.HTTP_201_CREATED)

#     def get(self, request, *args, **kwargs):
#         ret = []
#         products = Product.objects.all() 
   
#         if 'price' in request.query_params:
#             price = request.query_params['price']
#             products = products.filter(price__lte=price)
#         if 'name' in request.query_params:
#             name = request.query_params['name']
#             products = products.filter(name__contains=name)
#         '''
#         - gte: greater than and equal
#         - gt: greater then
#         - lte: less than and equl
#         - lt: less than
#         - name: ‘’
#         - name__contains: ‘’
#         '''
#         products = products.order_by('id')

#         for product in products:
#             temp = {
#                 "id": product.id,
#                 "name": product.name,
#                 "price": product.price,
#                 "product_type": product.product_type,
#             }
#             ret.append(temp)
        
#         return Response(ret)

# class ProductDetailView(APIView):   
#     def put(self, request, pk, *args, **kwargs):
#         product = Product.objects.get(pk=pk)

#         dirty = False
#         for field, value in request.data.items():
#             if field not in [f.name for f in product._meta.get_fields()]:
#                 continue

#             dirty = dirty or (value != getattr(product, field))
#             setattr(product, field, value) # object, name of field var, value

#         if dirty:
#             product.save() # save is high cost, so use dirty

#         return Response(status=status.HTTP_200_OK)

#     def delete(self, request, pk, *args, **kwargs):
#         if Product.objects.filter(pk=pk).exists():
#             product = Product.objects.get(pk=pk)
#             product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
#     def get(self, request, pk, *args, **kwargs):
#         try:
#             product = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         ret = {
#             "name": product.name,
#             "price": product.price,
#             "product_type": product.product_type,
#         }
#         return Response(ret, status=status.HTTP_200_OK)