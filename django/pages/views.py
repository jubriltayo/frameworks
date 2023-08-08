from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    # print(request.user)
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About Us</h1>")
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [343, 232, 4665, 564, 342],
        "my_html": "<h1>This is a plain html</h1>"
    } 
    return render(request, "about.html", my_context)

def product_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Product and Services</h1>")
    return render(request, "product.html", {})