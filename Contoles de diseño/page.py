import flet as ft

def main(page: ft.Page):
    # Configura la página
    page.title = "Mi página"
    page.add(ft.Text("¡Hola, mundo!"))

ft.app(target=main)
