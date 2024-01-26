from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title_no_hello, unique_product_title


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only=True) # error with this
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')

    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    email = serializers.CharField(source='user.email', read_only=True)

    body = serializers.CharField(source='content')

    class Meta:
        model = Product
        fields = ['owner',
                  'url',
                  'edit_url',
                  'email',
                  'pk',
                  'title',
                  'body', 'price', 'sale_price','public',
                  'path','endpoint',
        ]

    def get_edit_url(self, obj):
        # return f'/api/products/{obj.id}/'
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)