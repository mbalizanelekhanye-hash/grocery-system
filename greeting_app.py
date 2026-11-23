import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 32
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    name_field = ft.TextField(
        label="Your name",
        hint_text="Enter your name",
        width=320,
        autofocus=True,
    )
    greeting = ft.Text("", size=22, weight=ft.FontWeight.W_500)

    def greet(_):
        name = (name_field.value or "").strip()
        greeting.value = f"Hello, {name}!"
        page.update()

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Greeting App", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Enter your name and say hello.", size=15, color=ft.Colors.GREY_700),
                    name_field,
                    ft.ElevatedButton("Greet Me", on_click=greet),
                    greeting,
                ],
                spacing=18,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
            ),
            padding=32,
            border_radius=16,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(blur_radius=18, color=ft.Colors.BLACK12, offset=ft.Offset(0, 6)),
        )
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER, host="127.0.0.1", port=8550)

