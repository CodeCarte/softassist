from contas_a_pagar_e_receber.models import conta_a_pagar_receber_model
from sqlalchemy import inspect


def sqlalchemy_obj_to_dict(obj):

    return {column.key: getattr(obj, column.key) for column in inspect(obj).mapper.column_attrs}

