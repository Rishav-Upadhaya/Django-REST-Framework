from django.urls import reverse
from rest_framework import serializers
from .models import Product
from . import validators
from api.serializers import *

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk',
        read_only = True
    )
    title = serializers.CharField(read_only = True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source = 'user', read_only = True)
    # related_products = ProductInlineSerializer(source = 'user.product_set.all', read_only = True, many = True)
    # url = UserProductInlineSerializer(source = 'user',read_only = True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    # edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'owner',
            'pk',
            'url',
            # 'edit_url',
            'title',
            'body',
            'price',
            'sale_price',
            # 'my_discount',
            'public',
            'path',
            'endpoint',
            # 'related_products',
        ]    
        # my_discount is not a field in the model, but we can still access it using the serializer method field as below the value from the model(get_discount) is returned.
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
    
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }
    
    def get_edit_url(self, obj):
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}) 


