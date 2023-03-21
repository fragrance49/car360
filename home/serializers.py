from home.models import Blog
from rest_framework.serializers import ModelSerializer


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'