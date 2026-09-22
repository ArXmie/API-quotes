from django.urls import path
from .views import *

urlpatterns = [
    path('quotes/', QuotesView.as_view()),
    path('quotes/<int:id>', Get_Quote.as_view()),
    path('quotes/add', QuotesView.as_view()),
    path('quotes/random', Get_Quote_random.as_view()),
    path('category/', CategoriesView.as_view()),
    path('category/<int:id>', CategoryView.as_view()),
    path('category/add', CategoriesView.as_view()),
    path('category/quotes', Quote_CategoryAll.as_view()),
    path('category/<int:category_id>/quotes/random', Get_Category_Quote_random.as_view()),
    path('category/<int:category_id>/quotes', Category_QuotesView.as_view()),
    path('category/quote/add', Category_QuotesView.as_view()),
    path('tag/', TagsView.as_view()),
    path('tag/add', TagsView.as_view()),
    path('category/<int:category_id>/quotes/<int:quote_id>', Get_Category_Quote.as_view()),
    path('tag/<int:tag_id>/quotes/<int:quote_id>', Get_Tag_Quote.as_view()),
    path('tag/quote/add', Tag_QuotesView.as_view()),
    path('tag/<int:tag_id>/quotes/random', Get_Tag_Quote_random.as_view()),
    path('tag/<int:tag_id>/quotes', Tag_QuotesView.as_view()),
    path('six', FirstView),
    path('day', SecondView.as_view()),
    path('seven-days', ThirdView.as_view()),
    path('no-cache', FourthView.as_view()),
    path('template', FifthView.as_view())
]