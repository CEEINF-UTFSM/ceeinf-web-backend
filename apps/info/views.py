from django.views.generic import TemplateView


class ConvalidationsView(TemplateView):

    template_name = "convalidations.html"

class SubjectsView(TemplateView):

    template_name = "subjects_and_assistantships.html"
