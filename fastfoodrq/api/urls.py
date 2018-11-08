from django.conf.urls import url, include
from rest_framework import routers
from fastfoodrq.api.views import (
    ProductViewSet,
    CategoryViewSet,
    IngredientViewSet,
    TagViewSet,
)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'ingredient', IngredientViewSet)
router.register(r'tag', TagViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    )
]
