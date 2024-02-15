"""Module providingFunction printing python version."""
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import *


# Create your views here.
def error_404_view(request,exception):
    return render(request, '404.html')

def myfunctioncall(request):
    """Function printing python version."""
    return HttpResponse("Hello World")

def myfuncabout(request):
    return HttpResponse("About response")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request, name, age):
    mydic = {
        "name": name,
        "age" : age
    }
    return( JsonResponse(name, age))

def myfirapp(request):
    return render(request,'index.html')

def mysecpage(request):
    return render(request, 'seon.html')

def mythirpage(request):
    var = "hello world"
    gret = "How are you?"
    fruits = ["apple", "mango"
              , "banana"]
    num_1, num_2 = 3, 5
    ans = num_1 > num_2
    # print(ans)
    mydic = {
        "var" : var,
        "msg" : gret,
        "myfrut" : fruits,
        "answ" : ans,
        "num1" : num_1,
        "num2" : num_2
        }
    return render(request, 'thirpage.html'
                  , context=mydic)

def myimgpage(request):
    return render(request, 'imgpage.html')

def myimgpage2(request):
    return render(request, 'imgpage2.html')

def myimgpage3(request):
    return render(request, 'imgpage3.html')

def myimgpage4(request):
    return render(request,'imgpage4.html')

def myimgpage5(request,imagename):
    myimagename = str(imagename)
    myimagename = myimagename.lower()
    print(myimagename)
    if myimagename == "django":
        var=True
    elif myimagename == "python":
        var=False
    mydictionary ={
        "var":var
    }
    return render(request,'imgpage5.html',context=mydictionary)

def myform(request):
    return render(request,'uform.html')

def submit(request):
    mydic = {
        "var1" : request.GET['usrname'],
        "var2" : request.GET['usremail'],
        "method": request.method
    }
    return JsonResponse(mydic)

def forms2(request):
    if request.method =="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydic = {
                "form" : FeedbackForm()
            }
            errorflag = False
            Errors = []
            
            if True != title.istitle():
                errorflag = True
                errormsg = "Title should be capitilized!"
                Errors.append(errormsg)
                
            import re    
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            
            if not re.search(regex, email):
                errorflag = True
                errormsg = "Not a Valid Email address"
                Errors.append(errormsg)
                
            # else:
            #     mydic["success"] = True
            #     mydic["successmsg"] =  "Form Submitted"
            #     return render(request,'forms.html',context=mydic)
            
            if errorflag != True:
                mydic["success"] = True
                mydic["successmsg"] = "Form Submitted"
            
                # print(tit)
                # print(sub)
                # var =str("Form Submitted" + str(request.method))
                # return HttpResponse(var)
            mydic["error"] = errorflag
            mydic["errors"] = Errors
            return render(request,'forms.html',context=mydic)
    
    
    elif request.method == "GET":
        form = FeedbackForm()
        mydic = {
            "form" : form
        }
        return render(request,'forms.html',context=mydic)
