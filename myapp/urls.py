from django.conf.urls import url

from django.conf.urls import url
from django.urls import path,re_path
from django.views.static import serve
from Jtmyd import settings
from . import views
#from myapp import models
urlpatterns = [
	#url(r'^$',views.index,name='index'),
	url(r'^$',views.user.as_view(),name='user'),
	url(r'^register/$',views.register,name='register'),
	url(r'^forgetpassword/$',views.forgetpassword,name="forgetpassword"),
	url(r'^code/$',views.code,name="code"),
	url(r'^index/$', views.index, name='index'),
	url(r'^logout/$',views.quit,name="logout"),
	url(r'^upfile/$',views.upfile,name="upfile"),
	url(r'^New_folder/$',views.New_folder,name="New_folder"),
	url(r'^Delete/$',views.Delete,name="Delete"),
	url(r'^rename/$',views.rename,name="rename"),
	url(r'^rename1/$',views.rename1,name="renname1"),
	re_path(r'upfile/(?P<path>.*)$',serve,{'document_root':settings.MDEIA_ROOT}),
]