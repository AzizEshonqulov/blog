"""personal_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from pers_blog.views import loginPage, logoutPage, post, post_detail, home_page, post_new, comment_new, post_update, post_delete, category, registerPage
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post', post, name='post'),
    path('', home_page, name='home_page'),
    path('post/new', post_new, name = 'post_new'),
    path('comment/new', comment_new, name = 'comment_new'),
    path('post/<str:pk>', post_detail, name = 'post_detail'),
    path('post/update/<str:pk>', post_update, name = 'post_update'),
    path('post/delete/<str:pk>', post_delete, name = 'post_delete'),
    path('category/<str:pk>', category, name = 'category'),
    path('register', registerPage, name = 'register'),
    path('login', loginPage, name = 'login'),
    path('logout', logoutPage, name = 'logout'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)