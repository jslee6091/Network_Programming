from django.contrib import admin
from django.urls import path, include

from mysite.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),

    # http://localhost.8000/ -> home page
    path('', HomeView.as_view(), name='home'),

    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),
    
]

# bookmark 의 urls.py를 이용한다.
