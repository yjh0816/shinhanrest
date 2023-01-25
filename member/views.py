from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import (
    generics, 
    mixins, 
    status,
)
from .models import Member
from .serializers import (
    MemberSerializer,
)

class MemberRegisterView(
    APIView
    # mixins.ListModelMixin, 
    # mixins.CreateModelMixin, 
    # generics.GenericAPIView,
):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        tel = request.data.get('tel')

        if Member.objects.filter(username=username).exists():
            return Response({
                'detail': 'Already used'
            }, status=status.HTTP_400_BAD_REQUEST)

        member = Member(
            username = username,
            password = make_password(password),
            tel = tel,
        )
        member.save()
        return Response(status=status.HTTP_201_CREATED)
    # serializer_class = MemberSerializer

    # def get_queryset(self):
    #     members = Member.objects.all()  
    #     return members.order_by('id')

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, args, kwargs)

    # def post(self, request, *args, **kwargs):
    #     if not Member.objects.filter(username=request.data.get('username')).exists():
    #         return self.create(request, args, kwargs)
    #     return Response(status.HTTP_400_BAD_REQUEST)

