from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = """<h1>Bienvenido a mi web</h1>
<ul>
<li><a href="/">Home</a></li>
<li><a href="/about">Acerca de</a></li>
<li><a href="/portafolio">Portafolio</a></li>
<li><a href="/contact">Contacto</a></li>
</ul>
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")