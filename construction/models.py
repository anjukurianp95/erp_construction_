from django.db import models

# Create your models here.

class Meta:
    db_table= 'admin'
    db_table= 'contractor'
    db_table= 'employee'
    db_table= 'contracts'
    db_table= 'selectemployee'

class admin(models.Model):
    username=models.CharField(max_length=20,default='admin')
    password=models.CharField(max_length=20)

class contractor(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='available')

class employee(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    nationalid=models.IntegerField()
    grade=models.CharField(max_length=10)
    salary=models.IntegerField()
    status=models.CharField(max_length=20,default='available')


class contracts(models.Model):
    client=models.CharField(max_length=20)
    mobile=models.IntegerField()
    jtype=models.CharField(max_length=20)
    contractor=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='pending')
    fromdate=models.DateField()
    todate=models.DateField()
    noemp=models.IntegerField()
    budget=models.IntegerField()

class selectemployee(models.Model):
    wid=models.IntegerField()
    eid=models.IntegerField()
