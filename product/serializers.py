from rest_framework import serializers
from product.models import Banner

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'imageUrl', 'path', 'description')