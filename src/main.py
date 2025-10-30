import os
import sys
from src.file_manager import listar_documentos_por_tipo_e_ano, exibir_listagem
# As funções de CRUD (adicionar, remover, renomear) serão adicionadas no próximo sub-passo

def menu_principal():
    """Exibe o menu principal e processa a escolha do usuário."""
    while True:
        print("\n" + "="*30)
        print("BIBLIOTECA DIGITAL - MENU")
        print("="*30)
        print("1. Listar Documentos")
        print("2. Adicionar Novo Documento (Ainda não implementado)")
        print("3. Renomear Documento (Ainda não implementado)")
        print("4. Remover Documento (Ainda não implementado)")
        print("5. Sair")
        print("="*30)

        escolha = input("Escolha uma opção (1-5): ").strip()

        if escolha == '1':
            # Chama a função de listagem
            documentos = listar_documentos_por_tipo_e_ano()
            exibir_listagem(documentos)
        elif escolha == '2':
            print("\n>> Funcionalidade de Adicionar será implementada no próximo passo.")
        elif escolha == '3':
            print("\n>> Funcionalidade de Renomear será implementada no próximo passo.")
        elif escolha == '4':
            print("\n>> Funcionalidade de Remover será implementada no próximo passo.")
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