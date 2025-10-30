import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Corrige o path para src/

from file_manager import (
    listar_documentos_por_tipo_e_ano, 
    exibir_listagem,
    adicionar_documento,
    renomear_documento,
    remover_documento
)

def menu_principal():
    """Exibe o menu principal e processa a escolha do usuário."""
    while True:
        print("\n" + "="*30)
        print("BIBLIOTECA DIGITAL - MENU")
        print("="*30)
        print("1. Listar Documentos")
        print("2. Adicionar Novo Documento")
        print("3. Renomear Documento")
        print("4. Remover Documento")
        print("5. Sair")
        print("="*30)

        escolha = input("Escolha uma opção (1-5): ").strip()

        if escolha == '1':
            documentos = listar_documentos_por_tipo_e_ano()
            exibir_listagem(documentos)
            
            # PAUSA CORRIGIDA PARA VISUALIZAÇÃO
            input("\nPressione Enter para retornar ao menu...") 
            
        elif escolha == '2':
            nome_arquivo = input("Nome do novo documento (ex: tese_2025.pdf): ").strip()
            if nome_arquivo:
                sucesso, mensagem = adicionar_documento(nome_arquivo)
                print(f"\n>> {mensagem}")
            else:
                print("\n>> Nome do arquivo não pode ser vazio.")
            
        elif escolha == '3':
            nome_antigo = input("Nome atual do documento a renomear: ").strip()
            nome_novo = input("Novo nome do documento (incluindo extensão): ").strip()
            if nome_antigo and nome_novo:
                sucesso, mensagem = renomear_documento(nome_antigo, nome_novo)
                print(f"\n>> {mensagem}")
            else:
                print("\n>> Nomes de arquivos não podem ser vazios.")
            
        elif escolha == '4':
            nome_arquivo = input("Nome do documento a remover: ").strip()
            if nome_arquivo:
                sucesso, mensagem = remover_documento(nome_arquivo)
                print(f"\n>> {mensagem}")
            else:
                print("\n>> Nome do arquivo não pode ser vazio.")
            
        elif escolha == '5':
            print("\nObrigado por usar a Biblioteca Digital. Até mais!")
            sys.exit(0)
            
        else:
            print("\nOpção inválida. Por favor, escolha um número de 1 a 5.")

def main():
    # Garante que o diretório 'data' existe ao iniciar a aplicação
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Diretório 'data/' criado com sucesso.")
        
    menu_principal()

if __name__ == "__main__":
    main()