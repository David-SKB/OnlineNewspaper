"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.http import HttpResponse

from newspaper.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    ## main page
    url( r'^$' , index , name = 'index' ),
    ## login page
    url( r'^login/$' , login , name = 'login' ) ,
    ## login page
    url( r'^logout/$' , logout , name = 'logout' ) ,
    ## create page
    url( r'^createUser/$' , createUser , name = 'createUser' ) ,
    # detailed article page
    url(r'^(?P<articleID>[0-9]+)/$' , detail , name = 'detail' ) ,
    ## get likes for an article
    url( r'^getLikes/([0-9]+)/$' , getLikes , name = 'getLikes' ) ,
    ## post a comment
    url( r'^postComment/$' , postComment , name = 'postComment' ) ,
    ## like an article
    url( r'^likeArticle/$' , likeArticle , name = 'LikeArticle' ) ,
    ## sports page redirect
    url( r'^sportRedirect/$' , sportRedirect , name = 'sportRedirect' ) ,
    ## update details
    url( r'^updateDetails/$' , updateDetails , name = 'updateDetails' ) ,
    ## login page redirect
    url( r'^loginRedirect/$' , loginRedirect , name = 'loginRedirect' ) ,
    ## dislike an article
    url( r'^dislikeArticle/$' , dislikeArticle , name = 'dislikeArticle' ) ,
    ## get comments
    url( r'^getComments/([0-9]+)/$' , getComments , name = 'getComments' ) ,
    ## get username
    url( r'^getUsername/([0-9]+)/$' , getUsername , name = 'getUsername' ) ,
    ## updateRedirect
    url( r'^updateRedirect/$' , updateRedirect , name = 'updateRedirect' ) ,
    ## logout redirect
    url( r'^logoutRedirect/$' , logoutRedirect , name = 'logoutRedirect' ) ,
    ## delete a comment
    url( r'^deleteComment/([0-9]+)/$' , deleteComment , name = 'deleteComment' ) ,
    ## politics page redirect
    url( r'^politicsRedirect/$' , politicsRedirect , name = 'politicsRedirect' ) ,
    ## register page redirect
    url( r'^registerRedirect/$' , registerRedirect , name = 'registerRedirect' ) ,
    ## lifestyle page redirect
    url( r'^lifestyleRedirect/$' , lifestyleRedirect , name = 'lifestyleRedirect' ) ,
    ## Ajax: check if user exists on registration page
    url(r'^checkIfUniqueLogin/$' , checkIfUniqueLogin , name = 'checkIfUniqueLogin' ) ,
    ## tech. page redirect
    url( r'^technologyRedirect/$' , technologyRedirect , name = 'technologyRedirect' ) ,
    ## return username of whoever is logged in
    url( r'^getLoggedINUsername/$' , getLoggedINUsername , name = 'getLoggedINUsername' ) ,
    ## business + finance page redirect
    url( r'^businessfinanceRedirect/$' , businessfinanceRedirect , name = 'businessfinanceRedirect' ) ,
    ## Ajax: check if user's email is registered
    url(r'^checkIfEmailIsRegistered/$' , checkIfEmailIsRegistered , name = 'checkIfEmailIsRegistered' )
]
