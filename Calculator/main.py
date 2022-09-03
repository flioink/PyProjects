from kivy.app import App

from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
import  re

Window.size = (500, 700)
Builder.load_file("Calculator.kv")

class CalculatorWidget(Widget):

    def clear(self):
        self.ids.inputBox.text = "0"

    def buttonValue(self, number):
        prevNumber = self.ids.inputBox.text


        if "Err: x / 0" in prevNumber:
            prevNumber = ""
            self.ids.inputBox.text = number.text

        elif prevNumber == "0":
            self.ids.inputBox.text = ""
            self.ids.inputBox.text = number.text
        else:
            self.ids.inputBox.text = prevNumber + number.text

    def signs(self, sign):
        prevNumber = self.ids.inputBox.text
        self.ids.inputBox.text = prevNumber + sign.text

    def removeLast(self):
        prevNumber = self.ids.inputBox.text
        prevNumber = prevNumber[:-1]
        self.ids.inputBox.text = prevNumber
    def results(self):
        prevNumber = self.ids.inputBox.text
        try:
            result = eval(prevNumber)
            self.ids.inputBox.text = str(result)
        except:
            self.ids.inputBox.text = "Err: x / 0"

    def posNeg(self):
        prevNumber = self.ids.inputBox.text
        if "-" in prevNumber:
            self.ids.inputBox.text = f"{prevNumber.replace('-', '')}"
        else:
            self.ids.inputBox.text = f"-{prevNumber}"

    def dot(self):
        prevNumber = self.ids.inputBox.text
        numList = re.split("\+|\*|-|/|%", prevNumber)

        if ("+" in prevNumber or "-" in prevNumber or "*" in prevNumber or "%" in prevNumber)\
                and "." not in numList[-1]:
            prevNumber = f"{prevNumber}."
            self.ids.inputBox.text = prevNumber

        elif "." in prevNumber:
            pass
        else:
            prevNumber = f"{prevNumber}."
            self.ids.inputBox.text = prevNumber




class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == '__main__':
    CalculatorApp().run()
