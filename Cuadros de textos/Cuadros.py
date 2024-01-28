import flet as ft

def main(page: ft.Page):
    
    Columna1 = ft.Column(
        [
            ft.TextField( 
                label = "Columna1"
            ),
            ft.TextField(
                label = "",
                color = ft.colors.AMBER
                
            )
        ]
    )
    
    Columna2 = ft.Column(
        [
            ft.TextField(
                label = "Columna2"
            ),
            ft.TextField()
        ]
    )

    Columna2 = ft.Column(
        [
            ft.TextField(
                label = "Columna3"
            ),
            ft.TextField()
        ]
    )
    
    page.add(
        ft.Row(
            [
                Columna1,
                Columna2
            ]
        )
    )

ft.app(target = main)