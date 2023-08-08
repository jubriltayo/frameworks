# from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.
def product_create_view(request):
    # Pure django form
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data) #save to backend
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#   Pure HTML form
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

def product_detail_view(request, my_id=id):
    obj = get_object_or_404(Product, id=my_id)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

def product_update_view(request, my_id=id):
    """Set up initial value and loading and modifying backend data"""
    # initial_data = {
    #     "title": "My awesome title"
    # }
    # form = ProductForm(request.POST or None, initial=initial_data)
    obj = get_object_or_404(Product, id=my_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)

# def dynamic_lookup_view(request, my_id):
#     """Allows sub-routing with id &
#         also handles 404 error for missing ids in database"""
#     # obj = Product.objects.get(id=my_id)
#     obj = get_object_or_404(Product, id=my_id)
#     # try:
#     #     obj = Product.objects.get(id=my_id)
#     # except Product.DoesNotExist:
#     #     raise Http404
#     context = {
#         "object": obj
#     }
#     return render(request, "products/product_detail.html", context)

def product_delete_view(request, my_id):
    """Delete an entry from database via id"""
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        # confirm delete
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    """List everything in database """
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)