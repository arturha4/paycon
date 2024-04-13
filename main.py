import sys
import time

import gi
import threading
from paycon_api import *
gi.require_version("Gtk", "3.0")
from gi.repository import GLib,Gtk, Gdk
from gi.repository import GObject



class MainWindow(Gtk.Window):

    def __init__(self):
        self.data_storage = []
        Gtk.Window.__init__(self, title="Main Window")
        self.set_default_size(800, 600)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)

    def create_buttons(self):
        button_api = Gtk.Button(label="Загрузить из API")
        button_csv = Gtk.Button(label="Загрузить из файла")
        button_api.connect("clicked", self.on_button_clicked)
        button_csv.connect("clicked", self.on_button_clicked)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box.pack_start(button_api, True, True, 50)
        box.pack_start(button_csv, True, True, 50)
        self.add(box)


    def api_task1(self):
        self.data_storage.append(get_api_data_names(paycon_url))

    def api_task2(self):
        self.data_storage.append(get_api_data_names(paycon_url2))

    def show_download_dialog(self):
        dialog = Gtk.Dialog('Download', None, modal=True, destroy_with_parent=True)
        spinner = Gtk.Spinner()
        dialog.vbox.pack_start(spinner, True, True, 0)
        dialog.show_all()
        spinner.start()
        spinner.show()
        dialog.run()
        return dialog

    def on_button_clicked(self, dialog):
        ## не отрисовывается анимация спинера
        thread_api1 = threading.Thread(target=self.api_task1)
        thread_api2 = threading.Thread(target=self.api_task2)
        thread_api1.start()
        thread_api2.start()
        dialog = Gtk.Dialog('Download', None, modal=True, destroy_with_parent=True)
        spinner = Gtk.Spinner()
        dialog.vbox.pack_start(spinner, True, True,0)
        dialog.show_all()
        thread_api1.join()
        thread_api2.join()
        # print(self.data_storage)
        dialog.hide()


win = MainWindow()
win.create_buttons()
win.show_all()
Gtk.main()