import os
from django.db.models import Q
from django.http import HttpResponseRedirect, response
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.conf import settings
import json
import datetime
from .forms import UserRegisterForm, UserLoginForm, UserforgetpasswordForm, renzhengForm, ChangePasswordForm, \
    renzhengForm2
from .forms import UserRegisterForm, UserLoginForm, UserforgetpasswordForm, renzhengForm, ChangePasswordForm, \
    renzhengForm2
import os
import decimal
from .models import *
from myapp.static.utils.code import check_code
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from django.views import View
from django.db.models import Q
from Jtmyd.settings import MDEIA_ROOT, BASE_DIR
from os import listdir
from os.path import isfile, join
def code(request):
    """
       生成图片验证码
    """
    img, random_code = check_code()
    request.session["random_code"] = random_code
    from io import BytesIO
    # 实现了在内存中操作bytes
    stream = BytesIO()
    # 将二维码最终转为png格式
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())
def reclaim(request):
    user_from = UserLoginForm(request.POST)
    username = request.session.get("name")
    paswd = request.session.get("pawsd")
    use = T_User.objects.filter(username=username)
    for x in range(len(use)):
        pwd = use[x].password
        logo = check_password(paswd, pwd)
    fileisfolder = request.GET.get("folder")
    if fileisfolder == None or fileisfolder == "":
        fileisfolder = str(username)
    else:
        fileisfolder = str(request.GET.get("folder"))
    request.session["fileisfolder"] = fileisfolder
    if use:
        if logo == True:
            folder = T_File.objects.filter(is_del=True,File_Available=False,username_id=username, myfile="文件夹")
            folder2 = T_File.objects.filter(is_del=True,File_Available=False,username_id=username).exclude(myfile="文件夹")
            if folder or folder2:
                folder3 = 1
            else:
                folder3 = 0
            user2 = T_User.objects.get(username=username)
            Usedspace = decimal.Decimal(user2.Usedspace).quantize(decimal.Decimal("0.000"))
            capacity = decimal.Decimal(user2.capacity).quantize(decimal.Decimal("0.000"))
            width = (Usedspace / capacity * 100)
            a1 = decimal.Decimal(width).quantize(decimal.Decimal("0.000"))
            user1 = T_User.objects.filter(username=username)
            request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
            return render(request, 'reclaim.html',{"username": username, "use": user1, "width": a1, "file_is_folder": fileisfolder,
                           "folder": folder, "folder2": folder2, "folder3": folder3})
        else:
            return render(request, "user.html", {"msg": "数据异常，请先登录", "form": user_from})
    else:
        return render(request, "user.html", {"msg": "数据异常，请重新登录", "form": user_from})
def index(request):
    user_from = UserLoginForm(request.POST)
    username = request.session.get("name")
    paswd = request.session.get("pawsd")
    use = T_User.objects.filter(username=username)
    for x in range(len(use)):
        pwd = use[x].password
        logo = check_password(paswd, pwd)
    fileisfolder = request.GET.get("folder")
    if fileisfolder == None or fileisfolder == "":
        fileisfolder = str(username)
    else:
        fileisfolder = str(request.GET.get("folder"))
    request.session["fileisfolder"] = fileisfolder
    if use:
        if logo == True:
            folder = T_File.objects.filter(username_id=username, myfile="文件夹",is_del=False,File_Available=True)
            folder2 = T_File.objects.filter(username_id=username,is_del=False,File_Available=True ).exclude(myfile="文件夹")
            # for x in range(len(folder)):
            #     if folder[x].file_is_folder == None or folder[x].file_is_folder == "":
            folder_1=T_File.objects.filter(username_id=username, myfile="文件夹",is_del=False,File_Available=True,file_is_folder=request.session["fileisfolder"])
            folder2_2 = T_File.objects.filter(username_id=username, is_del=False, File_Available=True,file_is_folder=request.session["fileisfolder"]).exclude(myfile="文件夹")
            if folder_1 or folder2_2:
                folder3=1
            else:
                folder3 = 0
            user2 = T_User.objects.get(username=username)
            Usedspace = decimal.Decimal(user2.Usedspace).quantize(decimal.Decimal("0.000"))
            capacity = decimal.Decimal(user2.capacity).quantize(decimal.Decimal("0.000"))
            width = (Usedspace / capacity * 100)
            a1 = decimal.Decimal(width).quantize(decimal.Decimal("0.000"))
            user1 = T_User.objects.filter(username=username)
            request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
            return render(request, 'index.html',{"username": username, "use": user1, "width": a1, "file_is_folder": fileisfolder,
                           "folder": folder, "folder2": folder2,"folder3": folder3,})
        else:
            return render(request, "user.html", {"msg": "数据异常，请先登录", "form": user_from})
    else:
        return render(request, "user.html", {"msg": "数据异常，请重新登录", "form": user_from})
def rename1(request):
    user_from = UserLoginForm(request.POST)
    username = request.session.get("name")
    paswd = request.session.get("pawsd")
    use = T_User.objects.filter(username=username)
    for x in range(len(use)):
        pwd = use[x].password
        logo = check_password(paswd, pwd)
    fileisfolder = request.GET.get("folder")
    if fileisfolder == None or fileisfolder == "":
        fileisfolder = str(username)
    else:
        fileisfolder = str(request.GET.get("folder"))
    request.session["fileisfolder"] = fileisfolder
    if use:
        if logo == True:
            folder = T_File.objects.filter(username_id=username, myfile="文件夹", is_del=False, File_Available=True)
            folder2 = T_File.objects.filter(username_id=username, is_del=False, File_Available=True).exclude( myfile="文件夹")
            folder_1 = T_File.objects.filter(username_id=username, myfile="文件夹", is_del=False, File_Available=True,file_is_folder=request.session["fileisfolder"])
            folder2_2 = T_File.objects.filter(username_id=username, is_del=False, File_Available=True,file_is_folder=request.session["fileisfolder"]).exclude(myfile="文件夹")
            if folder_1 or folder2_2:
                folder3 = 1
            else:
                folder3 = 0
            user2 = T_User.objects.get(username=username)
            Usedspace = decimal.Decimal(user2.Usedspace).quantize(decimal.Decimal("0.000"))
            capacity = decimal.Decimal(user2.capacity).quantize(decimal.Decimal("0.000"))
            width = (Usedspace / capacity * 100)
            a1 = decimal.Decimal(width).quantize(decimal.Decimal("0.000"))
            user1 = T_User.objects.filter(username=username)
            request.session['login_from'] = request.META.get('HTTP_REFERER', '/rename1/' + "?folder=" + fileisfolder)
            return render(request, 'renname.html',{"username": username, "use": user1, "width": a1, "file_is_folder": fileisfolder,"folder": folder, "folder2": folder2,"folder3":folder3})
        else:
            return render(request, "user.html", {"msg": "数据异常，请先登录", "form": user_from})
    else:
        return render(request, "user.html", {"msg": "数据异常，请重新登录", "form": user_from})
class user(View):
    """
        CBV（class base views)用户登录
        """

    def get(self, request):
        username = request.session.get("name")
        fileisfolder = request.GET.get("folder")
        if fileisfolder == None or fileisfolder == "":
            fileisfolder = str(username)
        else:
            fileisfolder = request.GET.get("folder")
        user_from = UserLoginForm(request.POST)
        print("GET方法")
        msg = "请退出登陆后再来切换账户，敬请谅解"

        use1 = T_User.objects.filter(username=username)
        print(username)
        paswd = request.session.get("pawsd")
        for x in range(len(use1)):
            pwd = use1[x].password
            logo = check_password(paswd, pwd)
        if use1:
            if logo == True:
                if username == "" or username == None:  # 登录状态不允许切换账号
                    request.session.clear()
                    return render(request, "user.html", {"form": UserLoginForm})
                else:
                    use = T_User.objects.get(username=username)
                    Usedspace = decimal.Decimal(use.Usedspace).quantize(decimal.Decimal("0.000"))
                    capacity = decimal.Decimal(use.capacity).quantize(decimal.Decimal("0.000"))
                    width = (Usedspace / capacity * 100)
                    a1 = decimal.Decimal(width).quantize(decimal.Decimal("0.000"))
                    return redirect(reverse("myapp:index"))
            else:
                return render(request, "user.html", {"form": user_from})
        else:
            return render(request, "user.html", {"form": user_from})

    def post(self, request):
        user_from = UserLoginForm(request.POST)

        # print("POST方法")
        if user_from.is_valid():
            username = user_from.cleaned_data['username']
            password = user_from.cleaned_data['password']
            user_list = T_User.objects.filter(username=username)
            request.session['name'] = username
            request.session['pawsd'] = password
            fileisfolder = request.GET.get("folder")
            if fileisfolder == None or fileisfolder == "":
                fileisfolder = str(username)
            else:
                fileisfolder = request.GET.get("folder")
            request.session["fileisfolder"] = fileisfolder
            if user_list:
                use = T_User.objects.get(username=username)
                logostop = use.login_stop
                pwd = use.password
                logo = check_password(password, pwd)
                if logo:
                    if logostop == True:
                        use.login_errnum = 0
                        use.save()
                        return redirect(reverse("myapp:index"))
                    else:
                        request.session.clear()
                        return render(request, 'user.html',{"form": user_from, 'msg': '账户被锁定,请<a href=../forgetpassword/>重置密码</a>后再来登陆'})
                else:
                    use = T_User.objects.get(username=username)
                    use.login_errnum = use.login_errnum + 1
                    use.save()
                    if use.login_errnum >= 6:
                        use.login_stop = False
                        use.save()
                        # Log.objects.create(user_id=username, action='登陆失败', remarks='账户被锁定')
                        return render(request, 'user.html',
                                      {"form": user_from, 'msg': '账户被锁定，请<a href=../forgetpassword/>重置密码</a>后再来登陆'})
                    else:
                        # Log.objects.create(user_id=username, action='登陆失败', remarks='密码错误')
                        return render(request, 'user.html', {"form": user_from, 'msg': '账户或密码错误'})
            else:
                return render(request, 'user.html', {"form": user_from, 'msg': '账户或密码错误'})
        else:
            return render(request, 'user.html', {"form": user_from, 'msg': '请按规则输入账户或密码'})
def register(request):
    '''
    用户注册
    '''
    register_form = UserRegisterForm(request.POST)
    code1 = request.session.get("random_code")
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            username = register_form.cleaned_data['username']
            request.session['name'] = username
            request.session['pawsd'] = password
            email2 = request.POST.get('email2')
            email3 = email + email2
            password2 = register_form.cleaned_data['password2']
            code = register_form.cleaned_data['code']
            user_list = T_User.objects.filter(Q(username=username) | Q(email=email3))
            fileisfolder = request.GET.get("folder")
            if fileisfolder == None or fileisfolder == "":
                fileisfolder = str(username)
            else:
                fileisfolder = request.GET.get("folder")
            request.session["fileisfolder"] = fileisfolder
            if code.upper() == code1:
                if user_list:
                    request.session.clear()
                    return render(request, 'register.html', {
                        'msg': '用户名或邮箱已被注册', "register_form": register_form})
                if password2 == password:
                    path = BASE_DIR.joinpath(settings.MDEIA_ROOT)
                    print(path)
                    import os
                    def mkdir(path1):
                        os.chdir(path)
                        folder = os.path.exists(path1)
                        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                            os.makedirs(path1)  # makedirs 创建文件时如果路径不存在会创建这个路径
                        else:
                            return render(request, 'register.html', {
                                'msg': '用户名或邮箱已被注册', "register_form": register_form})

                    mkdir(username)
                    T_User.objects.create(username=username, email=email3,
                                          password=make_password(password, '九兲冥月刀-jtmyd'), name=username)
                    return redirect(reverse("myapp:index"))
                else:
                    request.session.clear()
                    return render(request, 'register.html', {
                        'msg': '两次密码不一致', "register_form": register_form}
                                  )
            else:
                request.session.clear()
                return render(request, 'register.html', {
                    'msg': '验证码不正确', "register_form": register_form})
        else:
            return render(request, 'register.html', {
                "register_form": register_form, 'msg': '请按规则输入表单各项',
            })
    else:
        username = request.session.get("name", "游客")
        use = T_User.objects.filter(username=username)
        if use:
            request.session.clear()
            return render(request, 'register.html', {"register_form": register_form})
        else:
            return render(request, "register.html", {"register_form": register_form})
def forgetpassword(request):
    '''
    用户忘记密码
    '''
    user_from = UserLoginForm(request.POST)
    code1 = request.session.get("random_code")
    forgetpassword_form = UserforgetpasswordForm(request.POST)
    if request.method == "POST":
        if forgetpassword_form.is_valid():
            username = forgetpassword_form.cleaned_data['username']
            email = forgetpassword_form.cleaned_data['email']
            password = forgetpassword_form.cleaned_data['password']
            password2 = forgetpassword_form.cleaned_data['password2']
            email2 = request.POST.get("email2")
            email3 = email + email2
            code = forgetpassword_form.cleaned_data['code']
            use = T_User.objects.filter(username=username, email=email3)
            if use:
                if password2 == password:
                    use1 = T_User.objects.get(username=username)
                    pwd = use1.password
                    ter = check_password(password, pwd)
                    # 使用filter固定格式，若使用get如果查询不到用户名则会报错不推荐使用
                    if ter == True:
                        request.session.clear()
                        return render(request, "forgetpassword.html",
                                      {"msg": "新密码与旧密码相同,请重新更换新密码", "forgetpassword_form": forgetpassword_form})
                    elif code.upper() == code1:
                        use1 = T_User.objects.get(username=username)
                        use1.password = make_password(password, '九兲冥月刀-jtmyd')
                        use1.login_errnum = 0
                        use1.save()
                        # Log.objects.create(user_id=username, action='重置密码成功')
                        use1.login_stop = True
                        use1.save()
                        request.session.clear()
                        return render(request, "user.html", {"msg": "重置密码成功", "form": user_from})
                    else:
                        request.session.clear()
                        return render(request, "forgetpassword.html",
                                      {"msg": "请正确的输入验证码", "forgetpassword_form": forgetpassword_form})
                else:
                    # Log.objects.create(user_id=username, action='重置密码失败',remarks='两次新密码不相同')
                    request.session.clear()
                    return render(request, "forgetpassword.html",
                                  {"msg": "两次密码不相同", "forgetpassword_form": forgetpassword_form})
            else:
                request.session.clear()
                return render(request, "forgetpassword.html",
                              {"msg": "用户名或者邮箱有误，请重新输入", "forgetpassword_form": forgetpassword_form})
        else:
            request.session.clear()
            return render(request, "forgetpassword.html",
                          {"msg": "请正确的输入各项数据", "forgetpassword_form": forgetpassword_form})
    else:
        return render(request, "forgetpassword.html", {"forgetpassword_form": forgetpassword_form})
def quit(request):
    '''
    用户退出登陆
    '''
    username = request.session.get("name", "游客")
    use = T_User.objects.filter(username=username)
    user_from = UserLoginForm(request.POST)
    if use:
        request.session.clear()
        username = "游客"
        return render(request, 'user.html', {"form": user_from, "username": username})
    else:
        request.session.clear()
        username = "游客"
        return render(request, "user.html", {"form": user_from, "username": username})
def upfile(request):
    "上传文件"
    username = request.session.get("name")
    if request.method == 'POST':
        fileisfolder = request.session.get("fileisfolder")
        file = request.FILES.get("picpath")
        user1 = T_User.objects.filter(username=username)
        if user1:
            user2 = T_User.objects.get(username=username)
            if file is None or file == "":
                Usedspace = decimal.Decimal(user2.Usedspace).quantize(decimal.Decimal("0.000"))
                capacity = decimal.Decimal(user2.capacity).quantize(decimal.Decimal("0.000"))
                width = (Usedspace / capacity * 100)
                a1 = decimal.Decimal(width).quantize(decimal.Decimal("0.000"))
                user1 = T_User.objects.filter(username=username)
                folder = T_File.objects.filter(username_id=username, myfile="文件夹")
                folder2 = T_File.objects.filter(username_id=username, ).exclude(myfile="文件夹")
                request.session["msg"] = "请选择文件后，再次上传"
                return render(request, 'index.html',{'name': username, "msg": "请选择文件后，再次上传", "use": user1, "width": a1,"file_is_folder": fileisfolder, "folder": folder, "folder2": folder2})
            else:
                ext = file.name.split('.')[-1]
                file_size = round((float(file.size) / 1073741824), 3)
                filepath = BASE_DIR.joinpath(settings.MDEIA_ROOT)
                filepath1 = str(filepath) + "\\" + fileisfolder + "\\" + file.name
                file1=T_File.objects.filter(File=file.name,file_is_folder=fileisfolder)
                if file1:
                    Usedspace = decimal.Decimal(user2.Usedspace).quantize(decimal.Decimal("0.000"))
                    capacity = decimal.Decimal(user2.capacity).quantize(decimal.Decimal("0.000"))
                    width = (Usedspace / capacity * 100)
                    a1 = decimal.Decimal(width).quantize(decimal.Decimal("0.000"))
                    user1 = T_User.objects.filter(username=username)
                    folder = T_File.objects.filter(username_id=username, myfile="文件夹")
                    folder2 = T_File.objects.filter(username_id=username).exclude(myfile="文件夹")
                    request.session["msg"] = "该路径下有相同的文件，请修改文件名后再次上传"
                    return render(request, 'index.html', {'name': username, "msg": "该路径下有相同的文件，请修改文件名后再次上传", "use": user1, "width": a1,"file_is_folder": fileisfolder, "folder": folder, "folder2": folder2})
                else:
                    if user2.Residual_capacity >= file_size:
                        with open(filepath1, "wb") as fp:
                            for info in file.chunks():
                                fp.write(info)
                        T_File.objects.create(file_is_folder=fileisfolder, username_id=username, File=file.name, myfile=ext,File_size=file_size)
                        user2.Usedspace = round((decimal.Decimal(user2.Usedspace) + decimal.Decimal(file_size)), 3)
                        user2.save()
                        request.session['login_from'] = request.META.get('HTTP_REFERER','/index/' + "?folder=" + fileisfolder)
                        return HttpResponseRedirect(request.session['login_from'])
                    else:
                        Usedspace = decimal.Decimal(user2.Usedspace).quantize(decimal.Decimal("0.000"))
                        capacity = decimal.Decimal(user2.capacity).quantize(decimal.Decimal("0.000"))
                        width = (Usedspace / capacity * 100)
                        a1 = decimal.Decimal(width).quantize(decimal.Decimal("0.000"))
                        user1 = T_User.objects.filter(username=username)
                        return render(request, 'index.html',
                                      {'name': username, "msg": "文件上传失败，剩余空间不足已存储该文件", "use": user1, "width": a1,"file_is_folder": fileisfolder})
        else:
            user_from = UserLoginForm(request.POST)
            return render(request, 'user.html', {"msg": "数据异常请重新登陆", "form": user_from})
    else:
        user_from = UserLoginForm(request.POST)
        username = request.session.get("name")
        paswd = request.session.get("pawsd")
        use = T_User.objects.filter(username=username)
        fileisfolder = request.session.get("fileisfolder")
        for x in range(len(use)):
            pwd = use[x].password
            logo = check_password(paswd, pwd)
        if use:
            if logo == True:
                if fileisfolder == None or fileisfolder == "":
                    fileisfolder = str(username)
                else:
                    fileisfolder = request.GET.get("fileisfolder")
                request.session["fileisfolder"] = fileisfolder

                filepath = BASE_DIR.joinpath(settings.MDEIA_ROOT)
                #request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + request.session["fileisfolder"] )
                return HttpResponseRedirect(request.session['login_from'])
            else:
                return render(request, "user.html", {"msg": "数据异常，请先登录", "form": user_from})
        else:
            return render(request, "user.html", {"msg": "数据异常，请重新登录", "form": user_from})
def New_folder(request):
    "新建文件夹"
    username = request.session.get("name")
    fileisfolder = request.session.get("fileisfolder")
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')
        use = T_User.objects.filter(username=username)
        a="."
        if use:
            if folder_name == None or folder_name == "":
                if fileisfolder == None or fileisfolder == "":
                    fileisfolder = str(username)
                else:
                    fileisfolder = request.session.get("fileisfolder")
                request.session["fileisfolder"] = fileisfolder
                request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
                request.session['msg'] = "请输入新文件夹名称"
                return HttpResponseRedirect(request.session['login_from'])

            elif a in folder_name:
                if fileisfolder == None or fileisfolder == "":
                    fileisfolder = str(username)
                else:
                    fileisfolder = request.session.get("fileisfolder")
                request.session["fileisfolder"] = fileisfolder
                request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
                request.session['msg'] = "文件夹名称中不能包含.等特殊字符"
                return HttpResponseRedirect(request.session['login_from'])
            else:
                if fileisfolder == None or fileisfolder == "":
                    fileisfolder = str(username)
                else:
                    fileisfolder = request.session.get("fileisfolder")

                request.session["fileisfolder"] = fileisfolder
                request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
                filepath = BASE_DIR.joinpath(settings.MDEIA_ROOT)
                path = str(filepath) + "\\" + str(fileisfolder)
                if folder_name in os.listdir(path):
                       request.session['msg'] = "当前路径已存在新创建的文件夹名称，请重新命名"
                       return HttpResponseRedirect(request.session['login_from'])
                else:
                       request.session['msg']="创建文件夹成功"
                       os.chdir(path)
                       os.makedirs(folder_name)
                       T_File.objects.create(file_is_folder=fileisfolder, username_id=username, File=folder_name, myfile="文件夹",File_size=0)
                       return HttpResponseRedirect(request.session['login_from'])
        else:
            return redirect(reverse("myapp:user"))
    else:
        #return HttpResponseRedirect(request.session['login_from'])
        return render(request, "index.html")
def Delete(request):
    "删除文件"
    username = request.session.get("name")
    fileisfolder = request.session.get("fileisfolder")
    if request.method == "POST":
        checkbox1=request.POST.getlist('checkbox1')
        checkbox2=request.POST.getlist('checkbox2')
        use= T_User.objects.filter(username=username)
        if use:
            if checkbox1 == None and checkbox2 == None:
                request.session['msg'] = "请选择文件夹或文件"
                if fileisfolder == None or fileisfolder == "":
                    fileisfolder = str(username)
                else:
                    fileisfolder = request.session.get("fileisfolder")
                request.session["fileisfolder"] = fileisfolder
                request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
                return HttpResponseRedirect(request.session['login_from'])
            else:
                if fileisfolder == None or fileisfolder == "":
                    fileisfolder = str(username)
                else:
                    fileisfolder = request.session.get("fileisfolder")
                request.session["fileisfolder"] = fileisfolder
                for checkbox_1 in checkbox1:
                    file1=T_File.objects.filter(File=checkbox_1,myfile="文件夹",file_is_folder=fileisfolder)
                    if file1:
                       filepath = BASE_DIR.joinpath(settings.MDEIA_ROOT)
                       path = str(filepath) + "\\" + str(fileisfolder)+"\\"+ checkbox_1
                       list1 = []
                       def Sizes(path):
                           fileList = os.listdir(path)  # 获取path目录下所有文件
                           for filename in fileList:
                               pathTmp = os.path.join(path, filename)  # 获取path与filename组合后的路径
                               if os.path.isdir(pathTmp):  # 判断是否为目录
                                   Sizes(pathTmp)  # 是目录就继续递归查找
                               elif os.path.isfile(pathTmp):  # 判断是否为文件
                                   filesize = os.path.getsize(pathTmp)  # 如果是文件，则获取相应文件的大小
                                   list1.append(filesize)
                       Sizes(path)
                       Size=float(sum(list1)/1073741824)
                       use = T_User.objects.filter(username=username)
                       for  x in range(len(use)):
                           use[x].Usedspace = round((decimal.Decimal(use[x].Usedspace) - decimal.Decimal(Size)), 3)
                           use[x].Residual_capacity = use[x].capacity - use[x].Usedspace
                           use[x].save()
                       file1_1=T_File.objects.filter(File=checkbox_1,myfile="文件夹",file_is_folder=fileisfolder)
                       for i in range(len(file1_1)):
                           file1_1[i].File_Available=False
                           file1_1[i].is_del=True
                           file1_1[i].createTime =datetime.datetime.now()
                           file1_1[i].save()
                for checkbox_2 in checkbox2:
                    if fileisfolder == None or fileisfolder == "":
                        fileisfolder = str(username)
                    else:
                        fileisfolder = request.session.get("fileisfolder")
                    request.session["fileisfolder"] = fileisfolder
                    checkbox_2=checkbox_2[:-2]
                    file2=T_File.objects.filter(File=checkbox_2,file_is_folder=fileisfolder,username=username)
                    if file2:
                        use = T_User.objects.filter(username=username)
                        for y in range(len(file2)):
                            for x in range(len(use)):
                                    use[x].Usedspace = round((decimal.Decimal(use[x].Usedspace) - decimal.Decimal(file2[y].File_size)),3)
                                    use[x].save()
                            file2[y].File_Available = False
                            file2[y].is_del = True
                            file2[y].createTime = datetime.datetime.now()
                            file2[y].save()
                request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
                return HttpResponseRedirect(request.session['login_from'])
    else:
        return redirect(reverse("myapp:index"))
def rename(request):
    "重命名"
    username = request.session.get("name")
    fileisfolder = request.session.get("fileisfolder")
    if fileisfolder == None or fileisfolder == "":
            fileisfolder = str(username)
    else:
           fileisfolder = request.session.get("fileisfolder")
    request.session["fileisfolder"] = fileisfolder
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
    if request.method == "POST":
        checkbox1 = request.POST.get('checkbox1')
        folder_name1 = request.POST.get('folder_name1')
        file_name="文件"
        file_point="."
        use=T_User.objects.filter(username=username)
        if use:
            if folder_name1 == None or folder_name1 == "":
                if fileisfolder == None or fileisfolder == "":
                    fileisfolder = str(username)
                else:
                    fileisfolder = request.session.get("fileisfolder")
                request.session["fileisfolder"] = fileisfolder
                request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
                request.session['msg'] = "请输入新文件夹名称"
                return HttpResponseRedirect(request.session['login_from'])
            elif checkbox1== None or folder_name1 == "":
                if fileisfolder == None or fileisfolder == "":
                    fileisfolder = str(username)
                else:
                    fileisfolder = request.session.get("fileisfolder")
                request.session["fileisfolder"] = fileisfolder
                request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
                request.session['msg'] = "请选择需要重命名的文件或文件夹"
                return HttpResponseRedirect(request.session['login_from'])
            elif file_name in checkbox1 and file_point in checkbox1:
                checkbox2=request.POST.get('checkbox1')[:-2]
                ext = checkbox1.split('.')[-1][:-2]
                t_file=T_File.objects.filter(File=checkbox2,myfile=ext,file_is_folder=fileisfolder,is_del=False,File_Available=True)
                if t_file:
                    if file_point in folder_name1:
                        filepath = BASE_DIR.joinpath(settings.MDEIA_ROOT)
                        path = str(filepath) + "\\" + str(fileisfolder)+"\\"+str(checkbox1)
                        path1=str(filepath) + "\\" + str(fileisfolder)
                        path2= str(filepath) + "\\" + str(fileisfolder)+"\\"+str(folder_name1)
                        if folder_name1 in os.listdir(path1):
                            request.session['msg'] = "当前路径已存在新创建的文件名称，请重新命名"
                            return HttpResponseRedirect(request.session['login_from'])
                        else:
                            os.chdir(path1)
                            os.rename(path[:-2],path2)
                            ext1 = folder_name1.split('.')[-1]
                            for x in range(len(t_file)):
                                t_file[x].File = folder_name1
                                t_file[x].myfile = ext1
                                t_file[x].save()
                            if fileisfolder == None or fileisfolder == "":
                                fileisfolder = str(username)
                            else:
                                fileisfolder = request.session.get("fileisfolder")
                            request.session["fileisfolder"] = fileisfolder
                            request.session['login_from'] = request.META.get('HTTP_REFERER','/index/' + "?folder=" + fileisfolder)
                            return HttpResponseRedirect(request.session['login_from'])
                    else:
                        request.session['msg'] = "文件名称中需要包含.等特殊字符"
                        if fileisfolder == None or fileisfolder == "":
                            fileisfolder = str(username)
                        else:
                            fileisfolder = request.session.get("fileisfolder")

                        request.session["fileisfolder"] = fileisfolder
                        request.session['login_from'] = request.META.get('HTTP_REFERER','/index/' + "?folder=" + fileisfolder)
                        return HttpResponseRedirect(request.session['login_from'])
                else:
                    request.session['msg'] = "请重新选择文件，再来重命名"
                    if fileisfolder == None or fileisfolder == "":
                        fileisfolder = str(username)
                    else:
                        fileisfolder = request.session.get("fileisfolder")

                    request.session["fileisfolder"] = fileisfolder
                    request.session['login_from'] = request.META.get('HTTP_REFERER','/index/' + "?folder=" + fileisfolder)
                    return HttpResponseRedirect(request.session['login_from'])

            else:
                checkbox2 = request.POST.get('checkbox1')
                file_point = "."
                t_file = T_File.objects.filter(File=checkbox1, myfile="文件夹", file_is_folder=fileisfolder, is_del=False,File_Available=True)
                if t_file:
                    if file_point not in folder_name1:
                        filepath = BASE_DIR.joinpath(settings.MDEIA_ROOT)
                        path = str(filepath) + "\\" + str(fileisfolder) + "\\" + str(checkbox1)
                        path1 = str(filepath) + "\\" + str(fileisfolder)
                        path3 = str(fileisfolder) + "\\" + str(checkbox1)
                        path4 = str(fileisfolder) + "\\" + str(folder_name1)
                        path2 = str(filepath) + "\\" + str(fileisfolder) + "\\" + str(folder_name1)
                        if folder_name1 in os.listdir(path1):
                            request.session['msg'] = "当前路径已存在新创建的文件名称，请重新命名"
                            return HttpResponseRedirect(request.session['login_from'])
                        else:
                            os.chdir(path1)
                            os.rename(path, path2)
                            ext1 = "文件夹"
                            for x in range(len(t_file)):
                                t_file[x].File = folder_name1
                                t_file[x].myfile = ext1
                                t_file[x].save()
                            t_file2 = T_File.objects.filter(file_is_folder=path3)
                            t_file3=T_File.objects.filter(file_is_folder__contains=path3,username=username).exclude(file_is_folder=path3)

                            if t_file3:
                                for x in range(len(t_file3)):
                                    File_Is_Folder_Old=t_file3[x].file_is_folder
                                    File_Is_Folder_Old_2=File_Is_Folder_Old.split(path3)[-1]
                                    File_Is_Folder_Old_3=path4+File_Is_Folder_Old_2
                                    t_file3[x].file_is_folder = File_Is_Folder_Old_3
                                    t_file3[x].save()
                            if t_file2:
                                for x in range(len(t_file2)):
                                    t_file2[x].file_is_folder = path4
                                    t_file2[x].save()
                            if fileisfolder == None or fileisfolder == "":
                                fileisfolder = str(username)
                            else:
                                fileisfolder = request.session.get("fileisfolder")
                            request.session["fileisfolder"] = fileisfolder
                            request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
                            return HttpResponseRedirect(request.session['login_from'])
                    else:
                        if fileisfolder == None or fileisfolder == "":
                            fileisfolder = str(username)
                        else:
                            fileisfolder = request.session.get("fileisfolder")
                        request.session["fileisfolder"] = fileisfolder
                        request.session['login_from'] = request.META.get('HTTP_REFERER','/index/' + "?folder=" + fileisfolder)
                        request.session['msg'] = "文件夹名称中不能包含.等特殊字符"
                        return HttpResponseRedirect(request.session['login_from'])

                else:
                    request.session['msg'] = "请重新选择文件夹，再来重命名"
                    if fileisfolder == None or fileisfolder == "":
                        fileisfolder = str(username)
                    else:
                        fileisfolder = request.session.get("fileisfolder")

                    request.session["fileisfolder"] = fileisfolder
                    request.session['login_from'] = request.META.get('HTTP_REFERER','/index/' + "?folder=" + fileisfolder)
                    return HttpResponseRedirect(request.session['login_from'])
        else:
            return redirect(reverse("myapp:user"))
    else:
        return HttpResponseRedirect(request.session['login_from'])
def num(request):
    if request.method =="POST":
        ts1=request.POST.get("num1")
        ts2=request.POST.get("num2")
        print(ts1,ts2)
        num=int(ts1)+int(ts2)
        return HttpResponse(str(num))
    return redirect(reverse("myapp:index"))
def CheckAgain(request):
    if request.method =="POST":
        user=request.POST.get("user")
        use=T_User.objects.filter(username=user)
        if use:
            res = {"succes": False, "msg": "用户名已被占用，请重新输入"}
        else:
           res = {"succes": True, "msg": "用户名可用"}
        return HttpResponse(json.dumps(res),content_type='application/json')
    else:
        redirect(reverse("myapp:register"))
def email_CheckAgain(request):
        if request.method == "POST":
            email = request.POST.get("email")
            email2 = request.POST.get("email2")
            email3=email+email2
            t_email = T_User.objects.filter(email=email3)
            if t_email:
                res = {"succes": False, "msg": "邮箱已被使用，请重新输入"}
            else:
                res = {"succes": True, "msg": "邮箱可用"}
            return HttpResponse(json.dumps(res), content_type='application/json')
        else:
              redirect(reverse("myapp:register"))
def code_CheckAgain(request):
    code1 = request.session.get("random_code")
    if request.method == "POST":
        code = request.POST.get("code")
        if code.upper() == code1.upper():
            res = {"succes": True, "msg": "验证通过"}
        else:
            res = {"succes": False, "msg": "验证失败"}
        return HttpResponse(json.dumps(res), content_type='application/json')
    else:
        redirect(reverse("myapp:register"))
def  ChangePassword(request):
    '''
    用户修改密码
    '''
    user_from = UserLoginForm(request.POST)
    ChanPasswd =  ChangePasswordForm(request.POST)
    username = request.session.get("name", "游客")
    if request.method == "POST":
        if ChanPasswd.is_valid():
            ypwd= ChanPasswd.cleaned_data['password']
            xpwd = ChanPasswd.cleaned_data['password2']
            xpwd2 = ChanPasswd.cleaned_data['password3']
            use = T_User.objects.filter(username=username)
            for x in range(len(use)):
                time = use[x].lastTime
            if use:
                if xpwd2 == xpwd:
                    for x in range(len(use)):
                        pwd = use[x].password
                        ter = check_password(ypwd, pwd)
                        tar1 = check_password(xpwd, pwd)

                    if ter == True:
                        if tar1 == True:

                            return render(request, "ChangePassword.html",{"msg": "原密码不能跟新密码相同，请更正后重新修改", "ChanPasswd": ChanPasswd})
                        else:
                            # for x in range(len(use)):
                            #     use[x].password = make_password(xpwd, '九兲冥月刀-jtmyd')
                            #     use[x].save()
                            use = T_User.objects.get(username=username)
                            use.password = make_password(xpwd, '九兲冥月刀-jtmyd')
                            use.save()

                            request.session.clear()
                            return render(request,"user.html",{"msg":"密码修改成功，重新登录请使用新密码","form": user_from})
                    else:

                        #request.session.clear()
                        return render(request, "ChangePassword.html",{"msg": "原密码错误，请更正后重新修改或<a href='../forgetpassword'>忘记密码</a>", "ChanPasswd": ChanPasswd,"use":use})
                else:
                    return render(request, "ChangePassword.html", {"msg": "两次新密码不相同，请更正后重新修改", "ChanPasswd": ChanPasswd,"use":use})
            else:
                request.session.clear()
                return render(request, "user.html", {"msg": "账户异常，重新登录后再修改密码", "form": user_from})
        else:
            use = T_User.objects.filter(username=username)
            for x in range(len(use)):
                time = use[x].lastTime
            return render(request, "ChangePassword.html", {"msg": "请按照提示正确无误输入各项数据，请更正后重新修改", "ChanPasswd": ChanPasswd,"use":use})
    else:
        username = request.session.get("name")
        user1 = T_User.objects.filter(username=username)
        if user1:
            return render(request,"ChangePassword.html",{"ChanPasswd": ChanPasswd,"use":user1})
        else:
            return render(request, "user.html", {"form": user_from, "msg": "账户异常，请重新登陆"})
def Recover_Files(request):
    global fileisfolder2
    username = request.session.get("name")
    if request.method == "POST":
        checkbox1 = request.POST.getlist('checkbox1')
        checkbox2 = request.POST.getlist('checkbox2')
        use = T_User.objects.filter(username=username)
        if use:
            if checkbox1 == None and checkbox2 == None:
                request.session['msg'] = "请选择需要恢复的文件夹或文件"
                return redirect(reverse("myappa:reclaim"))
            else:
                for checkbox_1 in checkbox1:
                    file1 = T_File.objects.filter(File=checkbox_1, myfile="文件夹", username=username,is_del=True,File_Available=False)
                    for i in range(len(file1)):
                        fileisfolder2 = file1[i].file_is_folder
                    if file1:
                        filepath = BASE_DIR.joinpath(settings.MDEIA_ROOT)
                        path = str(filepath) + "\\" + str(fileisfolder2) + "\\" + checkbox_1
                        list1 = []
                        def Sizes(path):
                            fileList = os.listdir(path)  # 获取path目录下所有文件
                            for filename in fileList:
                                pathTmp = os.path.join(path, filename)  # 获取path与filename组合后的路径
                                if os.path.isdir(pathTmp):  # 判断是否为目录
                                    Sizes(pathTmp)  # 是目录就继续递归查找
                                elif os.path.isfile(pathTmp):  # 判断是否为文件
                                    filesize = os.path.getsize(pathTmp)  # 如果是文件，则获取相应文件的大小
                                    list1.append(filesize)

                        Sizes(path)
                        Size = float(sum(list1) / 1073741824)
                        use = T_User.objects.filter(username=username)
                        for x in range(len(use)):
                            use[x].Usedspace = round((decimal.Decimal(use[x].Usedspace) + decimal.Decimal(Size)), 3)
                            use[x].Residual_capacity = use[x].capacity + use[x].Usedspace
                            use[x].save()
                        file1_1 = T_File.objects.filter(File=checkbox_1, myfile="文件夹", is_del=True,File_Available=False)
                        for i in range(len(file1_1)):
                            file1_1[i].File_Available = True
                            file1_1[i].is_del = False
                            file1_1[i].createTime = None
                            file1_1[i].save()
                for checkbox_2 in checkbox2:
                    checkbox_2 = checkbox_2[0:-2]
                    file2 = T_File.objects.filter(File=checkbox_2,is_del=True,File_Available=False, username=username)
                    if file2:
                        use = T_User.objects.filter(username=username)
                        for y in range(len(file2)):
                            for x in range(len(use)):
                                use[x].Usedspace = round((decimal.Decimal(use[x].Usedspace) + decimal.Decimal(file2[y].File_size)), 3)
                                use[x].save()
                            file2[y].File_Available = True
                            file2[y].is_del = False
                            file2[y].createTime = None
                            file2[y].save()

                return redirect(reverse("myapp:reclaim"))
    else:
        return redirect(reverse("myapp:index"))
