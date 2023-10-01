from django.shortcuts import render
from .models import resource
from .functions import handle_uploaded_file  
from .forms import UploadFileForm
from django.http import HttpResponse  
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,"signup.html")

def services(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES)
        # for i in request.FILES:
        #     print(request.FILES[i])
        file = request.FILES['file']
        reso = resource()
        # reso.desc = request.POST.get('Description')
        reso.desc = request.POST.get('Description')
        reso.img = file
        print(str(reso.img))
        reso.save()
        # return HttpResponse("YOUR FILE HAS BEEN UPLOADED! THANK YOU.\n SHARE MORE")
        return render(request,'index.html')
    else:
        form = UploadFileForm()
    return render(request,'services.html',{'form' : form})

def display(request):

    reso = resource.objects.all()
    k = 0
    dic = []
    for i in reso:
        temp = dict()
        temp['id'] = str(k)
        temp['desc'] = i.desc
        temp['file'] = str(i.img)
        dic.append(temp)
        # print(dic)
        k += 1
    return render(request,'products.html', {'dic' : dic})