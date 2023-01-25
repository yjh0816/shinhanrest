from rest_framework.response import Response
from rest_framework import (
    generics, 
    mixins, 
    status,
)
from .models import Member
from .serializers import (
    MemberSerializer,
)
# from rest_framework.views import APIView

# class MemberRegisterView(
#     APIView,
# )
    # def post(self, request, *args, **kwargs):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #     tel = request.data.get('tel')

    #     if Member.objects.filter(username=username).exists():
    #         return Response({
    #             'detail': 'Already used'
    #         }, status=status.HTTP_400_BAD_REQUEST)

    #     member = Member(
    #         username = username,
    #         password = make_password(password),
    #         tel = tel,
    #     )
    #     member.save()
    #     return Response(status=status.HTTP_201_CREATED)

class MemberRegisterView(
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
