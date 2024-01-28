import flet as ft

def main(page: ft.Page):
    # Crea una fila y una columna y las añade a la página
    page.add(
        ft.Row([ft.Text("Elemento 1"), ft.Text("Elemento 2"), ft.Text("Elemento 3")]),
        ft.Column([ft.Text("Elemento 4"), ft.Text("Elemento 5"), ft.Text("Elemento 6")])
    )

ft.app(target=main)
