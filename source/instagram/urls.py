from django.urls import path

from instagram.views.publications import PublicationAddView, PublicationDetailView, UserSearchView, UserProfileView

urlpatterns = [
    path('publication_add/', PublicationAddView.as_view(), name='publication_add'),
    path('publication_detail/<int:pk>', PublicationDetailView.as_view(), name='publication_detail'),
    path('user_search/', UserSearchView.as_view(), name='user_search'),
    path('user_detail/<int:pk>', UserProfileView.as_view(), name='user_profile')
]
