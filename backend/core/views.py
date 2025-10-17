from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os

class FrontendAppView(View):
    def get(self, request):
        try:
            # Путь к файлу index.html после сборки Vue
            index_file_path = os.path.join(settings.VUE_DIST_DIR, 'index.html')

            # Чтение содержимого файла
            with open(index_file_path, 'r') as file:
                content = file.read()

            # Возвращаем файл как HTTP Response
            return HttpResponse(content)

        except FileNotFoundError:
            return HttpResponse("Frontend build not found. Please build your Vue app.", status=500)

