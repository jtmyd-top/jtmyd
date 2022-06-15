var userlen = document.getElementById("id_username");
    var userlen1 = $('#id_username').val().length
    userlen.onfocus=function(){
    userlen.style.border="1px solid yellow";
    $('#p1').html("")
}
    userlen.onblur=function(){
            var userlen1 = $('#id_username').val().length
            if(userlen1 < 4 || userlen1>12){
                    userlen.style.border="1px solid red";
                    $('#p1').html("请输入4-12字符的用户名");
                    document.getElementById("p1").style.color="red";
                    succes_1=false;
            }else{
              var csrf = $('input[name="csrfmiddlewaretoken"]').val();
             $.ajax({

            // 1.指定朝哪个后端发送ajax请求
            url:CheckAgain_url, //不写就是朝当前地址提交【与form表单的action参数相同】
            // 2.请求方式
            type:'post',  // 不指定默认就是get，都是小写
            // 3.数据
            data:{'user':$('#id_username').val(),'email':"","csrfmiddlewaretoken": csrf},
            // 4.回调函数:当后端给你返回结果的时候会自动触发，args接受后端的返回结果
            success:function (args) {
                if(args.succes==true){
                    userlen.style.border="1px solid #333";
                    $('#p1').html(args.msg);
                    succes_1=true;
                    document.getElementById("p1").style.color="rgb(14 98 251)"
                }else if(args.succes==false){
                    userlen.style.border="1px solid #333";
                    succes_1=false;
                    $('#p1').html(args.msg);
                    document.getElementById("p1").style.color="red"
                }
            }
            })
}
    }
    var email=document.getElementById("id_email");
    var email2=document.getElementById("id_from-select");
    email.onfocus=function(){
    email.style.border="1px solid yellow";
    $('#p2').html("")
}
    email.onblur=function(){
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
            if($('#id_email').val().length != 0){
             $.ajax({

            // 1.指定朝哪个后端发送ajax请求
            url:email_CheckAgain_url, //不写就是朝当前地址提交【与form表单的action参数相同】
            // 2.请求方式
            type:'post',  // 不指定默认就是get，都是小写
            // 3.数据
            data:{'user':"",'email':$('#id_email').val(),'email2':$('#id_from-select').val(),"csrfmiddlewaretoken": csrf},
            // 4.回调函数:当后端给你返回结果的时候会自动触发，args接受后端的返回结果
            success:function (args) {
                if(args.succes==true){
                    succes_2=true;
                    email.style.border="1px solid #333";
                    $('#p2').html(args.msg);
                    document.getElementById("p2").style.color="rgb(14 98 251)"
                }else if(args.succes == false){

                    email.style.border="1px solid #333";
                    succes_2=false;
                    $('#p2').html(args.msg);
                    document.getElementById("p2").style.color="red"
                }
            }
            })
    }else{
                    succes_2=false;
                    email.style.border="1px solid red";
                    $('#p2').html("请输入邮箱前缀");
                    document.getElementById("p2").style.color="red";
    }
    }
     email2.onblur=function(){
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
            if($('#id_email').val().length != 0){
             $.ajax({

            // 1.指定朝哪个后端发送ajax请求
            url:email_CheckAgain_url, //不写就是朝当前地址提交【与form表单的action参数相同】
            // 2.请求方式
            type:'post',  // 不指定默认就是get，都是小写
            // 3.数据
            data:{'user':"",'email':$('#id_email').val(),'email2':$('#id_from-select').val(),"csrfmiddlewaretoken": csrf},
            // 4.回调函数:当后端给你返回结果的时候会自动触发，args接受后端的返回结果
            success:function (args) {
                if(args.succes==true){
                    succes_2=true;
                    email.style.border="1px solid #333";
                    $('#p2').html(args.msg);
                    document.getElementById("p2").style.color="rgb(14 98 251)"
                }else if(args.succes == false){
                    succes_2=false;
                    email.style.border="1px solid #333";
                    $('#p2').html(args.msg);
                    document.getElementById("p2").style.color="red"
                }
            }
            })
    }else{
                    succes_2=false;
                    email.style.border="1px solid red";
                    $('#p2').html("请输入邮箱前缀");
                    document.getElementById("p2").style.color="red";
    }
    }
    var pwd = document.getElementById("id_password");
    var pwd2 = document.getElementById("id_password2");
    pwd.onfocus=function(){
    pwd.style.border="1px solid yellow";
    $('#p3').html("")
}
    pwd2.onfocus=function(){
    pwd2.style.border="1px solid yellow";
    $('#p4').html("")
}
    pwd.onblur=function(){

            var pwd3 = $('#id_password').val().length
            if(pwd3 < 6 || pwd3 > 18){
                    succes_3=false;
                    document.getElementById("id_password").style.border="1px solid red";
                    $('#p3').html("请输入6-18字符的密码");
                    document.getElementById("p3").style.color="red";
            }else{
                    succes_3=true;
                    document.getElementById("id_password").style.border="1px solid #333";
                    $('#p3').html("新密码符合规则");
                    document.getElementById("p3").style.color="rgb(14 98 251)";

}
    }
pwd2.onblur=function(){

            var pwd4 = $('#id_password2').val().length
            if(pwd4 < 6 || pwd4 > 18){
                    succes_4=false;
                    document.getElementById("id_password").style.border="1px solid red";
                    $('#p4').html("请重新输入6-18字符的密码");
                    document.getElementById("p4").style.color="red";
            }else{
            if($('#id_password').val() == $('#id_password2').val()){
                    succes_4=true;
                    document.getElementById("id_password").style.border="1px solid #333";
                    document.getElementById("id_password2").style.border="1px solid #333";
                    $('#p4').html("两次密码一致");
                    document.getElementById("p4").style.color="rgb(14 98 251)";
            }else{
                    succes_4=false;
                    document.getElementById("id_password").style.border="1px solid #333";
                    document.getElementById("id_password2").style.border="1px solid red";
                    $('#p4').html("两次密码不一致");
                    document.getElementById("p4").style.color="red";
}
    }
}
    var code = document.getElementById("id_code");
    code.onfocus=function(){
    code.style.border="1px solid yellow";
    $('#p5').html("")
}
    code.onblur=function(){
        if($('#id_code').val().length != 0){
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({

            // 1.指定朝哪个后端发送ajax请求
            url:code_CheckAgain_url, //不写就是朝当前地址提交【与form表单的action参数相同】
            // 2.请求方式
            type:'post',  // 不指定默认就是get，都是小写
            // 3.数据
            data:{'code':$('#id_code').val(),"csrfmiddlewaretoken": csrf},
            // 4.回调函数:当后端给你返回结果的时候会自动触发，args接受后端的返回结果
            success:function (args) {
                if(args.succes==true){
                    succes_5=true;
                    code.style.border="1px solid #333";
                    $('#p5').html(args.msg);
                    document.getElementById("p5").style.color="rgb(14 98 251)"

                }else if(args.succes == false){
                    succes_5=true;

                    code.style.border="1px solid red";
                    $('#p5').html(args.msg);
                    document.getElementById("p5").style.color="red"

                }
            }
            })
            }else{
                    succes_5=false;
                    email.style.border="1px solid red";
                    $('#p5').html("请输入验证码");
                    document.getElementById("p5").style.color="red";

            }
    }

    $('#Next').click(function(){
        if(succes_1 == true && succes_2 == true && succes_3 == true && succes_4 == true && succes_5 == true){
            console.log(succes_1);
            alter("恭喜注册成功");
        }else{
              console.log(succes_1);
              alert("请按提示规则正确输入各项表单");
              return false;


       }
    })
function changeImg(ths) {
            ths.src = ths.src + '?';
            console.log(ths.src);
        }
function display() {
                    var traget=document.getElementById('list2');
                    var down=document.getElementById("fa-angle-down");
                    var hidden=document.getElementById("hidden");
                    //var width = {% widthratio use.Usedspace use.capacity 1%};
                        if(traget.style.display=="none") {
                            traget.style.display = 'block';
                            down.style.display = 'none';
                            hidden.style.display = 'inline';
                            document.getElementById("skills").style.width="{{width}}%";
                            //document.getElementById("container").innerHTML="";
                        }else{
                              traget.style.display = 'none';
                              hidden.style.display = 'none';
                              down.style.display = 'inline';
                              }
                        }
function display_0() {
                    var traget=document.getElementById('list_0');
                    var down=document.getElementById("fa-angle-down_0");
                    var hidden=document.getElementById("hidden_0");
                    //var width = {% widthratio use.Usedspace use.capacity 1%};
                        if(traget.style.display=="none") {
                            traget.style.display = 'block';
                            down.style.display = 'none';
                            hidden.style.display = 'inline';

                            //document.getElementById("container").innerHTML="";
                        }else{
                              traget.style.display = 'none';
                              hidden.style.display = 'none';
                              down.style.display = 'inline';
                              }
                        }

