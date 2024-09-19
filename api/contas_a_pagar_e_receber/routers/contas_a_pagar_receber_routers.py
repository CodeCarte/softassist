from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from shared.dependencies import get_db
from contas_a_pagar_e_receber.models.conta_a_pagar_receber_model import ContaPagarReceber
from functions.sqlalchemy_object_to_dict import sqlalchemy_obj_to_dict

router = APIRouter(prefix="/contas-a-pagar-e-receber")


class ContaPagarReceber_Response(BaseModel): #Pydantic sendo utilizado
    id: int
    descricao: str
    valor: Decimal
    tipo: str #PAGAR, RECEBER

    class Config:
        orm_mode = True

class ContaPagarReceber_Request(BaseModel): 
    descricao: str
    valor: Decimal
    tipo: str #PAGAR, RECEBER


@router.get("", response_model=List[ContaPagarReceber_Response]) #/ Definicao da Rota GET (ContaPagarReceber)
def listar_contas(db: Session = Depends(get_db)) -> List[ContaPagarReceber_Response]:

    return db.query(ContaPagarReceber).all()



@router.post("", response_model=ContaPagarReceber_Response, status_code=201) #Definicao da Rota POST (ContaPagarReceber)
def criar_contas(conta_a_pagar_e_receber_request: ContaPagarReceber_Request, 
                 db: Session = Depends(get_db)) -> ContaPagarReceber_Response:
    

    contas_a_pagar_e_receber = ContaPagarReceber(

        descricao = conta_a_pagar_e_receber_request.descricao,
        valor = conta_a_pagar_e_receber_request.valor,
        tipo = conta_a_pagar_e_receber_request.tipo

        )
    
    db.add(contas_a_pagar_e_receber)
    db.commit()
    db.refresh(contas_a_pagar_e_receber)

    return contas_a_pagar_e_receber

    