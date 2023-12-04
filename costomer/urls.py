from django.urls import path
from .views import *
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('product_det/<int:id>',ProductDetailsView.as_view(),name='prodet'),
    path('addtocart/<int:id>',AddtoCartView.as_view(),name='acart'),
    path('cartlist',CartListView.as_view(),name="cartlist"),
    path('removecart/<int:id>',DeleteCartItemView.as_view(),name='recart'),
    path('cout/<int:id>',CheckOutView.as_view(),name='cout'),
    path('orders',OrderListView.as_view(),name="olist"),
    path('corder/<int:id>',cancelorder,name="corder"),
    path('review/<int:id>',addreview,name='areview')
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)