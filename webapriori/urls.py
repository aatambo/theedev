from django.urls import path

from .views import CsvHistoryView, CsvOpenView, CsvResultsView

urlpatterns = [
    path("", CsvOpenView.as_view(), name="open"),
    path("history/", CsvHistoryView.as_view(), name="history"),
    path("<int:pk>/", CsvResultsView.as_view(), name="results"),
]
