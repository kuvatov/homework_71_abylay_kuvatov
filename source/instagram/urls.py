from django.urls import path

from instagram.views.comments import CommentCreateView
from instagram.views.home import HomeView
from instagram.views.likes import LikeCreateView
from instagram.views.profiles import ProfileView, ProfileUpdateView, ProfileSearchView, ProfileDetailView
from instagram.views.publications import PublicationCreateView, PublicationDetailView
from instagram.views.subscriptions import SubscriptionCreateView, SubscriptionDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('publication_create/', PublicationCreateView.as_view(), name='publication_create'),
    path('publication_detail/<int:pk>', PublicationDetailView.as_view(), name='publication_detail'),
    path('user_search/', ProfileSearchView.as_view(), name='user_search'),
    path('user_profile/<int:pk>', ProfileDetailView.as_view(), name='user_profile'),
    path('user_profile/<int:pk>/subscribe/', SubscriptionCreateView.as_view(), name='subscribe'),
    path('user_profile/<int:pk>/unsubscribe/', SubscriptionDeleteView.as_view(), name='unsubscribe'),
    path('publication_detail/<int:pk>/like/', LikeCreateView.as_view(), name='like'),
    path('publication_detail/<int:pk>/comment/add/', CommentCreateView.as_view(), name='comment_add'),
    path('personal_profile/', ProfileView.as_view(), name='profile'),
    path('personal_profile/update', ProfileUpdateView.as_view(), name='profile_update')
]
