import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(
            [
                ft.Icon(name=ft.icons.FOLDER_SPECIAL, color=ft.colors.PINK),
                ft.Icon(name=ft.icons.AUDIOTRACK, color=ft.colors.GREEN_400, size=30),
                ft.Icon(name=ft.icons.BEACH_ACCESS, color=ft.colors.BLUE, size=50),
                ft.Icon(name="settings", color="#c1c1c1"),

            ]
        )
    )

ft.app(target=main)
