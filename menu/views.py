from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Category

def home(request):
    current_url = request.path
    return render(request, 'menu/index.html', {'current_url': current_url})

def show_category(request, cat_id):
    current_url = request.path

    return render(request, 'menu/index.html', {'current_url': current_url})

# def show_category(request, cat_id):
#     cat = get_object_or_404(Category, id=cat_id)

#     response_data = f'id: {cat.id}<br>'
#     response_data += f'Title: {cat.title}<br>'

#     if cat.parent:
#         response_data += f'Parent: {cat.parent.title}<br>'
    
#     subcat = cat.children.all()
#     if subcat:
#         response_data += 'Subcategory:<br>'
#         for sub in subcat:
#             response_data += f'\a- {sub.title}<br>'

#     response_data += f'Slug: {cat.slug}<br>'
#     response_data += f'Created At: {cat.created_at}<br>'
    
#     return HttpResponse(response_data)