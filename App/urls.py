from django.urls import path
from App import views
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

#Para el manejo de paginas inexistentes
from django.conf.urls import handler404
from App.views import error_404_view

urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('about/',views.about,name="About"),
    path('login/',views.login_request,name="Login"),
    path('registro/',views.registro,name="Registro"),
    path('logout/', LogoutView.as_view(template_name="App/logout.html"), name="Logout"),
    path('addblogpost/', views.addblogpost,name="AddBlogpost"),
    path('updatepost/<post_id>/', views.updatepost, name="UpdatePost"),
    path('deletepost/<post_id>/', views.deletepost, name="DeletePost"),
    path('contact/', views.contact, name="Contact"),
    path('blogpost/', views.blogpost, name="Blogpost"),
    path('searchpost/', views.searchpost, name="SearchPost"),
    path('searchpostsite/', views.searchpostsite, name="SearchPostSite"),
    path('profile/', views.profile, name="Profile"),
    path('updateprofile/', views.updateprofile, name="UpdateProfile"),
    path('editpassword/', views.CambiarClave.as_view(), name="UpdatePass"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)