from django.shortcuts import render
from django.shortcuts import HttpResponse
from app import models
from django.db import connection
import re

# Create your views here.

def bottom(request):
    return render(request, "bottom.html")


def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def welcome(request):
    if request.method == 'POST':  # POST过程加密 get相反
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = models.UserInfo.objects.filter(username=username)
        if user.count() != 0:
            info = models.UserInfo.objects.values('password').filter(username=username)[0]
            print("info=", info)
            if info['password'] == password:
                return render(request, "welcome.html")
            else:
                return render(request, 'login.html', {'err': '密码错误请重新输入！'})
        else:
            return render(request, 'login.html', {'err': '用户不存在！'})


# Create your views here.


list = []


def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        list = ['id', 'stuname', 'stuphone', 'stuaddress', 'stucollege', 'stumajor']
        info = []
        for li in list:
            info.append(request.POST.get(li))
        # if globals()['UserId'] != 1:
        #     return HttpResponse("非root用户，没有权限添加用户！")
        # print(info)
        s = models.StuInfo.objects.filter(id=info[0])
        # print(s.count())
        if s.count() != 0:
            return render(request, 'add.html', {'err': '学生信息已存在，请勿重复添加'})
        stu = models.StuInfo()
        stu.id = info[0]
        stu.stuname = info[1]
        stu.stuphone = info[2]
        stu.stuaddress = info[3]
        stu.stucollege = info[4]
        stu.stumajor = info[5]
        stu.save()  # 保存数据
        return render(request, 'add.html', {'success': '学生信息添加成功!!'})


def delete(request):
    if request.method == 'GET':
        return render(request, 'delete.html')
    id = request.POST.get('id', None)
    print(id)
    if id.isspace() == True:
        return render(request, 'delete.html', {'err': '学号不能由空格组成,请重新输入！！！'})
    if len(id) == 0:
        return render(request, 'delete.html', {'err': '学号不能为空,请重新输入！！！'})
    emp = models.StuInfo.objects.filter(id=id)
    print("emp=", emp)
    if emp.count() == 0:
        return render(request, 'delete.html', {'err': '该用户不存在,请重新输入！！！'})
    models.StuInfo.objects.filter(id=id).delete()
    return render(request, 'delete.html', {'success': '删除成功'})


def update(request):
    if request.method == 'GET':
        return render(request, 'update.html')
    list = ['id', 'stuname', 'stuphone', 'stuaddress', 'stucollege', 'stumajor']
    info = []
    for li in list:
        info.append(request.POST.get(li))
    # if globals()['UserId'] != 1:
    #     return render(request, 'update.html', {'err': '权限不够，请切换为 root 用户重试'})
    id = request.POST.get('id', None)
    if id.isspace() == True:
        return render(request, 'update.html', {'err': '学号不能为空格组成,请重新输入！'})
    s = models.StuInfo.objects.filter(id=info[0])
    if s.count() == 0:
        return render(request, 'update.html', {'err': '没有此学生信息，无法修改'})
    stu = models.StuInfo()
    stu.id = info[0]
    stu.stuname = info[1]
    stu.stuphone = info[2]
    stu.stuaddress = info[3]
    stu.stucollege = info[4]
    stu.stumajor = info[5]
    stu.save()
    return render(request, 'update.html', {'success': '学生信息修改成功！'})


def select(request):
    if request.method == 'GET':
        return render(request, 'select.html')
    # if globals()['UserId'] != 1:
    #     return render(request, 'select.html', {'err': '非 root 用户，无法查看！'})
    # 从表单中获取id值
    id = request.POST.get('id', None)
    # 判断id不能为空的字符串类型
    if id.isspace() == True:
        return render(request, 'select.html', {'err': "不能为空值,请重新输入！"})
    # 从数据库根据id值将对应信息赋值给stu
    stu = models.StuInfo.objects.filter(id=id)
    if stu.count() == 0:
        return render(request, 'select.html', {'err': '没有查询到此学生信息，请确定是否录入系统'})
    info = \
    models.StuInfo.objects.values('id', 'stuname', 'stuphone', 'stuaddress', 'stucollege', 'stumajor').filter(id=id)[0]
    print("info=", info)
    return render(request, 'select.html', info)


def info(request):
    if request.method == 'POST':
        return render(request, 'info.html')
    info = models.StuInfo.objects.all()
    # print('info:',info)
    print(info)
    return render(request, 'info.html', {"info": info})
# Create your views here.


def selgrade(request):
    return render(request, "selgrade.html")


def gradeall(request):
    if request.method == 'POST':
        return render(request, "gradeall.html")
    with connection.cursor() as cursor:
        cursor.execute('select app_stuinfo.id, app_stuinfo.stuname, app_course.cno, cname, ccredit, grade, stumajor\
                            from app_sc, app_stuinfo, \
                            app_course where app_sc.scno_id=app_course.cno and \
                            app_stuinfo.id=app_sc.sid_id')
        info = cursor.fetchall()
        mid = []
        for li in info:
            line = {}
            line['id'] = li[0]
            line['stuname'] = li[1]
            line['cno'] = li[2]
            line['cname'] = li[3]
            line['ccredit'] = li[4]
            line['grade'] = li[5]
            line['stumajor'] = li[6]
            mid.append(line)
        # print('info:', info)

    return render(request, 'gradeall.html', {"info": mid})


def gradeone(request):
    if request.method == 'GET':
        return render(request, 'gradeone.html')
    id = request.POST.get('id', None)
    print(id)
    if id.isspace() == True:
        return render(request, 'gradeone.html', {'err': '学号不能由空格组成,请重新输入！！！'})
    if len(id) == 0:
        return render(request, 'gradeone.html', {'err': '学号不能为空,请重新输入！！！'})
    emp = models.StuInfo.objects.filter(id=id)
    print("emp=", emp)
    if emp.count() == 0:
        return render(request, 'gradeone.html', {'err': '该用户不存在,请重新输入！！！'})
    point = 0
    with connection.cursor() as cursor:
        cursor.execute('select stuname, app_course.cno, cname, ccredit, grade, stumajor '
                       ' from app_sc,app_stuinfo,app_course where app_sc.scno_id=app_course.cno and '
                       'app_stuinfo.id=app_sc.sid_id and app_stuinfo.id='+id)
        info = cursor.fetchall()
        mid = []
        sum = 0
        for li in info:
            line = {}
            line['cno'] = li[1]
            line['cname'] = li[2]
            line['ccredit'] = li[3]
            line['grade'] = li[4]
            line['stumajor'] = li[5]
            mid.append(line)
            if li[4] < 60:
                continue
            point += (li[4]-50)*li[3]*0.1
            sum += li[3]
    return render(request, 'gradeone.html', {"info": mid, "name": info[0][0], "stumajor": '专业：'+info[0][5], \
                                             "point": "绩点："+str(round(point/sum, 2))})


def grademajor(request):
    if request.method == 'GET':
        return render(request, 'grademajor.html')
    major = request.POST.get('major', None)
    print(major)
    if major.isspace() == True:
        return render(request, 'grademajor.html', {'err': '专业名不能由空格组成,请重新输入！！！'})
    if len(major) == 0:
        return render(request, 'grademajor.html', {'err': '专业名不能为空,请重新输入！！！'})
    emp = models.StuInfo.objects.filter(stumajor=major)
    if emp.count() == 0:
        return render(request, 'grademajor.html', {'err': '该专业下无学生,请确保专业名称输入正确！！！'})
    with connection.cursor() as cursor:
        sql = "select app_stuinfo.id, stuname, app_course.cno, cname,ccredit, grade from app_sc,app_stuinfo,app_course" \
              " where app_sc.scno_id=app_course.cno and app_stuinfo.id=app_sc.sid_id and stumajor='"\
                       + major +"'"
        cursor.execute(sql)
        info = cursor.fetchall()
        mid = []
        for li in info:
            line = {}
            line['id'] = li[0]
            line['stuname'] = li[1]
            line['cno'] = li[2]
            line['cname'] = li[3]
            line['ccredit'] = li[4]
            line['grade'] = li[5]
            mid.append(line)
    with connection.cursor() as cursor:
        sql = "select app_stuinfo.id, stuname, " \
              "count(*) as 修课门数, sum(case when grade>=60 then 1 else 0 end) as 通过门数,"\
              "Convert(decimal(5,2), sum((case when grade>=60 then grade-50 else 0 end)*ccredit)*1.0/sum(ccredit)*0.1) " \
              "as point " \
              "from app_sc,app_stuinfo,app_course " \
              "where app_sc.scno_id=app_course.cno and app_stuinfo.id=app_sc.sid_id and stumajor='" + major + "'"\
        "group by app_stuinfo.id, stuname order by " \
        "Convert(decimal(5,2), sum((case when grade>=60 then grade-50 else 0 end)*ccredit)*1.0/sum(ccredit)*0.1) desc"
        cursor.execute(sql)
        info = cursor.fetchall()
        point = []
        cot = 1
        for li in info:
            line = {}
            line['id'] = li[0]
            line['stuname'] = li[1]
            line['xcount'] = li[2]
            line['pass'] = li[3]
            line['point'] = li[4]
            line['rank'] = cot
            cot += 1
            point.append(line)
    return render(request, 'grademajor.html', {"info": mid,  "major": major+'专业', "point": point})


def gradecourse(request):
    if request.method == 'GET':
        return render(request, 'gradecourse.html')
    course = request.POST.get('course', None)
    print(course)
    if course.isspace() == True:
        return render(request, 'gradecourse.html', {'err': '课程名不能由空格组成,请重新输入！！！'})
    if len(course) == 0:
        return render(request, 'gradecourse.html', {'err': '课程名不能为空,请重新输入！！！'})
    emp = models.Course.objects.filter(cname=course)
    if emp.count() == 0:
        return render(request, 'gradecourse.html', {'err': '该课程下无学生,请确保课程名称输入正确！！！'})
    with connection.cursor() as cursor:
        sql = "select app_stuinfo.id, stuname, stucollege, stumajor, grade " \
              "from app_sc,app_stuinfo,app_course " \
              "where app_sc.scno_id=app_course.cno and app_stuinfo.id=app_sc.sid_id " \
              "and cname='" + course + "'"\
              "order by stucollege desc, stumajor  desc, grade desc"
        cursor.execute(sql)
        info = cursor.fetchall()
        mid = []
        for li in info:
            line = {}
            line['id'] = li[0]
            line['stuname'] = li[1]
            line['stucollege'] = li[2]
            line['stumajor'] = li[3]
            line['grade'] = li[4]
            mid.append(line)
    return render(request, "gradecourse.html", {"info": mid, "course": course})


def grademid(request):
    course = request.POST.get('course', None)
    return render(request, 'gradecoursemajor.html', {'course': course})


def gradecoursemajor(request):
    if request.method == 'GET':
        return render(request, 'gradecoursemajor.html')
    course = request.POST.get('course', None)
    if request.method == 'GET':
        return render(request, 'gradecoursemajor.html')
    major = request.POST.get('major', None)
    print(major)
    if major.isspace() == True:
        return render(request, 'gradecoursemajor.html', {'err': '专业名不能由空格组成,请重新输入！！！'})
    if len(major) == 0:
        return render(request, 'gradecoursemajor.html', {'err': '专业名不能为空,请重新输入！！！'})
    emp = models.StuInfo.objects.filter(stumajor=major)
    if emp.count() == 0:
        return render(request, 'gradecoursemajor.html', {'err': '该专业下无学生,请确保专业名称是否输入正确！！！'})
    top = request.POST.get('top', None)
    if course == '':
        return render(request, 'gradecourse.html', {'err': '请输入所需要查询的课程！！！'})
    if top == '':
        return render(request, 'gradecoursemajor.html', {'err': '！！！'})
    if major == '':
        return render(request, 'gradecoursemajor.html', {'err': '！！！'})
    print("top=", type(top))
    top = int(top)
    with connection.cursor() as cursor:
        sql = "select top " + str(top) +" app_stuinfo.id, stuname, grade " \
              "from app_sc,app_stuinfo, app_course " \
                  "where app_sc.scno_id=app_course.cno and app_stuinfo.id=app_sc.sid_id " \
              " and cname='" + course + "'"\
                  " and stumajor='" + major + "'"\
                  " order by grade desc"
        print("sql=", sql)
        cursor.execute(sql)
        info = cursor.fetchall()
        top = []
        cot = 1
        for li in info:
            line = {}
            line['id'] = li[0]
            line['stuname'] = li[1]
            line['grade'] = li[2]
            line['cot'] = cot
            cot += 1
            top.append(line)
    return render(request, "gradecoursemajor.html", {"info": top, 'course': course})


def gradefail(request):
    if request.method == 'GET':
        return render(request, 'gradefail.html')
    course = request.POST.get('course', None)
    major = request.POST.get('major', None)
    college = request.POST.get('college', None)
    id = request.POST.get('id', None)
    str = ""
    if course != "":
        str += " and cname="+"'"+course+"'"
        emp = models.Course.objects.filter(cname=course)
        if emp.count() == 0:
            return render(request, 'gradefail.html', {'err': '该课程下无学生,请确保课程名称输入正确！！！'})
    if major != "":
        emp = models.StuInfo.objects.filter(stumajor=major)
        if emp.count() == 0:
            return render(request, 'gradefail.html', {'err': '该专业下无学生,请确保专业名称输入正确！！！'})
        str += " and stumajor="+"'"+major+"'"
    if college != "":
        emp = models.StuInfo.objects.filter(stucollege=college)
        if emp.count() == 0:
            return render(request, 'gradefail.html', {'err': '该学院下无学生,请确保学院名称输入正确！！！'})
        str += " amd stucollege="+"'"+college+"'"
    if id != "":
        emp = models.StuInfo.objects.filter(id=id)
        if emp.count() == 0:
            return render(request, 'gradefail.html', {'err': '不存在该学学号学生,请确保学生学号输入正确！！！'})
        str += " and app_stuinfo.id="+"'"+id+"'"
    with connection.cursor() as cursor:
        sql = "select app_stuinfo.id, stuname,stumajor, stucollege,cname, grade " \
              "from app_sc,app_stuinfo,app_course " \
              "where app_sc.scno_id=app_course.cno " \
              "and app_stuinfo.id=app_sc.sid_id and grade<60 " + str + " order by " \
                                                         "stucollege, stumajor, app_course.cno," \
                                                         "app_stuinfo.id, grade desc"
        print("sql=", sql)
        cursor.execute(sql)
        info = cursor.fetchall()
        mid = []
        for li in info:
            line = {}
            line['id'] = li[0]
            line['stuname'] = li[1]
            line['major'] = li[2]
            line['college'] = li[3]
            line['course'] = li[4]
            line['grade'] = li[5]
            mid.append(line)
    return render(request, "failresult.html", {"info": mid})


def failresult(request):
    return render(request, "failresult.html")


def mid(request):
    return render(request, "gradefail.html")


def printc(request):
    with connection.cursor() as cursor:
        sql = "select * from app_course"
        cursor.execute(sql)
        info = cursor.fetchall()
        mid = []
        for li in info:
            line = {}
            line['cno'] = li[0]
            line['cname'] = li[1]
            if li[2] == None:
                line['cpno'] = ""
            else:
                line['cpno'] = li[2]
            line['ccredit'] = li[3]
            mid.append(line)
    return render(request, "addgrade.html", {"info": mid})


def addgrade(request):
    if request.method == 'GET':
        return render(request, "addgrade.html")
    elif request.method == 'POST':
        with connection.cursor() as cursor:
            sql = "select * from app_course"
            cursor.execute(sql)
            info = cursor.fetchall()
            mid = []
            for li in info:
                line = {}
                line['cno'] = li[0]
                line['cname'] = li[1]
                if li[2] == None:
                    line['cpno'] = ""
                else:
                    line['cpno'] = li[2]
                line['ccredit'] = li[3]
                mid.append(line)
        list = ['sno', 'cno', 'grade']
        info = []
        for li in list:
            info.append(request.POST.get(li))
        flag = models.StuInfo.objects.filter(id=info[0])
        if flag.count() == 0:
            return render(request, 'addgrade.html', {'err': '学生信息不存在，请重新输入！！！', "info": mid})
        flag = models.Course.objects.filter(cno=info[1])
        if flag.count() == 0:
            return render(request, 'addgrade.html', {'err': '课程编号不存在，请重新输入！！！', "info": mid})
        s = models.sc.objects.filter(sid=info[0], scno=info[1])
        if s.count() != 0:
            return render(request, 'addgrade.html', {'err': '学生成绩信息已存在，请勿重复添加！！！', "info": mid})
        sc = models.sc()
        sc.sid = models.StuInfo.objects.filter(id=info[0]).first()
        sc.scno = models.Course.objects.filter(cno=info[1]).first()
        sc.grade = int(info[2])
        sc.save()  # 保存数据
        return render(request, 'addgrade.html', {'success': '学生信息添加成功！！！', "info": mid})


def updategrade(request):
    if request.method == 'GET':
        return render(request, "updategrade.html")
    list = ['sno', 'cno', 'grade']
    info = []
    for li in list:
        info.append(request.POST.get(li))
    flag = models.StuInfo.objects.filter(id=info[0])
    if flag.count() == 0:
        return render(request, 'updategrade.html', {'err': '学生信息不存在，请重新输入！！！'})
    flag = models.Course.objects.filter(cno=info[1])
    if flag.count() == 0:
        return render(request, 'updategrade.html', {'err': '课程编号不存在，请重新输入！！！'})
    s = models.sc.objects.filter(sid=info[0], scno=info[1])
    if s.count() == 0:
        return render(request, 'updategrade.html', {'err': '没有此成绩信息，无法更改！！！'})
    # sid = models.StuInfo.objects.filter(id=info[0]).first()
    # scno = models.Course.objects.filter(cno=info[1]).first()
    # sc.grade = int(info[2])
    # sc.save()  # 保存数据
    data = {'sid': models.StuInfo.objects.filter(id=info[0]).first(),
            'scno': models.Course.objects.filter(cno=info[1]).first(),
            'grade': int(info[2])}
    models.sc.objects.filter(sid=info[0], scno=info[1]).update(**data)
    return render(request, "updategrade.html", {'success': '学生成绩修改成功！！！'})


def deletegrade(request):
    if request.method == 'GET':
        return render(request, "deletegrade.html")
    list = ['sno', 'cno']
    info = []
    for li in list:
        info.append(request.POST.get(li))
    flag = models.StuInfo.objects.filter(id=info[0])
    if flag.count() == 0:
        return render(request, 'deletegrade.html', {'err': '学生信息不存在，请重新输入！！！'})
    flag = models.Course.objects.filter(cno=info[1])
    if flag.count() == 0:
        return render(request, 'deletegrade.html', {'err': '课程编号不存在，请重新输入！！！'})
    s = models.sc.objects.filter(sid=info[0], scno=info[1])
    if s.count() == 0:
        return render(request, 'deletegrade.html', {'err': '没有此成绩信息，无法删除！！！'})
    models.sc.objects.filter(sid=info[0], scno=info[1]).delete()
    return render(request, "deletegrade.html", {'success': '学生成绩删除成功！！！'})

