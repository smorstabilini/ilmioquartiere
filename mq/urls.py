# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('mq.views',

    # include api urls
    #url(r"^api/", include("kc_users.api.urls")),

    # callback called by fb server after user inserts fb username and pwd
    url(r"^richieste/$", "richieste", name="richieste"),

)

