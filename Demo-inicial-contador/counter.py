import flet
from flet import IconButton, Page, Row, TextField,icons

def main(page: Page):
    page.title = "Ejemplo de contador de flet"
    page.vertical_alignment = "center" #La pagina se aliena verticalmete

    txt_number = TextField