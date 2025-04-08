import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, on_click, expand=1):
        super().__init__(text=text, expand=expand, on_click=on_click)

class DigitButton(CalcButton):
    def __init__(self, text, on_click, expand=1):
        super().__init__(text=text, on_click=on_click, expand=expand)
        self.bgcolor = ft.Colors.WHITE24
        self.color = ft.Colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text, on_click):
        super().__init__(text=text, on_click=on_click)
        self.bgcolor = ft.Colors.ORANGE
        self.color = ft.Colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text, on_click):
        super().__init__(text=text, on_click=on_click)
        self.bgcolor = ft.Colors.BLUE_GREY_100
        self.color = ft.Colors.BLACK
