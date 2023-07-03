import requests
import json
API_KEY = "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"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
#link = "https://api.openai.com/v1/models"
#requisition = requests.get(link,headers=headers)
link = "https://api.openai.com/v1/chat/completions"
id_model = "gpt-3.5-turbo"

body_message = {
    "model": id_model,
    "messages": [{"role": "system", "content": """
    CONTEXT: 
    1. You are "Jarvis", the virtual investment assistant for XP INC brazillian investment app.
    2. You will chat with the user - in Portuguese- and help them to reduce the monthly spends.
    3. Be fun and light-hearted while chatting.
    4. Consider the column {earn} to be his income. 
    5. Always consider the - DATA - to be historic's user.
    6. You will answer with the requested information
    

    RULES: 
    1. In each message, identify the user's preferences and find keywords to search for.
    
    DATA: 
    Origem/Mês,Janeiro,Fevereiro,Março,earn
    Água," R$  31,74 "," R$  35,10 "," R$  17,55 "," R$  5.000,00 "
    Luz," R$  163,11 "," R$  152,50 "," R$  116,68 ",
    Gás,"R$ 0,00","R$ 0,00","R$ 0,00",
    Internet," R$  52,65 "," R$  52,65 "," R$  52,65 ",
    Condomínio,"R$ 0,00","R$ 0,00","R$ 0,00",
    Aluguel,"R$ 0,00","R$ 0,00","R$ 0,00",
    Empregado Doméstico,"R$ 0,00","R$ 0,00","R$ 0,00",
    Prestação da casa,"R$ 0,00","R$ 0,00","R$ 0,00",
    Seguro da casa,"R$ 0,00","R$ 0,00","R$ 0,00",
    Telefone,"  R$  60,00 ","R$ 0,00","R$ 0,00",
    Assinatura TV,"R$ 0,00","R$ 0,00","R$ 0,00",
    Água Mineral,"R$ 0,00","R$ 0,00"," R$  75,00 ",
    Reparos Casa,"R$ 0,00","R$ 0,00","R$ 0,00",
    Produtos Limpeza,"R$ 0,00","R$ 0,00","R$ 0,00",
    Total Habitação," R$  247,50 "," R$  240,25 "," R$  261,88 ",
    ,,,,
    Café da manhã Fora,"R$ 0,00","R$ 0,00","R$ 0,00",
    Almoço Fora,"R$ 0,00","R$ 0,00","R$ 0,00",
    Lanches Fora,"R$ 63,60","R$ 0,00","R$ 63,80",
    Janta Fora,"R$ 164,50","R$ 42,00","R$ 70,00",
    Supermercado,"R$ 0,00","R$ 0,00","R$ 0,00",
    Feira,"R$ 0,00","R$ 0,00","R$ 0,00",
    Padaria,"R$ 89,82","R$ 0,00","R$ 0,00",
    Outros,"R$ 0,00","R$ 0,00","R$ 0,00",
    Total Alimentação," R$  317,92 "," R$  42,00 "," R$  133,80 ",
    ,,,,
    Uber," R$  275,72 "," R$  77,31 ","R$ 0,00",
    Seguro do carro,"R$ 0,00","R$ 0,00","R$ 0,00",
    Estacionamento,"R$ 0,00","R$ 0,00","R$ 0,00",
    Outros,"R$ 0,00"," R$  39,50 ","R$ 0,00",
    Total Transporte," R$  275,72 "," R$  116,81 ", R$  -   ,
    ,,,,
    Seguro saúde,"R$ 0,00","R$ 0,00","R$ 0,00",
    Medicamentos,"R$ 0,00"," R$  57,49 ","R$ 0,00",
    Plano de saúde," R$  112,37 "," R$  129,79 "," R$  129,79 ",
    Academia," R$  45,00 ","R$ 0,00"," R$  60,00 ",
    Outros,"R$ 0,00","R$ 0,00","R$ 0,00",
    Total Saúde," R$  157,37 "," R$  187,28 "," R$  189,79 ",
    ,,,,
    Colégio,"R$ 0,00","R$ 0,00","R$ 0,00",
    Faculdade," R$  258,76 "," R$  258,76 "," R$  279,83 ",
    Curso de ingles," R$  500,00 "," R$  500,00 "," R$  500,00 ",
    Assinatura Serviço,"R$ 0,00","R$ 0,00","R$ 0,00",
    Outros," R$  19,90 ","R$ 0,00","R$ 0,00",
    Total Educação," R$  778,66 "," R$  758,76 "," R$  779,83 ",
    ,,,,
    Cinema," R$  51,00 ","R$ 0,00","R$ 0,00",
    Balada,"R$ 0,00","R$ 0,00"," R$  60,00 ",
    Surf,"R$ 0,00","R$ 0,00"," R$  55,00 ",
    Assinatura Livro,"R$ 0,00","R$ 0,00","R$ 0,00",
    Outros,"R$ 0,00"," R$  86,50 "," R$  45,00 ",
    Total Lazer," R$  51,00 "," R$  86,50 "," R$  160,00 ",
    ,,,,
    IPTU,"R$ 0,00","R$ 0,00","R$ 0,00",
    IPVA,"R$ 0,00","R$ 0,00","R$ 0,00",
    IR,"R$ 0,00","R$ 0,00","R$ 0,00",
    MEI," R$  885,98 ","R$ 0,00","R$ 0,00",
    Total Impostos," R$  885,98 ", R$  -   , R$  -   ,
    ,,,,
    Cartão," R$  678,24 "," R$  295,25 "," R$  490,09 ",
    Videira,"R$ 0,00","R$ 0,00","R$ 0,00",
    Crédito Celular,"R$ 0,00"," R$  60,00 "," R$  60,00 ",
    Iphone conserto,"R$ 0,00","R$ 0,00","R$ 0,00",
    Barbearia,"R$ 0,00"," R$  10,00 "," R$  10,00 ",
    Presente,"R$ 0,00","R$ 0,00","R$ 0,00",
    Empréstimo,"R$ 0,00","R$ 0,00","R$ 0,00",
    outros,"R$ 0,00","R$ 0,00","R$ 0,00",
    Total Outros," R$  678,24 "," R$  365,25 "," R$  560,09 ",
    ,,,,
    Total Fixa," R$  3.074,47 "," R$  1.754,85 "," R$  1.951,59 ",
    
    
    
    """             
                  }, {"role": "user", "content": "Qual foi a orgem de gasto que mais gastei?"}]
}
body_message = json.dumps(body_message)

requisition = requests.post(link, headers=headers, data=body_message)
#print(requisition)

response = requisition.json()
responseMessage = response["choices"][0]["message"]["content"]


print(responseMessage)
#print(body_message)

