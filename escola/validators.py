def validate_cpf(cpf):
    return len(cpf) != 11

def validate_nome(nome):
    return not (nome.isalpha())

def validate_celular(celular):
    return len(celular) != 13
