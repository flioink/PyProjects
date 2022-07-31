# original design by LeMaster Tech

import math
from functools import partial
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class OhmsLawInputScreen(GridLayout):
    def __init__(self, **kwargs):
        super(OhmsLawInputScreen, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 10
        title = Label(text= "Ohm's law solver!", font_size="32sp", color=(1, 0.8, 0), bold=True, size_hint=(1, 0.5))
        self.add_widget(title)
        instructions = Label(text="Enter known values (minimum 2): ", font_size="20sp", bold=True, size_hint=(1, 0.5))
        self.add_widget(instructions)
        self.voltage = LabelAndInput("Volatage (V - volts)", (1, 0, 0))
        self.current = LabelAndInput("Current (I - amps)", (0, 1, 0))
        self.resistance = LabelAndInput("Resistance (R - ohms)", (0.5, 0.5, 0.5))
        self.power = LabelAndInput("Power (P - watts)", (1, 0, 1))
        self.add_widget(self.voltage)
        self.add_widget(self.current)
        self.add_widget(self.resistance)
        self.add_widget(self.power)
        self.buttons = ButtonBox()
        self.buttons.solveV.bind(on_press=partial(self.solve, "v"))
        self.buttons.solveI.bind(on_press=partial(self.solve, "i"))
        self.buttons.solveR.bind(on_press=partial(self.solve, "r"))
        self.buttons.solveP.bind(on_press=partial(self.solve, "p"))
        self.add_widget(self.buttons)
        self.answer = Label(text="Answer", bold=True, size_hint=(1, 0.5))
        self.formula = Label(text="Formula: ", bold=True, size_hint=(1, 0.5))
        self.add_widget(self.answer)
        self.add_widget(self.formula)

    def solve(self, target, button):
        values = [0, 0, 0, 0]
        if self.voltage.input.text != "":
            values[0] = float(self.voltage.input.text)
        if self.current.input.text != "":
            values[1] = float(self.current.input.text)
        if self.resistance.input.text != "":
            values[2] = float(self.resistance.input.text)
        if self.power.input.text != "":
            values[3] = float(self.power.input.text)

        v = values[0]
        i = values[1]
        r = values[2]
        p = values[3]

        # Target is Voltage
        if target == "v":
            if v != 0:
                work = "v = v"

            elif i != 0:
                if r != 0:
                    v = i*r
                    work = "v = i * r"
                elif p != 0:
                    v = i/p
                    work = "v = i/p"

            elif p != 0 and r != 0:
                v = math.sqrt(p*r)
                work = "v = sqrt(p*r)"
            else:
                v = "invalid input"

            # answer  rounded string
            answer = f"Voltage is: {round(v, 4)} volts"

        # Target is Current
        elif target == "i":
            if i != 0:
                work = "i = i"

            elif v != 0:
                if r != 0:
                    i = v/r
                    work = "i = v / r"
                elif p != 0:
                    i = p/v
                    work = "i = p/v"

            elif p != 0 and r != 0:
                i = math.sqrt(p) /r
                work = "i = sqrt(p) /r"
            else:
                i = "invalid input"

            # answer  rounded string
            answer = f"Current is: {round(i, 4)} amps"

        # Target is Resistance
        elif target == "r":
            if r != 0:
                work = "r = r"

            elif i != 0:
                if v != 0:
                    r = v / i
                    work = "r = v / i"
                elif p != 0:
                    r = p / i**2
                    work = "r = p / i^2"

            elif p != 0 and v != 0:
                r = v**2 / p
                work = "r = v^2 / p"
            else:
                r = "invalid input"

            # answer  rounded string
            answer = f"Resistance is: {round(r, 4)} ohms"

        # Target is Power
        elif target == "p":
            if p != 0:
                work = "p = p"

            elif v != 0:
                if r != 0:
                    p = v**2 / r
                    work = "p = v^2 / r"
                elif i != 0:
                    p = v * i
                    work = "p = v * i"

            elif i != 0 and r != 0:
                p = i**2 * r
                work = "p = i^2 * r"
            else:
                r = "invalid input"

            # answer  rounded string
            answer = f"Power is: {round(p, 4)} watts"


        #displayed stuff
        self.answer.text = answer
        self.formula.text = work





class ButtonBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ButtonBox, self).__init__(**kwargs)
        self.cols = 4
        self.rows = 1
        self.solveV = Button(text="Solve V", color=(1, 0, 0))
        self.solveI = Button(text="Solve I", color=(0, 1, 0))
        self.solveR = Button(text="Solve R", color=(0.5, 0.5, 0.5))
        self.solveP = Button(text="Solve P", color=(1, 0, 1))
        self.add_widget(self.solveV)
        self.add_widget(self.solveI)
        self.add_widget(self.solveR)
        self.add_widget(self.solveP)


class LabelAndInput(BoxLayout):
    def __init__(self, input_text=None, input_color=(0, 0, 0), **kwargs):
        super(LabelAndInput, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 1
        self.value = Label(text=input_text, color=input_color, bold=True, size_hint=(0.4, 1))
        self.add_widget(self.value)
        self.input = TextInput(multiline=False, size_hint=(0.6, 1))
        self.add_widget(self.input)


class OhmsLawApp(App):

    def build(self):
        return OhmsLawInputScreen()


if __name__ == "__main__":
    OhmsLawApp().run()