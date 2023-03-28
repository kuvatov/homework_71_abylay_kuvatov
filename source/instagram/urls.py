from django.urls import path

from instagram.views.comments import CommentCreateView
from instagram.views.home import HomeView
from instagram.views.likes import LikeView, UnlikeView
from instagram.views.publications import PublicationAddView, PublicationDetailView, UserSearchView, UserProfileView, \
    PublicationListView, ProfileView, ProfileUpdateView
from instagram.views.subscriptions import SubscriptionCreateView, SubscriptionDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('publication_add/', PublicationAddView.as_view(), name='publication_add'),
    path('publication_detail/<int:pk>', PublicationDetailView.as_view(), name='publication_detail'),
    path('publication_list/', PublicationListView.as_view(), name='publication_list'),
    path('user_search/', UserSearchView.as_view(), name='user_search'),
    path('user_profile/<int:pk>', UserProfileView.as_view(), name='user_profile'),
    path('subscribe/<int:pk>/', SubscriptionCreateView.as_view(), name='subscribe'),
    path('subscription/<int:pk>/unsubscribe/', SubscriptionDeleteView.as_view(), name='unsubscribe'),
    path('like/<int:pk>/', LikeView.as_view(), name='like'),
    path('like/<int:pk>/unlike', UnlikeView.as_view(), name='unlike'),
    path('publication_detail/<int:pk>/comment/add/', CommentCreateView.as_view(), name='comment_add'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update', ProfileUpdateView.as_view(), name='profile_update')
]
