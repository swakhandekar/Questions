"""Questions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from l1 import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home),
    url(r'^login/',views.log_in),
    url(r'^signup/',views.sign_up),
    url(r'^logout/',views.log_out),
    url(r'^submit/',views.addques),
    url(r'^leaderboard/',views.leaderboard),
    url(r'^my_questions/',views.my_ques),
    url(r'^view/',views.question),
    url(r'^save/',views.save),
    url(r'^delete/',views.delete),
    url(r'^staff_view',views.staff_view),
    url(r'^upvote/',views.upvote)

]
