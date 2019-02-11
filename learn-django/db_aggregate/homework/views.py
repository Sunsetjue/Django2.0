from django.shortcuts import render
from .models import Score,Student,Course,Teacher
from django.db.models import Sum,Avg,Count,Q,Max,Min,F
from django.http import HttpResponse

# Create your views here.
def homework_one(request):
    '''查询平均成绩大于60分的同学的id和平均成绩'''
    students = Student.objects.annotate(avg=Avg("score__number")).filter(avg__gt=60)
    for student in students:
        print(student.id,student.avg)

    return HttpResponse("success")

def homework_two(request):
    '''查询所有同学的id、姓名、选课的数量、总成绩'''
    # students1 = Student.objects.all()
    students = Student.objects.annotate(count=Count("score__course"),sum=Sum("score__number"))
    for student in students:
        print("id是{} 名字是{} 选课数量是{} 总成绩是{}".format(student.id, student.name, student.count, student.sum))

    return HttpResponse("success")

def home_three(request):
    '''查询姓“李”的老师的个数'''
    num = Teacher.objects.filter(name__contains="李").aggregate(count=Count("id"))
    print(num['count'])

    # 查询没学过“李老师”课的同学的id、姓名
    students = Student.objects.exclude(score__course__teacher__name__exact="李老师").values("id","name")
    for student in students:
        print(student)

    print('\n')

    # 查询学过课程id为1和2的所有同学的id、姓名
    students2 = Student.objects.filter(Q(score__course__id=1)|Q(score__course__id=2)).values("id","name").distinct()
    for student2 in students2:
        print(student2)

    print('\n')
    # 查询学过“黄老师”所教的“所有课”的同学的id、姓名
    students3 = Student.objects.filter(score__course__teacher__name__exact="黄老师").values("id","name").distinct()
    for student3 in students3:
        print(student3)

    return HttpResponse("success")

def homework_four(request):
    '''查询所有课程成绩小于60分的同学的id和姓名'''
    students1 = Student.objects.filter(score__number__lt=60).values("id","name").distinct()
    for student1 in students1:
        print(student1)

    print("\n")

    # 查询没有学全所有课的同学的id、姓名
    students2 = Student.objects.annotate(count=Count("score__course__id")).filter(count__lt=Course.objects.count()).values("id","name")
    for student2 in students2:
        print(student2)

    print("\n")

    # 查询所有学生的姓名、平均分，并且按照平均分从高到低排序
    results = Student.objects.annotate(avg=Avg("score__number")).order_by("-avg").values("name", "avg")
    for result in results:
        print(result)

    return HttpResponse("success")

def homework_five(request):
    '''查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分'''
    courses = Course.objects.annotate(max=Max("score__number"), min=Min("score__number"))
    for course in courses:
        print("课程ID是{} 课程名称是{} 最高分是{} 最低分是{}".format(course.id,course.name,course.max,course.min))

    print("\n")

    # 查询每门课程的平均成绩，按照平均成绩进行排序
    courses2 = Course.objects.annotate(avg=Avg("score__number")).order_by("-avg")
    for course2 in courses2:
        print("name:{} average:{}".format(course2.name,course2.avg))

    #统计总共有多少女生，多少男生
    result1 = Student.objects.filter(gender=1).count()
    result2 = Student.objects.filter(gender=2).count()
    print("男生有{} 女生有{}".format(result1,result2))


    return HttpResponse("success")

def homework_six(request):
    '''将“黄老师”的每一门课程都在原来的基础之上加5分'''
    Score.objects.filter(course__teacher__name="黄老师").update(number=F("number")+5)

    return HttpResponse("success")

def homework_seven(request):
    # 查询两门以上不及格的同学的id、姓名、以及不及格课程数
    students = Student.objects.filter(score__number__lt=60).annotate(count=Count("score__number")).filter(count__gte=2).values("id","name","count")
    for student in students:
        print(student)

    # 查询每门课的选课人数
    courses = Course.objects.annotate(count=Count("score__student__id")).values("name","count")
    for course in courses:
        print(course)

    return HttpResponse("success")