"""djangobookmark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookmarkap.views import BookmarkLV, BookmarkDV

urlpatterns = [
    # http://127.0.0.1:8000/admin
    path('admin/', admin.site.urls),
    
    # http://127.0.0.1:8000/bookmark
    # select * from bookmark;
    path('bookmark/', BookmarkLV.as_view(), name='index'),
    
    # http://127.0.0.1:8000/bookmark/?
    # select * from bookmark where id=1~3
    # 4부터 안되는 이유는 admin 페이지에서 만든 페이지수가 3개밖에 안되기 때문이다. 즉, 만들어진 id가 3까지만 있음
    path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),
]
