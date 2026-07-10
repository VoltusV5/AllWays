"""
Views для приложения core.
"""

import logging

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View


logger = logging.getLogger(__name__)


class FrontendAppView(View):
    """
    Отдает index.html собранного Vue.js приложения.
    Используется для передачи управления клиентскому роутеру.
    """

    def get(self, request, *args, **kwargs):

        index_file_path = settings.VUE_DIST_DIR / "index.html"

        try:
            content = index_file_path.read_text(encoding="utf-8")
            return HttpResponse(content)
            
        except FileNotFoundError:
            logger.error(f"Frontend build not found at {index_file_path}")
            return HttpResponse(
                "Frontend build not found. Please run 'npm run build' in your Vue app.", 
                status=501
            )
