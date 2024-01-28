import flet as ft

def main(page: ft.Page):
    # Añade todos los iconos disponibles a la página
    for icon_name in dir(ft.icons):
        # Filtra los atributos especiales de Python
        if not icon_name.startswith("__"):
            page.add(ft.Icon(name=icon_name))

ft.app(target=main)
