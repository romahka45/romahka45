from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyGridlayout(Widget):


    def press(self, instance):
        Im=self.Im.text
        MercandBMW=self.MercandBMW.text
        rt=self.rt.text

        # print(f'Пиздец {ТЫ}, значет между {мерсилибеха}, а {Автор}')
        # Print it to the screen
        self.add_widget(Label(text=f'Хорошо я {rt}, значет между {MercandBMW}, а {Im}'))

        # Clear the input boxes
        self.Im.text = ""
        self.MercandBMW.text = ""
        self.rt.text = ""


class MyApp(App):
    def build(self):
        return MyGridlayout()


if __name__ == '__main__':
    MyApp().run()