import flet
from flet import IconButton, Page, Row, TextField, icons, Text, Page, Column, TextField, ElevatedButton, app


def main(page: Page):
    page.title = "Ejemplo de contador de flet"
    page.horizontal_alignment = "center"  # La pagina se aliena verticalmete
    page.window_width = 400
    page.window_height = 200

    t = Text(value="Hello, world!", color="green")
    txt_number = TextField(value="0", text_align='right', width=100)

    def minus_click(event):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(event):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    page.add(
        Row(
            [
                t,
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click)
            ],
            alignment="center"
        )
    )


flet.app(target=main)
