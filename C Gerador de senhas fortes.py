import PySimpleGUI as sg
import string
import random
import pyperclip

def gerar_senha(tamanho):
    elementos_obrigatorios = [
        random.choice(string.digits),
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.punctuation)
    ]

    possibilidades = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    restante_senha = random.choices(possibilidades, k=tamanho-4)
    elementos_obrigatorios.extend(restante_senha)
    random.shuffle(elementos_obrigatorios)
    senha = "".join(elementos_obrigatorios)
    return senha

layout = [
    [sg.Text("Digite o tamanho da senha:")],
    [sg.Input(key='tamanho', size=(20, 1), focus=True)],
    [sg.Button("Gerar Senha", key='botao_gerar')],
    [sg.Text("", size=(40, 1), key='resultado')],
    [sg.Button("Copiar Senha", key='botao_copiar')]
]

janela = sg.Window("Gerador de Senhas Fortes", layout, return_keyboard_events=True)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break

    if event in ("botao_gerar", '\r'):
        try:
            tamanho = int(values['tamanho'])
            if tamanho < 5:
                sg.popup("Aviso", "O tamanho da senha deve ser de pelo menos 5 caracteres.")
            else:
                senha = gerar_senha(tamanho)
                janela['resultado'].update(f"Sua senha é: {senha}")
                janela['botao_gerar'].update(text="Gerar Outra Senha")
        except ValueError:
            sg.popup("Erro", "Por favor, insira um número válido para o tamanho da senha.")
    if event in ("botao_copiar"):
        senha = janela['resultado'].get().replace("Sua senha é: ", "")
        if senha:
            pyperclip.copy(senha)
            sg.popup("Copiado", "A senha foi copiada para a área de transferência.")

janela.close()
