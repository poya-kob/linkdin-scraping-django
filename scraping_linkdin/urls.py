"""scraping_linkdin URL Configuration

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
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse

from scrape.views import ApiRequestLinkedin, LinkedinUsersList, LinkedinUsersDetail
from account.views import LoginUsersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApiRequestLinkedin.as_view()),
    path('users-list/', login_required(LinkedinUsersList.as_view(), login_url='/auth/'),
         name='users_list'),
    path('users-list/<int:pk>', login_required(LinkedinUsersDetail.as_view(), login_url='/auth/'),
         name="users_detail"),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', LoginUsersView.as_view(), name='login_page')

]
