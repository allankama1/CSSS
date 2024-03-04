from django.shortcuts import render, redirect

from Hospitalmanagementsys.forms import ImageUploadForm
from hospitalapp.models import Members, appointment, Products, ImageModel


# Create your views here.
def index(request):
    if request.method == 'POST':
        appoint = appointment(name=request.POST['name'],
                              email=request.POST['email'],
                              phone=request.POST['phone'],
                              date=request.POST['date'],
                              department=request.POST['department'],
                              doctor=request.POST['doctor'],
                              message=request.POST['message'])
        appoint.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        member = Members(username=request.POST['username'],
                         password=request.POST['password'],
                         email=request.POST['email'])
        member.save()
        return redirect('/login')
    else:
        return render(request, 'Register.html')


def login(request):
    return render(request, 'Log in.html')


def appointmentdetails(request):
    myappoint = appointment.objects.all()
    return render(request, 'appointment details.html', {'myappoint': myappoint})


def details(request):
    products = Products.objects.all()
    return render(request, 'Products.html', {'products': products})


def adminhome(request):
    if request.method == 'POST':
        if Members.objects.filter(username=request.POST['username'],
                                  password=request.POST['password']).exists():
            members = Members.objects.get(username=request.POST['username'],
                                          password=request.POST['password'])
            return render(request, 'adminhome.html', {'members': members})
        else:
            return render(request, 'Log in.html')
    else:
        return render(request, 'Log in.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')
