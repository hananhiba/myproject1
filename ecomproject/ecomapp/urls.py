from . import views
from django.urls import path
app_name='ecomapp'

urlpatterns = [
    path('',views.AllProductCategory,name='AllProductCategory'),
    path('<slug:category_slug>/',views.AllProductCategory,name='Products_by_Category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.proDetail, name='proDetail'),

]
