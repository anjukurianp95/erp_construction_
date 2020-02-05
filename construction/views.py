from django.shortcuts import render
from construction.models import admin,contractor,employee,contracts,selectemployee
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def adminhome(request):
    return render(request,'adminhome.html')


def loginsubmit(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=admin.objects.filter(username=username,password=password)
        if(u.count()==1):
            return render(request,'adminhome.html')
        else:
            uc=contractor.objects.filter(email=username,password=password)
            if(uc.count()==1):
                request.session['usr']=username
                return render(request,'contractorhome.html')
            else:
                ue=employee.objects.filter(email=username,password=password)
                if(ue.count()==1):
                    request.session['usr']=username
                    return render(request,'employeehome.html')
                else:
                    return HttpResponse('username or password incorrect')
def addcontractor(request):
    return render(request,'adminaddcontractor.html')

def addemp(request):
    return render(request,'adminaddemployee.html')

def addcontract(request):
    query=contractor.objects.filter(status='available')
    return render(request,'adminaddcontract.html',{'authors':query})

def removecontractor(request):
    query=contractor.objects.all()
    return render(request,'adminremovecontractor.html',{'authors':query})

def viewcontractor(request):
    query=contractor.objects.all()
    return render(request,'adminviewcontractor.html',{'authors':query})

def adminremoveemployee(request):
    query=employee.objects.all()
    return render(request,'adminremoveemployee.html',{'authors':query})

def adminviewemployee(request):
    query=employee.objects.all()
    return render(request,'adminviewemployee.html',{'authors':query})

def submitcontractor(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
    a=contractor(name=name,email=email,mobile=mobile,password=password)
    a.save()
    return redirect('adminaddcontractor')

def submitemp(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        grade=request.POST.get('grade')
        salary=request.POST.get('salary')
        nid=request.POST.get('nationalid')
        email=request.POST.get('email')
        password=request.POST.get('password')
    a=employee(name=name,email=email,mobile=mobile,password=password,grade=grade,salary=salary,nationalid=nid)
    a.save()
    return redirect('adminaddemployee')

def submitcontract(request):
    if request.method=="POST":
        client=request.POST.get('client')
        mobile=request.POST.get('mobile')
        jtype=request.POST.get('type')
        contractor=request.POST.get('contractor')
        fdate=request.POST.get('fromdate')
        tdate=request.POST.get('todate')
        noemp=request.POST.get('noemp')
        budget=request.POST.get('budget')
        a=contracts(client=client,mobile=mobile,jtype=jtype,contractor=contractor,fromdate=fdate,todate=tdate,noemp=noemp,budget=budget)
        a.save()
        return redirect('adminaddcontract')

def submitcontractorremove(request):
    id=request.POST.get('id')
    b=contractor.objects.get(id=id)
    b.delete()
    return redirect('adminremovecontractor')

def submitemployeeremove(request):
    id=request.POST.get('id')
    b=employee.objects.get(id=id)
    b.delete()
    return redirect('adminremoveemployee')
#--------------------------------------
def contractorhome(request):
    return render(request,'contractorhome.html')

def contractorviewemployee(request):
    query=employee.objects.all()
    return render(request,'contractorviewemployee.html',{'authors':query})


def contractorviewworks(request):
    query=contractor.objects.get(email=request.session['usr'])
    a=query.id
    q2=contracts.objects.filter(contractor=a)
    return render(request,'contractorviewworks.html',{'authors':q2})

def submitworkstatus(request):
    if request.method=='POST':
        wid=request.POST.get('id')
        status=request.POST.get('status')
        query=contractor.objects.get(email=request.session['usr'])
        a=query.id
        contracts.objects.filter(id=wid).update(status=status)
        if(status=='Completed'):
            contractor.objects.filter(id=a).update(status='available')
        if(status=='Approved'):
            contractor.objects.filter(id=a).update(status='on work')
        if(status=='Pending'):
            contractor.objects.filter(id=a).update(status='available')
        return redirect('contractorviewworks')

def selectemployeee(request):
    query=contracts.objects.all()
    query2=employee.objects.all()
   
    return render(request,'contractorselectemployee.html',{'authors':query,'authors2':query2})

def selectemployeesubmit(request):
    if request.method=="POST":
        wid=request.POST.get('workid')
        eid=request.POST.get('empid')
        a=selectemployee(wid=wid,eid=eid)
        a.save()
    return redirect('contractorselectemployee')

    #------------------------------------------------------------

def employeehome(request):
    return render(request,'employeehome.html')

def employeeviewworks(request):
    query=employee.objects.get(email=request.session['usr'])
    a=query.id
    q2=selectemployee.objects.filter(eid=a)
    
    if(q2.count()==0):
        return HttpResponse('no works assigned currently')
    else:
        q4=selectemployee.objects.get(eid=a)
        b=q4.wid
        q3=contracts.objects.filter(id=b) 
        return render(request,'employeeviewworks.html',{'authors':q3})
    
        