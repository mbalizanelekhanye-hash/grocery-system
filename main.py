import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 32

    # Keep the entered name here so both routes can use it.
    name = ""
    name_field = ft.TextField(
        label="Your name",
        hint_text="Enter your name",
        width=320,
        autofocus=True,
    )

    def route_change(_=None):
        page.views.clear()

        page.views.append(
            ft.View(
                route="/",
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text("Welcome!", size=32, weight=ft.FontWeight.BOLD),
                            ft.Text("Enter your name to continue.", size=16),
                            name_field,
                            ft.Button(content="Continue", on_click=continue_to_greeting),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=18,
                        tight=True,
                    )
                ],
            )
        )

        if page.route == "/greeting":
            page.views.append(
                ft.View(
                    route="/greeting",
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(f"Hello, {name}!", size=32, weight=ft.FontWeight.BOLD),
                                ft.Button(content="Back", on_click=back_home),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20,
                            tight=True,
                        )
                    ],
                )
            )

        page.update()

    async def continue_to_greeting(_):
        nonlocal name
        name = (name_field.value or "").strip()
        if not name:
            page.show_dialog(
                ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Name required"),
                    content=ft.Text("Please enter your name before continuing."),
                    actions=[
                        ft.Button(
                            content="OK",
                            on_click=lambda _: page.pop_dialog(),
                        )
                    ],
                )
            )
            return

        await page.push_route("/greeting")

    async def back_home(_):
        await page.push_route("/")

    page.on_route_change = route_change
    route_change()


if __name__ == "__main__":
    ft.run(main)
