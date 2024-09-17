from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal
from typing import List

router = APIRouter(prefix="/contas-a-pagar-e-receber")


class ContaPagarReceber_Response(BaseModel): #Pydantic sendo utilizado
    id: int
    descricao: str
    valor: Decimal
    tipo: str #PAGAR, RECEBER

class ContaPagarReceber_Request(BaseModel): 
    descricao: str
    valor: Decimal
    tipo: str #PAGAR, RECEBER


@router.get("", response_model=List[ContaPagarReceber_Response]) #/ Definicao da Rota GET (ContaPagarReceber)
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

@router.post("", response_model=ContaPagarReceber_Response, status_code=201) #Definicao da Rota POST (ContaPagarReceber)
def criar_contas(conta: ContaPagarReceber_Request):

    return ContaPagarReceber_Response (
        id=3,
        descricao=conta.descricao,
        valor=conta.valor,
        tipo=conta.tipo
    )
    

    