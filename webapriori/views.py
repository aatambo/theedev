import datetime

from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import View
from django.views.generic import CreateView, ListView

from .models import Csv
from .utilities import Apriori, sort_res


class CsvOpenView(CreateView):
    """
    creates a form view for posts
    """

    model = Csv
    fields = ["csv", "min_support"]
    template_name = "index.html"

    def get_success_url(self):
        """redirect to when form is valid"""
        return reverse("results", kwargs={"pk": self.object.pk})


class CsvHistoryView(ListView):
    """view for products list"""

    model = Csv
    template_name = "history.html"
    context_object_name = "csvs"


class CsvResultsView(View):
    """detail view for products including list and form views for reviews"""

    template_name = "results.html"

    def get(self, request, pk, *args, **kwargs):
        """handle HTTP GET"""
        csv = get_object_or_404(Csv, pk=pk)
        file = csv.csv
        file = "media/" + str(file)
        file = open(file, "r")
        content = file.read()
        min_sup = csv.min_support

        file_contents = []
        for line in content.split("\n"):
            line = line.strip().rstrip(",")  # Remove trailing comma
            record = frozenset(list(map(str.strip, line.split(",")[1:])))
            file_contents.append(record)

        start = datetime.datetime.now()
        items = Apriori(file_contents, min_sup)
        end = datetime.datetime.now()
        program_run_time = str((end - start))
        result = sort_res(items)
        all_items = len(items)

        context = {
            "csv": csv,
            "items": items,
            "result": result,
            "all_items": all_items,
            "program_run_time": program_run_time,
            "content": content,
        }

        return render(request, self.template_name, context)
