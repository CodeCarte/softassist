from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_listar_contas_a_pagar_e_receber():

    response = client.get('/contas-a-pagar-e-receber') #Requisitando dados para o servidor
    assert response.status_code == 200 #Verificando se a solicitacao foi bem sucedida

    contas = response.json()

    for conta in contas:
        conta['valor'] = float(conta['valor'])

    assert contas == [ #Verificando se a resposta Json é igual a lista esperada
        {'id': 1, 'descricao': 'Aluguel', 'valor': 1000.50, 'tipo': 'PAGAR',}, 
        {'id': 2, 'descricao': 'Salário', 'valor': 5000.0, 'tipo': 'RECEBER'}
    ]

def test_criar_conta_a_pagar_e_receber():

    nova_conta = {
        "descricao": "Curso de Python",
        "valor": 333,
        "tipo": "PAGAR"
    }

    nova_conta_copy = nova_conta.copy()
    nova_conta_copy["id"] = 3

    response = client.post('/contas-a-pagar-e-receber', json=nova_conta)

    conta = response.json()
    
    conta['valor'] = float(conta['valor'])

    assert conta == nova_conta_copy

    assert response.status_code == 201
  






   


    