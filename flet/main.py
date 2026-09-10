import flet as ft

def main(page: ft.Page):

    page.title = "MEU APPZINHO FLET"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = "Purple"

    # criando os itens da pagina

    nome = ft.TextField(
        label="Digite seu nome",
        width=320
    )

    mensagem = ft.Text("")

    def enviar(e):
        if checkbox.value:
            mensagem.value = f"Obrigada, {nome.value}!"
        else:
            mensagem.value = "Aceite os termos para continuar."
        page.update()

    checkbox = ft.Checkbox(
        label="Aceito os termos"
    )

    botao = ft.ElevatedButton(
        "Enviar",
        on_click=enviar
    )

    page.add(
        ft.Column(
            [
                nome,
                checkbox,
                botao,
                mensagem
            ],
            width=320,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.run(main)