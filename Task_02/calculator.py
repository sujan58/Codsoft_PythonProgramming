from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle


class CalculatorApp(App):
    def build(self):
        self.expression = ""

        layout = BoxLayout(orientation='vertical', spacing=10)

        # Rectangle box for result display
        with layout.canvas.before:
            Color(0, 0, 1, 1)  # Blue color
            self.rect = Rectangle(size=(100, 100), pos=(0, 0))  # Initial position and size

        # Display label inside the rectangle box
        self.display = Label(text="", font_size='24sp', size_hint=(1, 0.25), halign='right', valign='middle')
        layout.add_widget(self.display)

        # Grid layout for buttons
        buttons_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.75))
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for button in buttons:
            if button == '=':
                equals_btn = Button(text=button, background_color=(0, 0, 1, 1))  # Blue button color
                equals_btn.bind(on_press=self.calculate)
                buttons_layout.add_widget(equals_btn)
            elif button == 'C':
                clear_btn = Button(text=button, background_color=(0, 0, 1, 1))  # Blue button color
                clear_btn.bind(on_press=self.clear)
                buttons_layout.add_widget(clear_btn)
            else:
                btn = Button(text=button, background_color=(0, 0, 1, 1))  # Blue button color
                btn.bind(on_press=self.on_button_press)
                buttons_layout.add_widget(btn)

        layout.add_widget(buttons_layout)

        return layout

    def on_button_press(self, instance):
        if instance.text == 'C':
            self.expression = ''
        else:
            self.expression += instance.text
        self.update_display(instance.text)

    def calculate(self, instance):
        try:
            self.expression = str(eval(self.expression))
            self.update_display('=')
        except Exception as e:
            self.expression = 'Error'
            self.update_display('=')

    def clear(self, instance):
        self.expression = ''
        self.update_display('C')

    def update_display(self, text):
        if text == '=':
            self.display.text = self.expression
        elif text == 'C':
            self.display.text = ''
        else:
            self.display.text += text


if __name__ == '__main__':
    CalculatorApp().run()
