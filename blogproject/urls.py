from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
(r'^$', 'blogproject.blog.views.index'),
url(
    r'^blog/view/(?P<slug>[^\.]+).html', 
    'blogproject.blog.views.view_post', 
    name='view_blog_post'),
url(
    r'^blog/category/(?P<slug>[^\.]+).html', 
    'blogproject.blog.views.view_category', 
    name='view_blog_category'),

