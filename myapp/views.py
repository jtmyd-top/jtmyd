import os
from django.db.models import Q
from django.http import HttpResponseRedirect, response
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.conf import settings


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

            user2 = T_User.objects.get(username=username)
            Usedspace = decimal.Decimal(user2.Usedspace).quantize(decimal.Decimal("0.000"))
            capacity = decimal.Decimal(user2.capacity).quantize(decimal.Decimal("0.000"))
            width = (Usedspace / capacity * 100)
            a1 = decimal.Decimal(width).quantize(decimal.Decimal("0.000"))
            user1 = T_User.objects.filter(username=username)
            request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
            return render(request, 'index.html',{"username": username, "use": user1, "width": a1, "file_is_folder": fileisfolder,
                           "folder": folder, "folder2": folder2})#,"folder3":folder3
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
                ext = file.name.split('.')[-1].lower()
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
                       use = T_User.objects.get(username=username)
                       use.Usedspace = round((decimal.Decimal(use.Usedspace) - decimal.Decimal(Size)), 3)
                       use.Residual_capacity = use.capacity - use.Usedspace
                       use.save()
                       file1_1=T_File.objects.get(File=checkbox_1,myfile="文件夹",file_is_folder=fileisfolder)
                       file1_1.File_Available=False
                       file1_1.is_del=True
                       file1_1.save()
                for checkbox_2 in checkbox2:
                    if fileisfolder == None or fileisfolder == "":
                        fileisfolder = str(username)
                    else:
                        fileisfolder = request.session.get("fileisfolder")
                    request.session["fileisfolder"] = fileisfolder
                    checkbox_2=checkbox_2[0:-2]
                    file2=T_File.objects.filter(File=checkbox_2,file_is_folder=fileisfolder)
                    if file2:
                        use = T_User.objects.get(username=username)
                        file2=T_File.objects.get(File=checkbox_2)
                        use.Usedspace = round((decimal.Decimal(use.Usedspace)-decimal.Decimal(file2.File_size)),3)
                        use.save()
                        file2.File_Available = False
                        file2.is_del = True
                        file2.save()
                request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/' + "?folder=" + fileisfolder)
                return HttpResponseRedirect(request.session['login_from'])
    else:
        return redirect(reverse("myapp:index"))
def rename(request):
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
            if file_name in checkbox1 and file_point in checkbox1:
                checkbox2=request.POST.get('checkbox1')[:-2]
                ext = checkbox1.split('.')[-1].lower()[:-2]
                t_file=T_File.objects.filter(File=checkbox2,myfile=ext,file_is_folder=fileisfolder,is_del=False,File_Available=True)
                if t_file:
                    if folder_name1 == None or folder_name1 == "":
                        print(folder_name1)
                        if fileisfolder == None or fileisfolder == "":
                            fileisfolder = str(username)
                        else:
                            fileisfolder = request.session.get("fileisfolder")
                        request.session["fileisfolder"] = fileisfolder
                        request.session['login_from'] = request.META.get('HTTP_REFERER','/index/' + "?folder=" + fileisfolder)
                        request.session['msg'] = "请输入新文件夹名称"
                        return HttpResponseRedirect(request.session['login_from'])
                    elif file_point in folder_name1:
                        filepath = BASE_DIR.joinpath(settings.MDEIA_ROOT)
                        path = str(filepath) + "\\" + str(fileisfolder)+"\\"+str(checkbox1)
                        path1=str(filepath) + "\\" + str(fileisfolder)
                        path2= str(filepath) + "\\" + str(fileisfolder)+"\\"+str(folder_name1)
                        if folder_name1 in os.listdir(path1):
                            request.session['msg'] = "当前路径已存在新创建的文件夹名称，请重新命名"
                            return HttpResponseRedirect(request.session['login_from'])
                        else:
                            os.chdir(path1)
                            os.rename(path[:-2],path2)
                            ext1 = folder_name1.split('.')[-1].lower()
                            t_file1=T_File.objects.get(File=checkbox2)
                            t_file1.File = folder_name1
                            t_file1.myfile = ext1
                            print(t_file1)
                            t_file1.save()

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
                t_file = T_File.objects.filter(File=checkbox1, myfile="文件夹", file_is_folder=fileisfolder, is_del=False,File_Available=True)
                if t_file:
                    print(2,checkbox1)
            return HttpResponseRedirect(request.session['login_from'])
        else:
            return redirect(reverse("myapp:user"))

    else:
        return HttpResponseRedirect(request.session['login_from'])

