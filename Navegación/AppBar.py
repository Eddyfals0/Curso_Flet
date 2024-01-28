# Importa la biblioteca flet y la renombra como ft para su uso en el código.
import flet as ft

# Define la función principal que se ejecutará cuando se inicie la aplicación.
def main(page: ft.Page):
    # Define una función anidada que se ejecutará cuando se haga clic en un elemento del menú.
    def check_item_clicked(e):
        # Cambia el estado de "checked" del elemento del menú al que se hizo clic.
        e.control.checked = not e.control.checked
        # Actualiza la página para reflejar los cambios realizados.
        page.update()

    # Configura la barra de aplicaciones de la página.
    page.appbar = ft.AppBar(
        # Establece el icono principal de la barra de aplicaciones.
        leading=ft.Icon(ft.icons.PALETTE),
        # Establece el ancho del icono principal.
        leading_width=40,
        # Establece el título de la barra de aplicaciones.
        title=ft.Text("Ania"),
        # Establece que el título no esté centrado.
        center_title=False,
        # Establece el color de fondo de la barra de aplicaciones.
        bgcolor=ft.colors.SURFACE_VARIANT,
        # Establece las acciones de la barra de aplicaciones.
        actions=[
            # Añade un botón de icono a la barra de aplicaciones.
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            # Añade otro botón de icono a la barra de aplicaciones.
            ft.IconButton(ft.icons.FILTER_3),
            # Añade un botón de menú emergente a la barra de aplicaciones.
            ft.PopupMenuButton(
                # Establece los elementos del menú emergente.
                items=[
                    # Añade un elemento al menú emergente.
                    ft.PopupMenuItem(text="Item 1"),
                    # Añade un divisor al menú emergente.
                    ft.PopupMenuItem(),  # divider
                    # Añade un elemento verificable al menú emergente.
                    ft.PopupMenuItem(
                        # Establece el texto del elemento verificable.
                        text="Checked item",
                        # Establece que el elemento verificable no esté marcado inicialmente.
                        checked=False,
                        # Establece la función que se ejecutará cuando se haga clic en el elemento verificable.
                        on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    # Añade un texto al cuerpo de la página.
    page.add(ft.Text("Body!"))

# Inicia la aplicación con la función principal como objetivo.
ft.app(target=main)