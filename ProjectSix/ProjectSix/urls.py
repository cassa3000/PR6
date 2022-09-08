from django.contrib import admin
from django.urls import path
from Six import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BlogListView.as_view()),
    path('post/<int:pk>', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete')

]
