"""cakes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from cakeapi import views as api_views
from rest_framework.routers import DefaultRouter 
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("api/cakes",api_views.CakesView,basename="cakes")
router.register("api/v1/cakes",api_views.CakesViewsetView,basename="cakes")
router.register("api/register",api_views.UsersView,basename="users")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("cakes/add/",views.CakesCreativeView.as_view(),name="cakes-add"),
    path("cakes/all/",views.CakesListView.as_view(),name="cakes-list"),
    path("cakes/<int:pk>",views.CakesDetailView.as_view(),name="cakes-detail"),
    path("cakes/<int:pk>/change",views.CakesEditView.as_view(),name="cakes-edit"),
    path("register/",views.SignUpView.as_view(),name="register"),
    path("cakes/<int:pk>/remove",views.CakesDeleteView.as_view(),name="cakes-delete"),
    path("login/",views.SigninView.as_view(),name="signin"),
    path("logout/",views.signout_view,name="signout"),
    path("api/token/",ObtainAuthToken.as_view())




]+router.urls  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
