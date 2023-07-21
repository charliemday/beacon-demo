from django.urls import path

from .views import PromptLogListCreateView

urlpatterns = [
    path(
        "log-prompt/", PromptLogListCreateView.as_view(), name="prompt-log-list-create"
    )
]
