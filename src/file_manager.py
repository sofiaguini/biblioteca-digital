import os
from collections import defaultdict
from datetime import datetime
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
            
           # --- TRECHO DE EXTRAÇÃO DE ANO REVISADO (Mais Simples) ---
            ano = None
            # Procura a primeira ocorrência de 4 dígitos (ex: 2023) no nome do arquivo
            match = re.search(r'(\d{4})', arquivo)
            if match and 1900 <= int(match.group(0)) <= 2099: # Verifica se está no intervalo razoável de anos
                ano = match.group(0)
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
        for ano, arquivos in sorted(anos.items()):
            print(f"Ano {ano}: {len(arquivos)} arquivos")
            for arq in arquivos:
                print(f"  - {arq}")