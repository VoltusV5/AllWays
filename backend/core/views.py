import os
from django.conf import settings
from django.views.generic import View
from django.http import HttpResponse, Http404

class FrontendAppView(View):
    """Отдаёт index.html из Vue сборки"""
    def get(self, request):
        try:
            with open(os.path.join(settings.VUE_DIST_DIR, "index.html")) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            raise Http404("Vue build not found. Сначала собери фронтенд (npm run build).")
