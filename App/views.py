from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from App.models import *
from App.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView


# Create your views here.

def inicio(request):
    blogposts = BlogPost.objects.all()
    if blogposts:
        return render(request, 'App/inicio.html', {'blogposts':blogposts})
    else:
        return render(request, 'App/inicio.html', {'message':"Aun no hay posteos en el blog!"})

def about(request):
    teammembers = TeamMember.objects.all()
    if teammembers:
        return render(request, 'App/about.html', {'teammembers':teammembers})
    else:
        return render(request, 'App/about.html')
    
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contra)
            if user is not None:
                login(request, user)
                return render (request, 'App/inicio.html', {'message':f"Bienvenido {usuario}!!"})
            else:
                return render (request, 'App/inicio.html', {'message':"Ups, datos incorrectos."})
        else:
            return render (request, 'App/inicio.html', {'message':"Error, formulario incorrecto."})
    form = AuthenticationForm()
    return render (request, 'App/login.html', {'form':form})

def registro(request):
    if request.method == 'POST':
        myForm = UserRegisterForm(request.POST)
        if myForm.is_valid():
            username=myForm.cleaned_data['username']
            myForm.save()
            return render(request,"App/inicio.html", {"message":"El nuevo usuario fue creado exitosamente!"})
    else:
        myForm=UserRegisterForm()
    return render(request,'App/registro.html', {'myForm':myForm})

@login_required
def addblogpost(request):
    if request.method == 'POST':
        myForm = BlogPostForm(request.POST, request.FILES)
        if myForm.is_valid():
            title = myForm.cleaned_data['title']
            subtitle = myForm.cleaned_data['subtitle']
            content = myForm.cleaned_data['content']
            category = myForm.cleaned_data['category']
            image = myForm.cleaned_data['image'] if 'image' in myForm.cleaned_data else None
            author = request.user
            blogpost = BlogPost(title=title, subtitle=subtitle, content=content, category=category, image=image, author=author)
            blogpost.save()
            return render(request, "App/inicio.html", {'message': "El posteo fue agregado"})
    else:
        myForm = BlogPostForm()
    return render(request, 'App/addblogpost.html', {'myForm': myForm})

def updatepost(request, post_id):
    blogpost = BlogPost.objects.get(id=post_id)
    if request.method == 'POST':
        myForm = BlogPostForm(request.POST,  request.FILES)
        if myForm.is_valid():
            info = myForm.cleaned_data
            blogpost.title=info['title']
            blogpost.subtitle=info['subtitle']
            blogpost.content=info['content']
            blogpost.category=info['category']
            blogpost.image = myForm.cleaned_data['image'] if 'image' in myForm.cleaned_data else None
            blogpost.author = request.user
            blogpost.save()
            return render(request,"App/inicio.html", {'message': "El posteo fue actualizado."})
    else:  
        initial_data={'title':blogpost.title, 'subtitle':blogpost.subtitle, 'content':blogpost.content, 'category':blogpost.category}
        myForm=BlogPostForm(initial=initial_data)
        return render (request, 'App/updatepost.html', {'myForm':myForm})
    
@login_required
def deletepost(request, post_id):
    blogpost = BlogPost.objects.get(id=post_id)
    blogpost.delete()

    blogpost = BlogPost.objects.all()
    blogposts = {'blogpost':blogpost}

    return render(request, 'App/inicio.html', {'message':"El posteo fue eliminado."})

def blogpost(request):
    return HttpResponse("Blog Post")

def searchpostsite(request):
    return render(request, 'App/searchpostsite.html')

def searchpost(request):
    if request.GET['title']:
        title = request.GET['title']
        blogposts = BlogPost.objects.filter(title__contains=title)
        return render(request, 'App/blogpost.html', {'blogposts':blogposts})
    else:
        response = "No se ingresó información"
    return HttpResponse(response)

def contact(request):
    if request.method == 'POST':
        myForm = ContactMessageForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            name=info['name']
            lastname=info['lastname']
            message=info['message']
            contactmessage = ContactMessage(name=name,lastname=lastname,message=message)
            contactmessage.save()
            return render(request,"App/contact.html")
    else:
        myForm=ContactMessageForm()
    return render(request,'App/contact.html', {'myForm':myForm})

def profile(request):
    return render(request, 'App/profile.html')


def updateprofile(request):
    usuario = request.user
    avatar, created = Avatar.objects.get_or_create(user=usuario)
    if request.method == 'POST':
        myForm = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if myForm.is_valid():
            usuario = myForm.save(commit=False)
            usuario.email = myForm.cleaned_data['email']
            usuario.first_name = myForm.cleaned_data['first_name']
            usuario.last_name = myForm.cleaned_data['last_name']
            usuario.save()
            if 'imagen' in request.FILES:
                avatar.imagen = request.FILES['imagen']
                avatar.save()
            return render(request, "App/inicio.html", {'message': "La información de usuario fue actualizada."})
    else:
        myForm = UserUpdateForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)
    return render (request, 'App/updateprofile.html', {'myForm':myForm})


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = 'App/updatepassword.html'
    success_url = reverse_lazy('Inicio')

def error_404_view(request, exception):
    return render(request, 'App/404.html')