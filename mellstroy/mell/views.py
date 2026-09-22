from django.shortcuts import render
from django.views.decorators.cache import cache_control, never_cache
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest,JsonResponse
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import *
from .forms import *

import random

@cache_control(
    max_age=60*60*24,
    public=True,
    # private=True,
    # no_cache=True,
    # keep_if_cached=False
)
def my_view(request):
    ...

@never_cache
def another_view(request):
    ...
    
@cache_control(
    max_age=60*60*6,
    public=True,
)
def FirstView(request):
    return render(request, 'index.html')
    
@method_decorator(cache_control(
    max_age=60*60*24,
    public=True
), 'dispatch')
class SecondView(View):
    def get(self, request):
        return render(request, 'index.html')
    
@method_decorator(cache_control(
    max_age=60*60*24*7,
    public=True
), 'dispatch')
class ThirdView(View):
    def get(self, request):
        return render(request, 'index.html')
    
@method_decorator(never_cache, 'dispatch')
class FourthView(View):
    def get(self, request):
        return render(request, 'index.html')
    
@method_decorator(cache_control(
    max_age=60*60*24*7,
    public=True
), 'dispatch')
class FifthView(TemplateView):
    template_name = 'index.html'

@method_decorator(csrf_exempt, 'dispatch')
class QuotesView(View):
    def get(self, request):
        quotes = list(Quotes.objects.values('id', 'quote', 'author'))
        obj = {
            'data': quotes
        }
        return JsonResponse(obj)
    
    def post(self, request):
            raw_json = request.body
            new_data = loads(raw_json)
            
            form = QuoteForm(new_data)
            if form.is_valid():
                quote = form.save()
                return JsonResponse(
                    {'status': 'success', 
                     'message': 'Added!',
                     'id': quote.pk}, status=201
                )
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400},
                    status=400
                    )
    
@method_decorator(csrf_exempt, 'dispatch')    
class Get_Quote(View):
    def get(self, request, id):
        quote = Quotes.objects.values('id', 'quote', 'author').get(id=id)
        return JsonResponse(quote)

    def put(self, request, id):
            quote_instance = get_object_or_404(Quotes, id=id)
            dict_from_request = loads(request.body)
            form = QuoteForm(dict_from_request, instance=quote_instance)
            if form.is_valid():
                quote = form.save()
                return JsonResponse(
                    {'status': 'success',
                    'message': 'Changed!',
                    'id': quote.id}, status=201
                )
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400}, status=400
                )
    
class Get_Quote_random(View):
    def get(self, request):
        quote = Quotes.objects.order_by('?').values('id', 'quote', 'author').first()
        return JsonResponse(quote)
    
class Get_Category_Quote_random(View):
    def get(self, request, category_id):
        quote_data = Quote_Category.objects.filter(category_id=category_id).order_by('?').values(
            'quote__id',
            'quote__quote',
            'quote__author'
        ).first()

        return JsonResponse(quote_data)
    
@method_decorator(csrf_exempt, 'dispatch')    
class Category_QuotesView(View):
    def get(self, request, category_id):
        quote_data = list(Quote_Category.objects.filter(category_id=category_id).values(
            'quote__id',
            'quote__quote',
            'quote__author'
        ))

        return JsonResponse({'data': quote_data})
    
    def post(self, request):
            raw_json = request.body
            new_data = loads(raw_json)
            
            form = Q_CForm(new_data)
            if form.is_valid():
                q_c = form.save()
                return JsonResponse(
                    {'status': 'success', 
                     'message': 'Added!',
                     'id': q_c.pk}, status=201
                )
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400},
                    status=400
                    )
    
class Get_Category_Quote(View):
    def get(self, request, category_id, quote_id):
        quote_data = Quote_Category.objects.filter(
            category_id=category_id,
            quote_id=quote_id).values(
            'quote__id',
            'quote__quote',
            'quote__author'
        ).get()

        return JsonResponse(quote_data)

@method_decorator(csrf_exempt, 'dispatch')
class CategoriesView(View):
    def get(self, request):
        category = list(Category.objects.values('id', 'name'))
        obj = {
            'data': category
        }
        return JsonResponse(obj)
    
    def post(self, request):
            raw_json = request.body
            new_data = loads(raw_json)
            
            form = CategoryForm(new_data)
            if form.is_valid():
                category = form.save()
                return JsonResponse(
                    {'status': 'success', 
                     'message': 'Added!',
                     'id': category.pk}, status=201
                )
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400},
                    status=400
                    )

class Quote_CategoryAll(View):
    def get(self, request):
            q_c = list(Quote_Category.objects.values('id', 'quote', 'category'))
            obj = {
                'data': q_c
            }
            return JsonResponse(obj)

@method_decorator(csrf_exempt, 'dispatch')                
class CategoryView(View):
    def get(self, request, id):
        category = Category.objects.values('id', 'name').get(id=id)
        obj = {
            'data': category
        }
        return JsonResponse(obj)
    
    def put(self, request, id):
        c_instance = get_object_or_404(Category, id=id)
        dict_from_request = loads(request.body)
        form = CategoryForm(dict_from_request, instance=c_instance)
        if form.is_valid():
            quote = form.save()
            return JsonResponse(
                {'status': 'success',
                'message': 'Changed!',
                'id': quote.id}, status=201
            )
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400}, status=400
            )
    
@method_decorator(csrf_exempt, 'dispatch')
class TagsView(View):
    def get(self, request):
        tag = list(Tags.objects.values('id', 'name'))
        obj = {
            'data': tag
        }
        return JsonResponse(obj)
    
    def post(self, request):
            raw_json = request.body
            new_data = loads(raw_json)
            
            form = TagForm(new_data)
            if form.is_valid():
                tag = form.save()
                return JsonResponse(
                    {'status': 'success', 
                     'message': 'Added!',
                     'id': tag.pk}, status=201
                )
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400},
                    status=400
                    ) 
                
@method_decorator(csrf_exempt, 'dispatch')                
class TagView(View):
    def get(self, request, id):
        category = Category.objects.values('id', 'name').get(id=id)
        obj = {
            'data': category
        }
        return JsonResponse(obj)
    
    def put(self, request, id):
        t_instance = get_object_or_404(Tags, id=id)
        dict_from_request = loads(request.body)
        form = CategoryForm(dict_from_request, instance=t_instance)
        if form.is_valid():
            tag = form.save()
            return JsonResponse(
                {'status': 'success',
                'message': 'Changed!',
                'id': tag.id}, status=201
            )
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400}, status=400
            )
    
    
class Get_Tag_Quote(View):
    def get(self, request, tag_id, quote_id):
        quote_data = Quote_Tag.objects.filter(
            tag_id=tag_id,
            quote_id=quote_id).values(
            'quote__id',
            'quote__quote',
            'quote__author'
        ).get()
        return JsonResponse(quote_data)
    
@method_decorator(csrf_exempt, 'dispatch')
class Tag_QuotesView(View):
    def get(self, request, tag_id):
        quote_data = list(Quote_Tag.objects.filter(
            tag_id=tag_id).values(
            'quote__id',
            'quote__quote',
            'quote__author'
        ))
        return JsonResponse({'data':quote_data})
    
    def post(self, request):
            raw_json = request.body
            new_data = loads(raw_json)
            
            form = Q_TForm(new_data)
            if form.is_valid():
                quote = form.save()
                return JsonResponse(
                    {'status': 'success', 
                     'message': 'Added!',
                     'id': quote.pk}, status=201
                )
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400},
                    status=400
                    )
    
class Get_Tag_Quote_random(View):
    def get(self, request, tag_id):
        quote_data = Quote_Tag.objects.filter(tag_id=tag_id).order_by('?').values(
            'quote__id',
            'quote__quote',
            'quote__author'
        ).first()

        obj = {
            'data': quote_data
        }
        return JsonResponse(obj)