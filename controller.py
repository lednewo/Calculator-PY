class CalculatorController:
    def __init__(self, on_update):
        self.expression = ""
        self.on_update = on_update 

    def handle_input(self, text):
        if text == "AC":
            self.expression = ""
        elif text == "=":
            self.calculate_result()
        elif text == "%":
            self.percent()
        elif text.strip() == "":
            return
        else:
            self.expression += text

        self.on_update(self.expression or "0")

    def calculate_result(self):
        try:
            self.expression = str(eval(self.expression))
        except:
            self.expression = "Erro"

    def percent(self):
        try:
            self.expression = str(eval(self.expression) / 100)
        except:
            self.expression = "Erro"
