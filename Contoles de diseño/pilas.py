import flet as ft

def main(page: ft.Page):
    # Crea una pila y la añade a la página
    page.add(
        ft.Stack([ft.Text("Elemento 1"), ft.Text("Elemento 2"), ft.Text("Elemento 3")])
    )

ft.app(target=main)
