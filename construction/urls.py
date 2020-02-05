from django.urls import path
from construction import views

urlpatterns=[
        path('', views.index,name='index'),
        path('login/',views.login,name='login'),
        path('logout/',views.logout_view,name='logout'),
        path('admihome/',views.adminhome,name='adminhome'),
        path('loginsubmit/',views.loginsubmit,name='loginsubmit'),
        path('addcontractor/',views.addcontractor,name='adminaddcontractor'),
        path('addcontractorsubmit/',views.submitcontractor,name='contractorsubmit'),
        path('viewcontractor/',views.viewcontractor,name='adminviewcontractor'),
        path('viewemployee/',views.adminviewemployee,name='adminviewemployee'),
        path('addemp/',views.addemp,name='adminaddemployee'),
        path('addempsubmit/',views.submitemp,name='empsubmit'),
        path('addcontract/',views.addcontract,name='adminaddcontract'),
        path('submitcontract/',views.submitcontract,name='contractsubmit'),
        path('removecontractorpage/',views.removecontractor,name='adminremovecontractor'),
        path('removecontractor/',views.submitcontractorremove,name='submitremovecontractor'),
        path('removeemployeepage/',views.adminremoveemployee,name='adminremoveemployee'),
        path('removeemp/',views.submitemployeeremove,name='submitremoveemployee'),
         path('contractorviewemployee/',views.contractorviewemployee,name='contractorviewemployee'),

        #---------------------------------------------------------------------
        
        path('contractorhome/',views.contractorhome,name='contractorhome'),
        path('contractorviewworks/',views.contractorviewworks,name='contractorviewworks'),
        path('submitworkstatus/',views.submitworkstatus,name='submitworkstatus'),
        path('contractorselectemployee/',views.selectemployeee,name='contractorselectemployee'),
        path('selectemploysubmit/',views.selectemployeesubmit,name='selectemployeesubmit'),

        #----------------------------------------------------------------------
        
        path('employeehome/',views.employeehome,name='employeehome'),
        path('employeeviewworks/',views.employeeviewworks,name='employeeviewworks'),
]