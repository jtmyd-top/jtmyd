from django.conf.urls import url

from django.conf.urls import url
from django.urls import path,re_path
from django.views.static import serve
from Jtmyd import settings
from . import views
urlpatterns = [
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
	url(r'^num/$',views.num,name="num"),
	url(r'^CheckAgain/$',views.CheckAgain,name="CheckAgain"),
	url(r'^email_CheckAgain/$',views.email_CheckAgain,name="email_CheckAgain"),
	url(r'^code_CheckAgain/$',views.code_CheckAgain,name="code_CheckAgain"),
	re_path(r'upfile/(?P<path>.*)$',serve,{'document_root':settings.MDEIA_ROOT}),
	url(r'^ChangePassword/$',views.ChangePassword,name="ChangePassword"),
	url(r'^reclaim/$',views.reclaim,name="reclaim"),
	url(r'^Recover_Files/$',views.Recover_Files,name="Recover_Files"),


]