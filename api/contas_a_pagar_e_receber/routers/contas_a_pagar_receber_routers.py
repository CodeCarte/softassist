from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from shared.dependencies import get_db
from models.conta_a_pagar_receber_model import ContaPagarReceber
from functions.sqlalchemy_object_to_dict import sqlalchemy_obj_to_dict

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
def criar_contas(conta_a_pagar_e_receber_request: ContaPagarReceber_Request, 
                 db: Session = Depends(get_db)) -> ContaPagarReceber_Response:
    

    contas_a_pagar_e_receber = ContaPagarReceber(
        conta_a_pagar_e_receber_request.model_dump()
        )
    
    db.add(contas_a_pagar_e_receber)
    db.commit()
    db.refresh(contas_a_pagar_e_receber)

    return ContaPagarReceber_Response (

        **sqlalchemy_obj_to_dict(contas_a_pagar_e_receber)  
    )
    

    