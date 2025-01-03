#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()), 
    path('booking/', include(router.urls)),
    path('message/', views.msg), 
]

# urlpatterns = [
#     path('', views.index, name='index')
# ]