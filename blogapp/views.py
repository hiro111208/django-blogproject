from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import BlogPost

# Create your views here.


class IndexView(ListView):
    '''トップページのビュー

    投稿記事を一覧表示するのでListViewを継承する

    Attributes:
      template_name: レンダリングするテンプレート
      context_object_name: object_listキーの別名を設定
      queryset: データベースのクエリ
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # object_listキーの別名を設定
    context_object_name = 'orderby_records'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並べ替える
    queryset = BlogPost.objects.order_by('-posted_at')
