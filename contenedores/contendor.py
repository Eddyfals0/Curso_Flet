import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto conjuntos"
    
    # Centra los controles en la página
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Crea un contenedor con un gradiente de color
    gradient_container = ft.Container(
    content=ft.Column( 
        [
            ft.Row(
                [
                    ft.Text(
                        "SETS",
                        size=50,  # Cambia el tamaño del texto a 30
                        color="#b8fadd",  # Cambia el color del texto a rojo
                        font_family="Arial",  # Cambia la fuente del texto a Arial
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(
                        "By EDDY",
                        size=12,  # Cambia el tamaño del texto a 30
                        color="#9f75ff",
                        font_family="Arial",  # Cambia la fuente del texto a Arial
                        weight=ft.FontWeight.BOLD
                    )

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.TextField(
                        label = "Elementos de A",
                        hint_text = "elemento1, elemento2, elemnto3",
                        prefix_text= "A = {",
                        suffix_text = "}",
                        color = ft.colors.BLUE,
                        border_color = "#9f75ff",
                        focused_border_color = ft.colors.BLUE,
                        focused_bgcolor = ft.colors.WHITE
                    ),
                    ft.TextField(
                        label = "Elementos de B",
                        hint_text = "elemento1, elemento2, elemnto3",
                        prefix_text= "B = {",
                        suffix_text = "}",
                        color = ft.colors.GREEN,
                        border_color = "#9f75ff",
                        focused_border_color = ft.colors.GREEN,
                        focused_bgcolor = ft.colors.WHITE
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.FilledButton(icon="SETTINGS_BACKUP_RESTORE", text = "Actualizar")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    ),
    #bgcolor = "#6b04fd",
    border_radius=10,
    width=650,
    height=250,
    gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#6b04fd", "#2c0076"],
        ),
    )

    
    page.add(
        ft.Row(
            [
                gradient_container
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),

    )

ft.app(target=main)
