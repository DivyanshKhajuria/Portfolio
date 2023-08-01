from django.shortcuts import render
from .models import Mymessage


# Create your views here.
def about(request):
    contaxt={'about':'active'}
    return render(request, 'myapp/about.html', contaxt)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        youmsg=request.POST['youmsg']
        obj=Mymessage(name=name, email=email, youmsg=youmsg)
        obj.save()
  
    return render(request, 'myapp/contactme.html')


def educations(request):
    contaxt1={'education':'active'}
    return render(request, 'myapp/edu.html', contaxt1)



# Create your views here.
def skills(request):
    contaxt={'skills':'active'}
    return render(request, 'myapp/skill.html',contaxt)



