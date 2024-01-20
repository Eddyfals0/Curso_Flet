import flet as ft

def main(page: ft.Page):
    page.title = 'My First Page'
    page.horizontal_alignment = "center"

    txt_number = ft.TextField(value = 0, text_align = "right", width = 100)

    def minus_click(event):
        txt_number.value = int(txt_number.value) - 1

    def plus_click(event):
        txt_number.value = int(txt_number.value) + 1

    page.add(
        Row([
            ft.IconButton(ft.icons.REMONVE, on_click=minus_click)

        ]
        )
    )