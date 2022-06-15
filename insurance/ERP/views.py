from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
# Create your views here.

# ------------------------------------------------- Global Variable-----------------------------------------
def globals(request):
    use=request.user
    user_name=User.objects.filter(username=use)
    company_info = Company_info.objects.all()
    context={
        'user_name':user_name,
        'company_info':company_info
    }
    return context
# ------------------------------------------------- Global Variable-----------------------------------------

def index(request):
    return render(request,'index.html',globals(request))

def Dashboardv(request):
    return render(request,'dashboard.html',globals(request))

def AdminDashboardv(request):
    return render(request,'pages/admin/admin_dashboard.html',globals(request))

def Branch_Infor_showV(request):
    return render(request,'pages/admin/branch_info/forms/branch_info.html',globals(request))
def Branch_Infor_saveV(request):
    if request.method == 'POST':
        counts=BranchInformation.objects.all().count()
        id=counts+1
        user = request.user.id
        user_name=User.objects.get(id=user)
        Name=request.POST.get('name')
        Short=request.POST.get('short')
        Address=request.POST.get('address')
        Phone=request.POST.get('phone')
        Fax=request.POST.get('fax')
        Email=request.POST.get('email')
        data=BranchInformation(id=id,B_name=Name,B_short_name=Short,B_address=Address,B_phone=Phone,B_fax=Fax,B_email=Email,Create_user=user_name)
        data.save()
        mess="Data save"
        return JsonResponse({"mess":mess},status=200,safe=False)

