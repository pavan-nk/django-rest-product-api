from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    """
    Product API:
    - Auth required
    - Each user sees only their own products
    - Supports search by name
    """

    # REQUIRED for DRF router
    queryset = Product.objects.all()

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    # SEARCH SUPPORT
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        # Return only products belonging to the logged-in user
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Attach logged-in user automatically
        serializer.save(user=self.request.user)
