"""Reggae CDMX URL Configuration."""

from django.conf import settings
from django.conf.urls import include, url

from reggae_cdmx import views


urlpatterns = [
    # Events
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^events/$', views.EventListView.as_view(), name='event_list'),
    url(r'^events/new$', views.EventCreateView.as_view(), name='create'),
    url(r'^events/(?P<pk>[0-9]+)/edit$', views.EventUpdateView.as_view(), name='update'),
    url(r'^events/(?P<pk>[0-9]+)/delete$', views.EventDeleteView.as_view(), name='delete'),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventDetailView.as_view(), name='detail'),
    # Venues
    url(r'^venues/$', views.VenueListView.as_view(), name='venue_list'),
    url(r'^venues/new$', views.VenueCreateView.as_view(), name='venue_create'),
    url(r'^venues/(?P<pk>[0-9]+)/edit$', views.VenueUpdateView.as_view(), name='venue_update'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
