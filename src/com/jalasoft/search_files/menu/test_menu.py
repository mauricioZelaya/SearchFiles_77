#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TkForm - Formularios en Tkinter con tk.Entry y ttk.Combobox

Copyleft 2014, Carlos Zayas Guggiari <carlos@zayas.org>
"""

import tkinter as tk
from tkinter import ttk


class Campo(object):
    """Clase para definir cada campo del formulario."""

    def __init__(self, padre, linea, etiqueta, tipo, valor, modo=False):
        self.padre = padre
        self.linea = linea
        self.etiqueta = etiqueta
        self.valor = tk.StringVar()
        self.etiqueta = tk.Label(padre, text=etiqueta)
        self.etiqueta.grid(column=0, row=linea)
        tipos = {'combobox': self.combobox,
                 'entry': self.entry}
        tipos[tipo](valor, modo)

    def entry(self, valor, modo=False):
        self.ent = tk.Entry(self.padre, textvariable=self.valor)
        self.valor.set(valor)
        self.ent.grid(column=1, row=self.linea)

    def combobox(self, valor, modo=False):
        estado = 'readonly' if modo else 'normal'
        self.box = ttk.Combobox(self.padre,
                                textvariable=self.valor,
                                state=estado)
        self.box['values'] = valor
        self.box.current(0)  # Selecciona el primer elemento de la tupla.
        self.box.bind("<<ComboboxSelected>>", self.combobox_elegir)
        self.box.grid(column=1, row=self.linea)

    def combobox_elegir(self, evento):
        self.valor.set(self.box.get())


class Formulario(object):
    """Clase para definir un conjunto de campos."""

    def __init__(self, padre, campos):
        self.padre = padre
        self.campos = {}
        self.guardar = False
        linea = 0
        for campo in campos:
            etiqueta, tipo, valor, modo = campo
            self.campos[etiqueta] = Campo(padre, linea,
                                          etiqueta, tipo, valor, modo)
            linea += 1
        self.btnacep = tk.Button(padre, text="Aceptar", command=self.aceptar)
        self.btncanc = tk.Button(padre, text="Cancelar", command=self.cancelar)
        self.btnacep.grid(column=1, row=linea, sticky='W')
        self.btncanc.grid(column=1, row=linea, sticky='E')

    def aceptar(self):
        self.guardar = True
        self.padre.destroy()

    def cancelar(self):
        self.padre.destroy()


if __name__ == '__main__':
    raiz = tk.Tk()
    form = Formulario(raiz, [
                             ["Nombre", "combobox", ['Juan', 'Luis', 'Pedro'],
                              False],
                             ["Direccion", "entry", "", False],
                             ["Tipo", "combobox", ['Casa', 'Trabajo', 'Movil'],
                              True],
                             ["Numero", "entry", "(595)", False]
                            ])
    raiz.mainloop()
    if form.guardar:
        for campo in form.campos:
            print(campo, form.campos[campo].valor.get())