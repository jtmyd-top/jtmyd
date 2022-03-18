from django.db import models
# Create your models here.

import decimal
class T_User(models.Model):
	username = models.CharField(verbose_name="用户名", max_length=8, primary_key=True)
	password = models.CharField(verbose_name="密码", max_length=512)
	email    = models.EmailField(verbose_name='安全邮箱',max_length=50)
	login_stop = models.BooleanField(verbose_name="账号是否正常",default=True)
	capacity  = models.DecimalField(verbose_name="存储总容量(G)",default=10.000,max_digits=5,decimal_places=3)
	Usedspace = models.DecimalField(verbose_name="已用容量(G)", default=0, max_digits=5, decimal_places=3)
	Residual_capacity = models.DecimalField(verbose_name="剩余容量(G)", default=10, max_digits=5, decimal_places=3)
	lastTime = models.DateTimeField(verbose_name="最晚修改用户信息的日期时间",auto_now=True)  # 凡是对对象进行操作(创建/添加/修改/更新),时间都会随之改变
	createTime = models.DateTimeField(verbose_name="最早创建用户信息的日期时间",auto_now_add=True)
	name  = models.CharField(verbose_name="昵称",max_length=8,blank=True)
	login_errnum = models.IntegerField(verbose_name="用户密码输错次数",default=0)
	objects = models.Manager()
	class Meta:
			verbose_name = "用户"
			verbose_name_plural = "用户表"
			db_table="用户信息"
	def __str__(self):
		return str(self.username)

	def save(self, *args, **kwargs):
		self.Residual_capacity=decimal.Decimal(self.capacity)-decimal.Decimal(self.Usedspace)
		super().save(*args, **kwargs)  # 执行真正的 .save() 方法.实现数据库内容动态修改

class T_File(models.Model):
	"""
	文件信息
	"""
	username = models.ForeignKey(T_User, verbose_name="用户名", on_delete=models.CASCADE)
	File =models.CharField(verbose_name="文件名", max_length=800)
	myfile = models.FileField(verbose_name="文件类型",upload_to='upload',)
	file_is_folder=models.CharField(verbose_name="文件所在的目录", max_length=8000)
	is_del=models.BooleanField(verbose_name="是否删除", default=False)
	Upload_date = models.DateTimeField(verbose_name="上传日期日期", auto_now_add=True)
	createTime = models.DateTimeField(verbose_name="删除日期",null=True,blank=True)
	is_del= models.BooleanField(verbose_name="是否删除", default=False)
	File_Available=	models.BooleanField(verbose_name="文件是否可用", default=True)
	File_size=models.CharField(verbose_name="文件大小", max_length=800)
	objects = models.Manager()
	class Meta:
		verbose_name = "用户"
		verbose_name_plural = "文件表"
		db_table="文件信息"
	def __str__(self):
		return str(self.username)