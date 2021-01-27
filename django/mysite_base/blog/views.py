from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import MonthArchiveView, DayArchiveView
from django.views.generic.dates import TodayArchiveView
from blog.models import Post

# Search 관련
from django.views.generic.edit import FormView
from blog.form import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html"
    
    # object_list의 context name 설정 
    # 안하면 model name에서 _list가 추가된 형태로 자동 지정
    context_object_name = "posts"
    
    # paginating a Listview
    paginate_by = 3

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = "modify_date"

class PostYAV(YearArchiveView):
    model = Post
    make_object_list = True
    date_field = "modify_date"


class PostMAV(MonthArchiveView):
    model = Post
    date_field = "modify_date"
    month_format ="%m"


class PostDAV(DayArchiveView):
    model = Post
    date_field = "modify_date"
    month_format ="%m"


class PostTAV(TodayArchiveView):
    model = Post
    date_field = "modify_date"
    month_format ="%m"


# SearchFormView는 내가 만든 이름, FormView는 장고에 내장된 것
class SearchFormView(FormView):
    form_class = PostSearchForm # form.py에 생성
    template_name = "blog/post_search.html"
    
    # 검색 할때의 페이지와 검색 결과가 나오는 페이지를 같게 한다.
    def form_valid(self, form):
        schword = self.request.POST['search_word']

        post_list = Post.objects.filter(Q(title__icontains=schword)| Q(description__icontains=schword)|Q(content__icontains=schword)).distinct()

        # 검색된 결과
        context = {}
        context['form'] = form
        context['search_keyword'] = schword
        context['search_list'] = post_list


        # request는 사용자가 전달한 정보
        return render(self.request, self.template_name, context)

