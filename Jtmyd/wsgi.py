"""
WSGI config for Jtmyd project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application






from django.core.wsgi import get_wsgi_application
sys.path.append('D:/OneDrive - cvxbdf88/XXR/pythone/Jtmyd/')
# 加入本项目的虚拟环境(当两个django项目使用不同版本时，这可能非常有用)
virtualenv_dir = 'E:\python\Lib\site-packages'  # 虚拟环境python包文件夹
sys.path.insert(0, virtualenv_dir)  # 加入导包路径from django.core.wsgi import get_wsgi_application
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["DJANGO_SETTINGS_MODULE"] = "Jtmyd.settings"


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jtmyd.settings')

application = get_wsgi_application()
