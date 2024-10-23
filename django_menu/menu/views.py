from django.shortcuts import render


def show_menu(request):
    render(request, 'menu/menu_template.html')
