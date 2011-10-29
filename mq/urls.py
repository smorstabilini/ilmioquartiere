# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('kc_users.views',

    # include api urls
    url(r"^api/", include("kc_users.api.urls")),

    # callback called by fb server after user inserts fb username and pwd
    url(r"^fb_user_auth/$", "fb_user_auth", name="fb_user_auth"),

    # callback called by fb server after user inserts fb username and pwd. this is just for development
    url(r"^fb_friend_list/(?P<how_many>\d+)/$", "fb_friend_list", name="fb_friend_list"),

    # view called when a fb user insert kc username and password:
    url(r"^associate_accounts/$", "wrapper_associate_accounts", name="associate_accounts"),


# OAuth
urlpatterns += patterns('piston.authentication',
    url(r'^oauth/request_token/$', 'oauth_request_token', name='oauth_request_token'),
    url(r'^oauth/authenticate/$', 'oauth_user_auth', name='oauth_user_auth'),
    url(r'^oauth/access_token/$', 'oauth_access_token', name='oauth_access_token'),
)
