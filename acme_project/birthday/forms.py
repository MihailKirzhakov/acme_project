# birthday/forms.py
from django import forms

# Импортируем класс модели Birthday.
from .models import Birthday
from .validators import real_age


# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.

    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = "__all__"
        widgets = {"birthday": forms.DateInput(attrs={"type": "date"})}
        validators = (real_age,)

        def clean_first_name(self):
            # Получаем значение имени из словаря очищенных данных.
            first_name = self.cleaned_data['first_name']
            # Разбиваем полученную строку по пробелам
            # и возвращаем только первое имя.
            return first_name.split()[0]
