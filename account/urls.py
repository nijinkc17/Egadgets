from django.urls import path
from .views import *
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('reg',RegView.as_view(),name="signup"),
    path('home',HomeView.as_view(),name="home"),
    path('logout',LgOutView.as_view(),name='logout')
    
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)