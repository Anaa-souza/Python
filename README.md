
# 💜 Meu Appzinho Flet

> Atividades práticas de **Programação Mobile utilizando Python e Flet**, desenvolvidas durante as aulas.

Este projeto reúne algumas atividades desenvolvidas durante as aulas de Programação Mobile. Os exercícios foram realizados utilizando **Python** e a biblioteca **Flet**, com o objetivo de praticar a criação de interfaces e a interação com o usuário.

Ao longo das atividades, foram utilizados diferentes componentes do Flet, como textos, campos de entrada, ícones, botões, caixas de seleção e containers.

---

## 🛠️ Tecnologias utilizadas

- 🐍 Python
- 💜 Flet
- 💻 Visual Studio Code

---

## 📱 Atividades desenvolvidas

### 1. Tela de apresentação

A primeira atividade consiste na criação de uma tela simples de apresentação, contendo um nome e um subtítulo.

O objetivo foi praticar a criação de textos, o alinhamento dos componentes e a organização dos elementos na tela.

#### 💻 Código

```python
import flet as ft

def main(page: ft.Page):

    page.title = "MEU APPZINHO FLET"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.bgcolor = "Purple"

    # criando os itens da pagina

    titulo = ft.Text("Ana Carolina", size=32)

    subtitulo = ft.Text(
        "Estudante de programação mobile!",
        size=18
    )

    page.add(
        ft.Column(
            [titulo, subtitulo],
            width=320,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.run(main)
```

#### 📌 Explicação

O `ft.Text()` é utilizado para criar os textos que aparecem na tela.

Os componentes `titulo` e `subtitulo` são colocados dentro de uma `Column`, fazendo com que fiquem organizados verticalmente, um abaixo do outro.

O `width=320` define a largura da área utilizada pelos elementos, enquanto `horizontal_alignment` mantém o conteúdo centralizado.

---

### 2. Cartão de apresentação

Na segunda atividade, a tela de apresentação foi aprimorada com informações de contato.

Além do nome e do subtítulo, foram adicionados um e-mail e um número de telefone acompanhados de seus respectivos ícones.

As informações foram agrupadas dentro de um `Container`, criando um pequeno cartão de apresentação.

#### 💻 Código

```python
import flet as ft

def main(page: ft.Page):

    page.title = "MEU APPZINHO FLET"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = "Purple"

    # criando os itens da pagina

    titulo = ft.Text("Ana Carolina", size=32)

    subtitulo = ft.Text("Estudante de programação mobile!", size=18)

    email = ft.Row([
        ft.Icon(ft.Icons.EMAIL),
        ft.Text("ana@email.com")
    ])

    telefone = ft.Row([
        ft.Icon(ft.Icons.PHONE),
        ft.Text("(11) 98765-4321")
    ])

    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                subtitulo,
                email,
                telefone
            ]),
            width=320,
            padding=20,
            bgcolor="#4A126B",
            border_radius=15
        )
    )

ft.run(main)
```

#### 📌 Explicação

O `ft.Container()` foi utilizado para criar o cartão que reúne todas as informações.

O nome e o subtítulo são criados utilizando `ft.Text()`.

Para o e-mail e o telefone, foram utilizados `ft.Icon()` e `ft.Text()` dentro de `ft.Row()`. Dessa forma, cada ícone fica ao lado da sua respectiva informação.

A propriedade `padding` cria um espaçamento interno no cartão, enquanto `border_radius` deixa os cantos arredondados.

---

### 3. Campo de nome, Checkbox e mensagem

Na terceira atividade, foi criado um pequeno formulário para interação com o usuário.

O usuário pode digitar seu nome, marcar a opção **"Aceito os termos"** e clicar no botão **"Enviar"**.

Depois do envio, o programa verifica se os termos foram aceitos e retorna uma mensagem personalizada utilizando o nome digitado.

#### 💻 Código

```python
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
```

#### 📌 Explicação

O `ft.TextField()` cria o campo onde o usuário pode digitar seu nome.

O `ft.Checkbox()` cria a opção para aceitar os termos.

O `ft.ElevatedButton()` cria o botão de envio. Quando ele é pressionado, a função `enviar()` é executada.

Dentro da função, o programa verifica se o Checkbox está marcado.

Caso esteja marcado, o nome digitado é utilizado para criar uma mensagem personalizada:

> **Obrigada, Ana Carolina!**

Caso os termos não sejam aceitos, o programa retorna:

> **Aceite os termos para continuar.**

O `page.update()` é utilizado para atualizar a tela depois que o valor da mensagem é alterado.

---

## 📚 Componentes utilizados

Durante as atividades, foram utilizados diferentes componentes e recursos do Flet:

| Componente | Função |
|---|---|
| `ft.Text` | Exibir textos |
| `ft.TextField` | Permitir a entrada de texto |
| `ft.Icon` | Exibir ícones |
| `ft.Row` | Organizar elementos lado a lado |
| `ft.Column` | Organizar elementos verticalmente |
| `ft.Container` | Agrupar e organizar componentes |
| `ft.Checkbox` | Criar uma opção de seleção |
| `ft.ElevatedButton` | Criar um botão |
| `page.update()` | Atualizar a interface após uma ação |
| `ft.run(main)` | Executar a aplicação |

---

## 🎯 Objetivo das atividades

As atividades tiveram como objetivo praticar os conceitos básicos de desenvolvimento de interfaces utilizando **Python e Flet**.

A partir dos exercícios, foi possível aprender a criar componentes visuais, organizar elementos na tela, trabalhar com campos de entrada e desenvolver pequenas interações com o usuário.

As atividades também mostraram como uma interface pode ser construída de forma gradual, começando com elementos simples e adicionando novos componentes e funcionalidades.

---

## 🖼️ Resultados

Os prints das telas desenvolvidas durante as atividades serão disponibilizados separadamente junto aos arquivos do projeto.

Eles apresentam a evolução das interfaces desenvolvidas durante os exercícios.

---

## 👩‍💻 Autora

**Ana Carolina**

Estudante de Desenvolvimento de Sistemas.

---

> Projeto desenvolvido para fins acadêmicos e de aprendizado.
````
