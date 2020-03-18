from django.urls import path

from reporter.views import HomePageView, patients_dataset

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('patient/', patients_dataset, name='patients'),
]