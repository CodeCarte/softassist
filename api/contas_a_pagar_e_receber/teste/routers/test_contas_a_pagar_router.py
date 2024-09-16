from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_listar_contas_a_pagar_e_receber ():

    response = client.get('/contas-a-pagar-e-receber')

    assert response.status_code == 200


   


    