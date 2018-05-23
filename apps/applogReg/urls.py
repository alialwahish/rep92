from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^main$',views.main),
    url(r'^login$',views.login),
    url(r'^register$',views.register),
    url(r'^quotes$',views.quotes),
    url(r'logout$',views.logout),
    url(r'^add_quote$',views.add_quote),
    url(r'^add_fav/(?P<id>\d+)/$',views.add_fav),
    url(r'^view_user/(?P<id>\d+)$',views.view_user),
    url(r'^remove_fav_quote/(?P<id>\d+)/$',views.remove_fav_quote),
]
