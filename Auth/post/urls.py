from django.urls import path
# from .views import list_view, create_view, update_view, read_view
from .views import *

# 앱 이름 설정
app_name = 'post'

urlpatterns = [
    path('list/', list_view, name='list' ),
    path('create/', create_view, name='create' ),
    path('<int:post_id>/', read_view, name='read' ),
    path('update/<int:post_id>/', update_view, name='update' ),
    path('delete/<int:post_id>/', delete_view, name='delete' ),
]