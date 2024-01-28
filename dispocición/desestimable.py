import flet as ft

def main(page):
    page.window_height, page.window_width = 500, 400

    def close_yes_dlg(e):
        page.close_dialog()
        dlg.data.confirm_dismiss(True)

    def close_no_dlg(e):
        page.close_dialog()
        dlg.data.confirm_dismiss(False)

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete this item?"),
        actions=[
            ft.TextButton("Yes", on_click=close_yes_dlg),
            ft.TextButton("No", on_click=close_no_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    def handle_confirm_dismiss(e: ft.DismissibleDismissEvent):
        if e.direction == ft.DismissDirection.END_TO_START: # right-to-left slide
            # save current dismissible to dialog's data
            dlg.data = e.control
            page.show_dialog(dlg)
        else: # left-to-right slide
            e.control.confirm_dismiss(True)

    def handle_dismiss(e):
        lv.controls.remove(e.control)
        page.update()

    def handle_update(e: ft.DismissibleUpdateEvent):
        print(f"Update - direction: {e.direction}, progress: {e.progress}, reached: {e.reached}, previous_reached: {e.previous_reached}")

    page.add(
        lv := ft.ListView(
            controls=[
                ft.Dismissible(
                    content=ft.ListTile(title=ft.Text(f"Item {i}")),
                    dismiss_direction=ft.DismissDirection.HORIZONTAL,
                    background=ft.Container(bgcolor=ft.colors.GREEN),
                    secondary_background=ft.Container(bgcolor=ft.colors.RED),
                    on_dismiss=handle_dismiss,
                    on_update=handle_update,
                    on_confirm_dismiss=handle_confirm_dismiss,
                    dismiss_thresholds={
                        ft.DismissDirection.END_TO_START: 0.2,
                        ft.DismissDirection.START_TO_END: 0.2,
                    },
                )
                for i in range(10)
            ],
            expand=True,
        )
    )


ft.app(main)