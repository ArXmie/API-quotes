from django.urls import path
from .views import *

urlpatterns = [
    path('quotes/', Get_Quotes.as_view()),
    path('quotes/<int:id>', Get_Quote.as_view()),
    path('quotes/add', Post_Quote.as_view()),
    path('quotes/random', Get_Quote_random.as_view()),
    path('category/', Get_Category.as_view()),
    path('category/add', Post_Category.as_view()),
    path('category/<int:category_id>/quotes/random', Get_Category_Quote_random.as_view()),
    path('category/<int:category_id>/quotes', Get_Category_Quotes.as_view()),
    path('category/quote/add', Post_Q_C.as_view()),
    path('tag/', Get_Tag.as_view()),
    path('tag/add', Post_Tag.as_view()),
    path('category/<int:category_id>/quotes/<int:quote_id>', Get_Category_Quote.as_view()),
    path('tag/<int:tag_id>/quotes/<int:quote_id>', Get_Tag_Quote.as_view()),
    path('tag/quote/add', Post_Q_T.as_view()),
    path('tag/<int:tag_id>/quotes/random', Get_Tag_Quote_random.as_view()),
    path('tag/<int:tag_id>/quotes', Get_Tag_Quotes.as_view()),
    path('six', FirstView),
    path('day', SecondView.as_view()),
    path('seven-days', ThirdView.as_view()),
    path('no-cache', FourthView.as_view()),
    path('template', FifthView.as_view())
]