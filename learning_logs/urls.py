"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # topic page
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # new topic page
    path('new_topic/', views.new_topic, name='new_topic'),
    #  Page for adding a new entry
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # edit entry page
    path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]

