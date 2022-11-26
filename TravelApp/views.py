from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Place
# Create your views here.
def index(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})


def register(request):
    return render(request,'register.html')
    print('entering')
    # name = request.POST['Name']
    # print(name,'name..')
    # password = request.POST['Password']
    # confirmpassword = request.POST['Confirmpassword']
    # print('........entering')

    # UserManage(username=name,password=password).save()
    # return render(request, 'login.html')

# def Login(reqest):
#     return render(reqest,'login.html')

# def loginView(request):
#     print('entering into login view')
#                                                                                                               
#     print(name,'name////..')
#     password=request.POST['Password']
#     if name and password:        
#         queryset = UserManage.objects.filter(username=name,password=password)
        
#         return render(request,'bank.html')
#     else:
#         return HttpResponse('No valid user')
    
# def (request):
#     return render(request,'bank.html')
# def logout_view(request):
#     logout(request)
#     return redirect('home')
        
