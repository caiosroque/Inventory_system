import PySimpleGUI as sg
from SCRPT_BD import insert
from SCRPT_BD import data
from SCRPT_BD import cursor


sg.theme('DarkAmber')   # Tema

layout = [  [sg.Text('Nome'), sg.Input(key="inpt_produto")],
            [sg.Text('Código'), sg.Input(key="inpt_codigo")],
            [sg.Text('Data'), sg.Input(key="inpt_data")],
            [sg.Text('Quantidade'), sg.Input(key="inpt_quantidade")],
            [sg.Button('Adicionar'), sg.Button('Cancel')],
            [sg.Table(values=data, headings=cursor.description, display_row_numbers=False, auto_size_columns=True, num_rows=min(25, len(data)))],
]
# Criar a janela
window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == "Adicionar":
        produto = values["inpt_produto"]
        codigo = values["inpt_codigo"]
        data = values["inpt_data"]
        quantidade = values["inpt_quantidade"]
        insert(produto, codigo, data, quantidade)
        sg.popup_auto_close("Adicionado ao banco de dados")

window.close()


#inpt_produto inpt_codigo inpt_data inpt_quantidade