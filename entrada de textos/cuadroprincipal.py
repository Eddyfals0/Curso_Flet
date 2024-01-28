import flet as ft

def main(page: ft.Page):
    page.window_height, page.window_width = 300, 400
    
    # Crea cuadros de texto de entrada con prefijos y/o sufijos y los añade a la página
    page.add(
        ft.TextField(label="Con prefijo", prefix_text="https://"),
        ft.TextField(label="Con sufijo", suffix_text=".com"),
        ft.TextField(label="Con prefijo y sufijo", prefix_text="https://", suffix_text=".com"),
        ft.TextField(label ="vacio")
    )

ft.app(target=main)
