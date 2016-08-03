from django.conf.urls import include, url
from django.contrib import admin
from app.models import StateCapital, State, City 
from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^delete_state/(?P<pk>\d+)/$', 'app.views.delete_state'),
    url(r'^edit_state/(?P<pk>\d+)/$', 'app.views.edit_state'),
    url(r'^delete_city/(?P<pk>\d+)/$', 'app.views.delete_city'),
    url(r'^edit_city/(?P<pk>\d+)/$', 'app.views.edit_city', name='edit_city'),
    url(r'^create_city/', 'app.views.create_city'),
    url(r'^city_search/', 'app.views.city_search'),
    url(r'^state_detail/(?P<pk>\d+)/$', 'app.views.state_detail'),
    url(r'^state_list/','app.views.state_list'),
    url(r'^city_list/','app.views.city_list'),
    url(r'^city_detail/(?P<pk>\d+)/$', 'app.views.city_detail'),
    url(r'^capital_list','app.views.capital_list'),
    url(r'^capital_detail/(?P<pk>\d+)/$', 'app.views.capital_detail'),
    url(r'^city_search_post/', 'app.views.city_search_post'),
    
    url(r'^admin/', include(admin.site.urls)),
    #old views
    url(r'^list/', 'app.views.list'),
    url(r'^detail_view/(?P<pk>\d+)/$', 'app.views.detail_view'),
    url(r'^state_list_class_view/', views.StateListView.as_view()),

]
