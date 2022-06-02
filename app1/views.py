from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def show1(request):
    return render(request,'app1/home1.html')

def show2(request):
    obj= request.POST.get('text','defalt')
    removepunc= request.POST.get('removepunc','off')
    fullcap= request.POST.get('fullcaf','off')
    charactor= request.POST.get('charactor','off')
    print(obj)

    if removepunc=="on":                                      # code with harry django L:11
        a="?.,:;[]()|/"
        b=""
        for i in obj:
            if i not in a:
                b+=i
        print(b)
        return render(request,'app1/home2.html',{'obj':b})

    elif fullcap =="on":
        b = ""
        for i in obj:
            b = b + i
            b=b.upper()
        return render(request, 'app1/home2.html', {'obj':b})
    elif charactor=='on':
        b=0
        for i in obj:
            b+=1
        #print(b)
        return render(request,'app1/home2.html',{'obj':b})
    #else:
        #return HttpResponse("error")


def show3(request):
    a="""<h1>select user website</h1>
    <a href=" https://www.facebook.com/">facebook</a><br>
    <a href=" https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04">how to install mysql</a><br>
    <a href=" https://www.makeuseof.com/how-to-install-visual-studio-code-ubuntu/#:~:text=To%20install%20Visual%20Studio%20Code%2C%20launch%20the%20Ubuntu%20Software%20app,directly%20from%20the%20Applications%20menu.">vs code</a><br>
    """
    return HttpResponse(a)