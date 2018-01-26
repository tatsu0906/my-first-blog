from django.conf.urls import url
from . import views

urlpatterns = [

    #Main_Site
    url(r'^MainSite$', views.render_MainSite_index, name='MainSite_index'),
    url(r'^MainSite/7$', views.render_MainSite_7, name='MainSite_7'),
    url(r'^MainSite/matrix$', views.render_MainSite_matrix, name='MainSite_matrix'),
    url(r'^MainSite/title$', views.render_MainSite_title, name='MainSite_title'),
    url(r'^MainSite/24$', views.render_MainSite_24, name='MainSite_24'),
    url(r'^MainSite/17$', views.render_MainSite_17, name='MainSite_17'),
    url(r'^MainSite/coreterm$', views.render_MainSite_coreterm, name='MainSite_coreterm'),
    url(r'^MainSite/suppleterm$', views.render_MainSite_suppleterm, name='MainSite_suppleterm'),
    url(r'^MainSite/board$', views.render_MainSite_board, name='MainSite_board'),

    url(r'^MainSite/2020matrix$', views.render_MainSite_2020, name='MainSite_2020'),

    #SnG
    url(r'^SnG$', views.render_SnG_index, name='SnG_index'),
    url(r'^SnG/7$', views.render_SnG_7, name='SnG_7'),
    url(r'^SnG/matrix$', views.render_SnG_matrix, name='SnG_matrix'),
    url(r'^SnG/title$', views.render_SnG_title, name='SnG_title'),
    url(r'^SnG/24$', views.render_SnG_24, name='SnG_24'),
    url(r'^SnG/17$', views.render_SnG_17, name='SnG_17'),
    url(r'^SnG/coreterm$', views.render_SnG_coreterm, name='SnG_coreterm'),
    url(r'^SnG/suppleterm$', views.render_SnG_suppleterm, name='SnG_suppleterm'),
    url(r'^SnG/board$', views.render_SnG_board, name='SnG_board'),

    url(r'^SnG/introduction$', views.render_SnG_introduction, name='SnG_introduction'),
    url(r'^SnG/purpose$', views.render_SnG_purpose, name='SnG_purpose'),

    #Yerim
    url(r'^Yerim$', views.render_Yerim_index, name='Yerim_index'),
    url(r'^Yerim/7$', views.render_Yerim_7, name='Yerim_7'),
    url(r'^Yerim/matrix$', views.render_Yerim_matrix, name='Yerim_matrix'),
    url(r'^Yerim/title$', views.render_Yerim_title, name='Yerim_title'),
    url(r'^Yerim/24$', views.render_Yerim_24, name='Yerim_24'),
    url(r'^Yerim/17$', views.render_Yerim_17, name='Yerim_17'),
    url(r'^Yerim/coreterm$', views.render_Yerim_coreterm, name='Yerim_coreterm'),
    url(r'^Yerim/suppleterm$', views.render_Yerim_suppleterm, name='Yerim_suppleterm'),
    url(r'^Yerim/board$', views.render_Yerim_board, name='Yerim_board'),

    url(r'^Yerim/introduction$', views.render_Yerim_introduction, name='Yerim_introduction'),
    url(r'^Yerim/purpose$', views.render_Yerim_purpose, name='Yerim_purpose'),

    #Other Site
    url(r'^modPage$', views.render_modPage, name='modPage'),

]