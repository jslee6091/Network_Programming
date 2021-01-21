from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import MonthArchiveView, DayArchiveView
from django.views.generic.dates import TodayArchiveView
from blog.models import Post

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = "posts" # object_list

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



