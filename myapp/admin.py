from django.contrib import admin
from .models import T_User,T_File
# Register your models here.
@ admin.register(T_User)
class T_User(admin.ModelAdmin):
	list_display = ["name","username","password","email","login_stop","login_errnum","capacity","Usedspace","Residual_capacity","lastTime","createTime"]
	list_display_links = ['username']
	list_filter = ['username']
	search_fields = ['username']
	list_per_page = 10
	fields = ['username','name','email',"capacity","login_stop"]
@ admin.register(T_File)
class T_File(admin.ModelAdmin):
	list_display = ["File","username","is_del","File_Available","File_size"]
	list_display_links = ['File']
	list_filter = ['File']
	search_fields = ['File']
	list_per_page = 10
	fields = ['is_del','File_Available']