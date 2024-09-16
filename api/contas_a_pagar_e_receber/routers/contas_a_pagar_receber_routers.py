from fastapi import APIRouter

router = APIRouter(prefix="/contas-a-pagar-e-receber")

def listar_contas():

    return [
        {"contas1": "contas1"},
        {"contas2": "contas2"}
    ]