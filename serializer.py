from products.models import catogery

from rest_framework import serializers
class CatogerySerializer(serializers.ModelSerializer):
    class Meta:
        model =catogery
        fields = '__all__'