from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer




class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']  # поля для поиска


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    pagination_class = PageNumberPagination

    # Добавляем фильтрацию по продукту
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products']  # фильтр по id продукт

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # количество элементов на странице
    page_size_query_param = 'page_size'  # параметр для изменения размера страницы
    max_page_size = 100  # максимальное количество на странице