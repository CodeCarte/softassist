from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal
from typing import List

router = APIRouter(prefix="/contas-a-pagar-e-receber")


class ContaPagarReceber_Response(BaseModel): #dados que o cliente vai receber do servidor
    id: int
    descricao: str
    valor: Decimal
    tipo: str #PAGAR, RECEBER

class ContaPagarReceber_Request(BaseModel): #dados que o cliente vai enviar ao servidor
    descricao: str
    valor: Decimal
    tipo: str #PAGAR, RECEBER


@router.get("/", response_model=List[ContaPagarReceber_Response]) #/ Indica que é a raiz de router, no caso (/contas-a-pagar-e-receber)
def listar_contas():

    return [
        ContaPagarReceber_Response(
        id=1,
        descricao="Aluguel",
        valor=1000.50,
        tipo="PAGAR"
        ),

        ContaPagarReceber_Response(
        id=2,
        descricao="Salário",
        valor=5000,
        tipo="RECEBER"
            ),
]

@router.post("/", response_model=ContaPagarReceber_Response, status_code=201)
def criar_contas(conta: ContaPagarReceber_Request):

    return ContaPagarReceber_Response (
        id=3,
        descricao=conta.descricao,
        valor=conta.valor,
        tipo=conta.tipo
    )
    

    