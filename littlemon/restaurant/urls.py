from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu_item'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
