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
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.box.pack_start(button_api, True, True, 50)
        self.box.pack_start(button_csv, True, True, 50)
        self.add(self.box)


    def api_task1(self):
        self.data_storage.extend(get_api_data_names(paycon_url))

    def api_task2(self):
        self.data_storage.extend(get_api_data_names(paycon_url2))

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
        dialog.hide()
        self.remove_old_box()
        self.add_new_box_with_treeview()

    def create_tree_view(self):
        products_store_list = Gtk.ListStore(int,str)
        for inx, item in enumerate(self.data_storage):
            products_store_list.append([inx, item])
        products_tree_view = Gtk.TreeView(products_store_list)
        for i, column_title in enumerate([" ", "Title"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            products_tree_view.append_column(column)
        return products_tree_view
        # self.remove(self.box)
        # self.prodcuts_tree_view_box = Gtk.Box()
        # self.prodcuts_tree_view_box.pack_start(products_tree_view, True, True,0)
        # self.show_all()

    def remove_old_box(self):
        # Assuming the old box is called oldBox
        oldBox = self.get_child()
        self.remove(oldBox)

    def add_new_box_with_treeview(self):
        # Create a new box containing a TreeView
        self.box = Gtk.HPaned()
        treeview = self.create_tree_view()
        # self.box.pack_start(treeview, True, True, 0)
        self.box.add(treeview)

        # Add the new Box to the mainWindow
        self.add(self.box)
        self.box.show_all()


win = MainWindow()
win.create_buttons()
win.show_all()
Gtk.main()