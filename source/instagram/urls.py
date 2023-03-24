from django.urls import path

from instagram.views.publications import PublicationAddView, PublicationDetailView

urlpatterns = [
    path('publication_add/', PublicationAddView.as_view(), name='publication_add'),
    path('publication_detail/<int:pk>', PublicationDetailView.as_view(), name='publication_detail')
]
