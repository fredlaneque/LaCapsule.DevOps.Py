"""
URL configuration for mybackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from webservice import routes

urlpatterns = [
    path('admin', admin.site.urls),
    path('test', routes.first_route),
    path('message', routes.message),
    path('square/<int:number>/', routes.calc_square),
    path('concat/<str:str1>/<str:str2>/', routes.concat),
    path('json_route', routes.json_route),
    path('fill', routes.fill),
    path('upload', routes.upload_route),
    path('json_adv', routes.process_advanced_json)
]
