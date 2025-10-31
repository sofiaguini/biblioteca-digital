import re

def validar_nome_arquivo(nome):
    """
    Valida se o nome do arquivo é válido para o sistema.
    - Deve conter extensão (.pdf, .epub, etc.)
    - Deve ter ano de 4 dígitos opcional
    Retorna True/False e mensagem.
    """
    if not nome:
        return False, "Nome não pode ser vazio."
    
    if not re.search(r'\.\w+$', nome):
        return False, "Nome deve ter extensão (ex: .pdf)."
    
    # Opcional: checa se tem ano
    if not re.search(r'\d{4}', nome):
        return True, "Nome válido (sem ano detectado)."
    
    return True, "Nome válido com ano detectado."

# Exemplo de uso:
# valido, msg = validar_nome_arquivo("artigo_2023.pdf")
# print(msg)