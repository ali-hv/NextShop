from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/v1/dj-rest-auth/registration/",
         include("dj_rest_auth.registration.urls")),
    path("api/v1/users/", include("accounts.urls")),
    path("api/v1/products/", include("products.urls")),
    path("api/v1/cart/", include("cart.urls")),
]
