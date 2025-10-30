import os
from collections import defaultdict
import re

def listar_documentos_por_tipo_e_ano(diretorio='data'):
    """
    Lista todos os documentos digitais no diretório, organizados por tipo de arquivo e ano de publicação.
    Tenta extrair um ano de 4 dígitos (ex: 2023) do nome do arquivo.
    Retorna um dicionário: {tipo: {ano: [lista_arquivos]}}
    """
    documentos = defaultdict(lambda: defaultdict(list))
    
    if not os.path.exists(diretorio):
        print(f"Diretório '{diretorio}' não existe. Crie a pasta 'data' e adicione arquivos.")
        return documentos
    
    for arquivo in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho):
            _, extensao = os.path.splitext(arquivo)
            tipo = extensao.lower().lstrip('.')  # ex: 'pdf'
            
            # --- TRECHO DE EXTRAÇÃO DE ANO REVISADO (FINAL) ---
            ano = None
            # Procura a primeira ocorrência de 4 dígitos
            match = re.search(r'(\d{4})', arquivo)
            if match:
                ano_str = match.group(0)
                # Verifica se o ano está em um intervalo razoável (1900 a 2099)
                if 1900 <= int(ano_str) <= 2099: 
                    ano = ano_str
            # ------------------------------------------
            
            if ano:
                documentos[tipo][ano].append(arquivo)
            else:
                # Se não encontrar ano, coloca em 'desconhecido'
                documentos[tipo]['desconhecido'].append(arquivo)
    
    return documentos

def exibir_listagem(documentos):
    """Exibe a listagem organizada de forma legível."""
    if not documentos:
        print("Nenhum documento encontrado.")
        return
    
    for tipo, anos in documentos.items():
        print(f"\n--- Tipo: {tipo.upper()} ---")
        # Ordena a lista de anos (para que 2023 venha antes de 2024, 'desconhecido' no final)
        for ano, arquivos in sorted(anos.items(), key=lambda item: item[0] if item[0] != 'desconhecido' else 'zzzz'):
            print(f"Ano {ano}: {len(arquivos)} arquivos")
            for arq in arquivos:
                print(f"  - {arq}")

def adicionar_documento(nome_arquivo_novo, diretorio='data'):
    """
    Cria um arquivo vazio na pasta 'data/' com o nome fornecido.
    Retorna True se bem-sucedido, False caso contrário.
    """
    caminho = os.path.join(diretorio, nome_arquivo_novo)
    
    if os.path.exists(caminho):
        return False, f"Erro: Arquivo '{nome_arquivo_novo}' já existe!"
    
    try:
        with open(caminho, 'w') as f:
            pass
        return True, f"Documento '{nome_arquivo_novo}' adicionado com sucesso."
    except Exception as e:
        return False, f"Erro ao criar arquivo: {e}"

def renomear_documento(nome_antigo, nome_novo, diretorio='data'):
    """
    Renomeia um documento existente na pasta 'data/'.
    Retorna True se bem-sucedido, False caso contrário.
    """
    caminho_antigo = os.path.join(diretorio, nome_antigo)
    caminho_novo = os.path.join(diretorio, nome_novo)
    
    if not os.path.exists(caminho_antigo):
        return False, f"Erro: Arquivo '{nome_antigo}' não encontrado."
        
    if os.path.exists(caminho_novo):
        return False, f"Erro: O nome '{nome_novo}' já está em uso."
        
    try:
        os.rename(caminho_antigo, caminho_novo)
        return True, f"Documento '{nome_antigo}' renomeado para '{nome_novo}'."
    except Exception as e:
        return False, f"Erro ao renomear arquivo: {e}"

def remover_documento(nome_arquivo, diretorio='data'):
    """
    Remove um documento da pasta 'data/'.
    Retorna True se bem-sucedido, False caso contrário.
    """
    caminho = os.path.join(diretorio, nome_arquivo)
    
    if not os.path.exists(caminho):
        return False, f"Erro: Arquivo '{nome_arquivo}' não encontrado."
        
    try:
        os.remove(caminho)
        return True, f"Documento '{nome_arquivo}' removido com sucesso."
    except Exception as e:
        return False, f"Erro ao remover arquivo: {e}"