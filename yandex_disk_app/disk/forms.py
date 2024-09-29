from django import forms

class FileFilterForm(forms.Form):
    FILE_TYPES = [
        ('all', 'Все'),
        ('image', 'Изображения'),
        ('document', 'Документы'),
        ('video', 'Видео'),
    ]
    file_type = forms.ChoiceField(choices=FILE_TYPES, initial='all', label='Тип файла')