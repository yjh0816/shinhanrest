from rest_framework import serializers
from .models import Product, Comment, Like

class ProductSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    
    def get_comment_count(self, obj):
        return obj.comment_set.all().count()

    def get_like_count(self, obj):
        return obj.like_set.all().count()

    class Meta:
        model = Product
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )
    
    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required.')
        return value

    class Meta:
        model = Comment
        fields = '__all__'
        # extra_kwargs = {'member': {'required': False}}

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class LikeCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )
    
    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required.')
        return value

    class Meta:
        model = Like
        fields = '__all__'