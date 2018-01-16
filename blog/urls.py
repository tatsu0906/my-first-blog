from django.conf.urls import url
from . import views

urlpatterns = [
	#front page
    url(r'^$', views.render_index, name='index'),
    url(r'^7$', views.render_7, name='7'),
    url(r'^matrix$', views.render_matrix, name='matrix'),
    url(r'^title$', views.render_title, name='title'),
	url(r'^24$', views.render_24, name='24'),
	url(r'^17$', views.render_17, name='17'),
	url(r'^coreterm$', views.render_coreterm, name='coreterm'),
	url(r'^suppleterm$', views.render_suppleterm, name='suppleterm'),
	url(r'^board$', views.render_board, name='board'),



    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]