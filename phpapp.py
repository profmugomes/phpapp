#!/bin/python3

# phpapp
# Author Murilo Gomes <contatoprofmugomes@gmail.com>
# Copyright (c) 2023 Murilo Gomes
# License GPL-2.0
# Version 1.0.0, 2023-02-20

import gi
import socket
from subprocess import Popen

gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, WebKit2

# Obtém um número de porta que não está sendo usada
portNumber = socket.socket()
portNumber.bind(('', 0))
lh_port = portNumber.getsockname()[1]

# Inicia o servidor embutido do PHP
lh_php = Popen(['php', '-S', 'localhost:{}'.format(lh_port), '-t', 'www/'], stdin=None, stdout=None, stderr=None, close_fds=True)

def on_destroy(widget):
    # Fecha o processo do servidor embutido do PHP
    lh_php.kill()

# Cria a janela
window = Gtk.Window()
window.set_default_size(800, 600)

# Ativa a função destroy
window.connect("destroy", Gtk.main_quit)

# Adiciona o painel da janela
scrolled_window = Gtk.ScrolledWindow()
scrolled_window.connect("destroy", on_destroy)

# Chama o controle do WebView do WebKit2
webview = WebKit2.WebView()
webview.load_uri("http://localhost:{}".format(lh_port))

# Adiciona o webview no painel da janela
scrolled_window.add(webview)

# Adiciona o painel na janela
window.add(scrolled_window)

# Exibe a janela
window.show_all()
Gtk.main()
