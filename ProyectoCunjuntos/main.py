import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto conjuntos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
        primary=ft.colors.GREEN,
            primary_container=ft.colors.GREEN_200,
            secondary=ft.colors.BLUE,
            secondary_container=ft.colors.BLUE_200,
            background=ft.colors.WHITE,
            surface=ft.colors.GREY_50,
            error=ft.colors.RED,
            on_primary=ft.colors.WHITE,
            on_secondary=ft.colors.WHITE,
            on_background=ft.colors.BLACK,
            on_surface=ft.colors.BLACK,
            on_error=ft.colors.WHITE,
        ),
    )

    #App bar 
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor= "#81f4c3",
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(
                        text="Checked item",
                        checked=False,
                        on_click=None
                    ),
                ]
            ),
        ],
    )
    
    
    
    page.add(
        ft.Row(
            [
            ft.TextField(
                label = "Elementos de A",
                hint_text = "elemento1, elemento2, elemnto3",
                prefix_text= "A = {",
                suffix_text = "}",
                color = ft.colors.BLUE,
                border_color = ft.colors.WHITE,
                focused_border_color = ft.colors.BLUE,
                focused_bgcolor = ft.colors.WHITE
            ),
            ft.TextField(
                label = "Elementos de B",
                hint_text = "elemento1, elemento2, elemnto3",
                prefix_text= "B = {",
                suffix_text = "}",
                color = ft.colors.GREEN,
                border_color = ft.colors.WHITE,
                focused_border_color = ft.colors.GREEN,
                focused_bgcolor = ft.colors.WHITE
            )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.FilledButton(icon="SETTINGS_BACKUP_RESTORE", text = "Añadir")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
ft.app(target=main)
