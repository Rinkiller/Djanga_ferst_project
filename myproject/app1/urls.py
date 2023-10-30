from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coin/', views.coin, name='about'),
    path('get-coin/', views.get_all_coin, name='about'),
    path('get-user-prod/<int:user_id>/<int:days>', views.get_user_products, name='get_user_products'),
    path('upload/', views.upload_image, name='upload_image'),
]


