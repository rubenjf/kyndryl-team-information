
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import EventUpdateView

urlpatterns = [
    
    path('index/',views.index, name='index'),
    path('',auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('address/',views.address, name='address'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('update/<int:id>',views.update, name='update'),
    path('profile_list/',views.profile_list, name='profile_list'),
    path('getPofile/<int:id>',views.getProfile, name='getProfile'),
    path('download_detail/<int:pk>', views.download_detail, name='download_detail'),
    path('download_doc/<int:pk>', views.download_doc, name='download_doc'),
    path('download_img/<int:pk>', views.download_img, name='download_img'),
   
   
  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
