import pyodbc

#Conexão com o banco de dados
conn = pyodbc.connect ('DRIVER={SQL Server};' 'Server=DESKTOP-H3TVMMA;''Database=DB_SISTEMA;' 'Trusted_Connection=True;')
print("Sucess Connect")

#Cursor -> executa as funções no banco de dados
cursor = conn.cursor()


def insert(inpt_produto, inpt_codigo, inpt_data, inpt_quantidade): #Variaveis com informações para serem armazenadas no banco de dados

    #Comando insert para inserir as informações no banco de dados
    insert_info = f"""INSERT INTO ESTOQUE(PRODUTO, CODIGO, DATA_ADC, QUANTIDADE)
                    VALUES ('{inpt_produto}', {inpt_codigo}, '{inpt_data}', {inpt_quantidade})"""
    print("Added to database")

    #Cursor executando o insert no banco de dados
    cursor.execute(insert_info)

    #Commit para atualizar no banco de dados
    cursor.commit()



query = f'SELECT * FROM ESTOQUE'
cursor.execute(query)
data = cursor.fetchall()
