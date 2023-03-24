from django.urls import path

from instagram.views.comments import CommentListView, CommentCreateView
from instagram.views.home import HomeView
from instagram.views.likes import LikeView
from instagram.views.publications import PublicationAddView, PublicationDetailView, UserSearchView, UserProfileView, \
    PublicationListView
from instagram.views.subscriptions import SubscriptionCreateView, SubscriptionDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('publication_add/', PublicationAddView.as_view(), name='publication_add'),
    path('publication_detail/<int:pk>', PublicationDetailView.as_view(), name='publication_detail'),
    path('publication_list', PublicationListView.as_view(), name='publication_list'),
    path('user_search/', UserSearchView.as_view(), name='user_search'),
    path('user_profile/<int:pk>', UserProfileView.as_view(), name='user_profile'),
    path('subscribe/<int:pk>/', SubscriptionCreateView.as_view(), name='subscribe'),
    path('unsubscribe/<int:pk>/', SubscriptionDeleteView.as_view(), name='unsubscribe'),
    path('like/<int:pk>/', LikeView.as_view(), name='like'),
    path('publication_detail/<int:pk>/comment', CommentListView.as_view(), name='comment_list'),
    path('publication_detail/<int:pk>/comment/add/', CommentCreateView.as_view(), name='comment_add')
]
