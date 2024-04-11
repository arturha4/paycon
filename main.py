import sys

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib,Gtk


class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyGtkApplication")
        GLib.set_application_name('My Gtk Application')

    def do_activate(self):
        self.window = Gtk.ApplicationWindow(application=self, title="Main window")
        self.window.resize(800, 600)
        self.window.present()
        button_api = Gtk.Button.new_with_label('Загрузить из API')
        button_csv = Gtk.Button.new_with_label('Загрузить из файла')
        self.window.add(button_api)
        # self.window.add(button_csv)

#
# app = MyApplication()
# exit_status = app.run(sys.argv)
# sys.exit(exit_status)


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Main Window")
        self.set_default_size(800, 600)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)

    def create_buttons(self):
        button_api = Gtk.Button(label="Загрузить из API")
        button_csv = Gtk.Button(label="Загрузить из файла")
        button_api.connect("clicked", self.on_button_clicked)
        button_csv.connect("clicked", self.on_button_clicked)

        self.add(button_api)
        self.add(button_csv)

    def on_button_clicked(self, widget):
        print("Button clicked!")

win = MainWindow()
win.create_buttons()
win.show_all()
Gtk.main()
