import flet as ft
from controller import CalculatorController
from buttons import DigitButton, ActionButton, ExtraActionButton

def main(page: ft.Page):
    page.title = "Calc App"

    result = ft.Text(value="0", size=40, color=ft.Colors.WHITE)

    def update_result(new_text):
        result.value = new_text
        page.update()

    controller = CalculatorController(update_result)

    def on_button_click(e):
        controller.handle_input(e.control.text) 

    page.add(
        ft.Container(
            width=350,
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment="end"),
                    ft.Row(
                        controls=[
                            ExtraActionButton("AC", on_button_click),
                            ExtraActionButton(" ", on_button_click),
                            ExtraActionButton("%", on_button_click),
                            ActionButton("/", on_button_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("7", on_button_click),
                            DigitButton("8", on_button_click),
                            DigitButton("9", on_button_click),
                            ActionButton("*", on_button_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("4", on_button_click),
                            DigitButton("5", on_button_click),
                            DigitButton("6", on_button_click),
                            ActionButton("-", on_button_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("1", on_button_click),
                            DigitButton("2", on_button_click),
                            DigitButton("3", on_button_click),
                            ActionButton("+", on_button_click),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("0", on_button_click, expand=2),
                            DigitButton(".", on_button_click),
                            ActionButton("=", on_button_click),
                        ]
                    ),
                ]
            )
        )
    )

    update_result("0")

ft.app(target=main)
