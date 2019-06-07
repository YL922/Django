from django.db import models

# Create your models here.
class clazz(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30)

    def __unicode__(self):
        return u'clazz:%s'%self.cname

class course(models.Model):
    course_no=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=30)

    def __unicode__(self):
        return u'course:%s'%self.course_name

class student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    cls=models.ForeignKey(clazz,on_delete=models.CASCADE)
    cour=models.ManyToManyField(course)

    def __unicode__(self):
        return u'student:%s'%self.sname


def getcls(cname):
    try:
        cls=clazz.objects.get(cname=cname)
    except clazz.DoesNotExist:
        cls = clazz.objects.create(cname=cname)
    return cls


def getcourselist(*coursenames):
    courselist=[]
    for cn in coursenames:
        try:
            c=course.objects.get(course_name=cn)
        except course.DoesNotExist:
            c = course.objects.create(course_name=cn)
        courselist.append(c)
    return courselist



def register(sname,cname,*coursenames):
    cls=getcls(cname)
    courselist=getcourselist(*coursenames)
    try:
        stu=student.objects.get(sname=sname)
    except student.DoesNotExist:
        stu=student.objects.create(sname=sname,cls=cls)
    stu.cour.add(*courselist)

    return True

