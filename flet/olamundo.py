import flet as ft

def main (pagina: ft.Page):
    pagina.title = "Olá Ana 😜" 
    pagina.add(ft.Text("Olá Ana 😜"))

#ft.run(main, view=ft.AppView.WEB_BROWSER)
ft.run(main)