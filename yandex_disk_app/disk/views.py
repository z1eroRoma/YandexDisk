import json
from zipfile import ZipFile

import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .services import YandexDiskAPI
from .forms import FileFilterForm


def index(request):
    if request.method == 'POST':
        public_key = request.POST.get('public_key')
        if public_key:
            request.session['public_key'] = public_key
            return HttpResponseRedirect('files/')
    return render(request,'disk/index.html')

def file_list(request):
    public_key = request.session.get('public_key')
    if not public_key:
        return HttpResponseRedirect('/')

    api = YandexDiskAPI(public_key)
    filter_form = FileFilterForm(request.GET or None)
    try:
        response = api.get_files()
        files = response.get('_embedded', {}).get('items', [])

        # Проверка типа файла
        for file in files:
            file['is_image'] = file['mime_type'].startswith('image/')
            file['is_document'] = file['mime_type'].startswith('application/')

        # Фильтрация файлов по типу
        file_type = filter_form.cleaned_data.get('file_type') if filter_form.is_valid() else 'all'
        if file_type == 'image':
            files = [f for f in files if f['is_image']]
        elif file_type == 'document':
            files = [f for f in files if f['is_document']]

    except requests.RequestException as e:
        return HttpResponse(f'Ошибка при получении файлов с Яндекс.Диска: {str(e)}')

    return render(request, 'disk/file_list.html', {
        'files': files,
        'filter_form': filter_form,
        'api_response': json.dumps(response, indent=4, ensure_ascii=False)
    })
def download_file(request, file_path):
    public_key = request.session.get('public_key')  # используем request.session.get()
    if not public_key:
        return HttpResponseRedirect('/')

    api = YandexDiskAPI(public_key)
    try:
        download_link = api.get_download_link(file_path)
        response = requests.get(download_link)
        file_name = file_path.split('/')[-1]  # извлекаем имя файла
        response = HttpResponse(response.content, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    except requests.RequestException as e:
        return HttpResponse(f'Ошибка при скачивании файла с Яндекс.Диска: {str(e)}')



def download_files(request):
    if request.method == 'POST':
        file_paths = request.POST.getlist('file_paths')  # Получаем список путей к файлам
        zip_filename = 'files.zip'

        # Создание zip-архива
        from zipfile import ZipFile
        import os

        with ZipFile(zip_filename, 'w') as zip_file:
            api = YandexDiskAPI(request.session.get('public_key'))
            for path in file_paths:
                try:
                    # Скачиваем файл с Яндекс.Диска
                    response = api.get_files(path)  # Создайте метод get_file в YandexDiskAPI для загрузки файла
                    if response.ok:
                        zip_file.writestr(path.split('/')[-1], response.content)  # Добавляем файл в архив
                except requests.RequestException as e:
                    print(f'Ошибка при скачивании файла {path}: {str(e)}')

        # Возвращаем архив пользователю
        with open(zip_filename, 'rb') as zip_file:
            response = HttpResponse(zip_file.read(), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename={zip_filename}'
            os.remove(zip_filename)  # Удаляем файл после отправки
            return response

    return HttpResponse('Invalid request')