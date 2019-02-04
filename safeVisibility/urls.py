"""safeVisibility URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url

from visibility import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    

    url(r'^classe/$', views.classe_list, name='classe_list'),
    url(r'^classe/new/$', views.new_classe, name='new_classe'),
    url(r'^classe/show/(?P<id>\d+)/$', views.show_classe, name='show_classe'),

    url(r'^etablissement/$', views.etablissement_list, name='etablissement_list'),
    url(r'^etablissement/new/$', views.new_etablissement, name='new_etablissement'),
    url(r'^etablissement/show/(?P<id>\d+)/$', views.show_etablissement, name='show_etablissement'),
    url(r'^etablissement/search/$', views.search_etablissement, name='search_etablissement'),
    url(r'^etablissement/page/1/$', views.page_etablissement, name='page_etablissement'),
    url(r'^etablissements/page/2/$', views.page_etablissements, name='page_etablissements'),
    
    url(r'^connexion/$', views.page_connexion, name='page_connexion'),
    url(r'^accueil/$', views.page_accueil, name='page_accueil'),
    url(r'^login/$', views.page_login, name='page_login')

]
