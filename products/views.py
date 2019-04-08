from django.shortcuts import render

# Create your views here.




def products_list(request):
    return render (request,
                   'products/index.html',
                   {'name':'test',
                    'some_func': lambda value: value or 'Argument is empty'
                    }
    )


def product_detail(request):
    return render(request, 'products/detail.html')
