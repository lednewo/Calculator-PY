import flet as ft

def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 600
    page.window.resizable = False
    page.title = "Calc App"

    expression = ""

    result = ft.Text(value="0", size=40, color=ft.Colors.WHITE)

    def update_result():
        result.value = expression or "0"
        page.update()

    
    def button_click(e):
        nonlocal expression
        text = e.control.text

        if text == "AC":
            expression = "0"
        elif text == "=":
            try:
                expression = str(eval(expression))
            except:
                expression = "Erro"
        elif text == "%":
            try:
                expression = str(eval(expression) / 100)
            except:
                expression = "Erro"
        else:
            expression += text

        update_result()

    
    class CalcButton(ft.ElevatedButton):
        def __init__(self, text, expand=1):
            super().__init__(text=text, expand=expand, on_click=button_click)

    class DigitButton(CalcButton):
        def __init__(self, text, expand=1):
            super().__init__(text=text, expand=expand)
            self.bgcolor = ft.Colors.WHITE24
            self.color = ft.Colors.WHITE

    class ActionButton(CalcButton):
        def __init__(self, text):
            super().__init__(text=text)
            self.bgcolor = ft.Colors.ORANGE
            self.color = ft.Colors.WHITE

    class ExtraActionButton(CalcButton):
        def __init__(self, text):
            super().__init__(text=text)
            self.bgcolor = ft.Colors.BLUE_GREY_100
            self.color = ft.Colors.BLACK

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
                            ExtraActionButton(text="AC"),
                            ExtraActionButton(text=" "),
                            ExtraActionButton(text="%"),
                            ActionButton(text="/"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="7"),
                            DigitButton(text="8"),
                            DigitButton(text="9"),
                            ActionButton(text="*"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="4"),
                            DigitButton(text="5"),
                            DigitButton(text="6"),
                            ActionButton(text="-"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="1"),
                            DigitButton(text="2"),
                            DigitButton(text="3"),
                            ActionButton(text="+"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(text="0", expand=2),
                            DigitButton(text="."),
                            ActionButton(text="="),
                        ]
                    ),
                ]
            )
        )
    )

    update_result()

ft.app(target=main)
