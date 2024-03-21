from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from digestapi.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        categories = Category().objects.all()
        serialized = CategorySerializer(categories, many=True)
        return Response(serialized.data)
    
    def retrieve(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            serialized = CategorySerializer(category, many=False)
            return Response(serialized.data)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
