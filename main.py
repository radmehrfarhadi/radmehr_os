import sys
import os
import builtins
import threading
import queue

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

BASE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.join(BASE, "radmehr_os")
ANDROID_MODULES = os.path.join(BASE, "android_modules")

# Android-specific compatibility modules must win over desktop modules.
if CORE not in sys.path:
    sys.path.insert(0, CORE)
if ANDROID_MODULES not in sys.path:
    sys.path.insert(0, ANDROID_MODULES)

os.chdir(BASE)


class TerminalIO:
    def __init__(self, app):
        self.app = app
        self.input_queue = queue.Queue()
        self.encoding = "utf-8"

    def write(self, text):
        if text:
            Clock.schedule_once(lambda dt: self.app.append_output(text), 0)
        return len(text) if text else 0

    def flush(self):
        pass

    def readline(self):
        return self.input_queue.get() + "\n"

    def reconfigure(self, **kwargs):
        return None


class RadmehrApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation="vertical", padding=10, spacing=8)

        self.output = Label(
            text="Radmehr OS starting...\n",
            size_hint_y=0.9,
            halign="left",
            valign="top",
        )
        self.output.bind(
            size=lambda instance, value: setattr(instance, "text_size", (value[0], None))
        )

        self.input_box = TextInput(
            multiline=False,
            size_hint_y=0.1,
            hint_text="Type here and press Enter",
        )
        self.input_box.bind(on_text_validate=self.send_input)

        self.root_layout.add_widget(self.output)
        self.root_layout.add_widget(self.input_box)
        Clock.schedule_once(self.start_radmehr, 0.5)
        return self.root_layout

    def append_output(self, text):
        self.output.text += str(text)

    def send_input(self, instance):
        value = instance.text
        instance.text = ""
        self.append_output(value + "\n")
        if hasattr(self, "terminal"):
            self.terminal.input_queue.put(value)

    def start_radmehr(self, dt):
        self.terminal = TerminalIO(self)
        sys.stdout = self.terminal
        sys.stderr = self.terminal
        builtins.input = self.android_input
        threading.Thread(target=self.run_core, daemon=True).start()

    def android_input(self, prompt=""):
        if prompt:
            print(prompt, end="")
        return self.terminal.input_queue.get()

    def run_core(self):
        try:
            import radmehr_os
            radmehr_os.main()
        except SystemExit:
            print("\nRadmehr OS exited.")
        except Exception:
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    RadmehrApp().run()
