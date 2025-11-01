from django.contrib import admin
from django.urls import path, include
from boards import views as boards_views
from accounts import views as accounts_views


urlpatterns = [
    path('', boards_views.BoardListView.as_view(), name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('accounts/', include('accounts.urls')),   # keep accounts auth routes here
    
    path('boards/<int:pk>', boards_views.TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/', boards_views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new/', boards_views.new_topic, name='new_topic'),
    path('admin/', admin.site.urls),
    path(
        'boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',
        boards_views.PostUpdateView.as_view(),
        name='edit_post'
    ),
    path(
        'boards/<int:pk>/topics/<int:topic_pk>/',
        boards_views.PostListView.as_view(),
        name='topic_posts'
    ),

    path('boards/<int:pk>/topics/<int:topic_pk>/reply/', boards_views.reply_topic, name='reply_topic'),


    path('settings/account/', accounts_views.UserUpdateView.as_view(), name='my_account'),



]
    
