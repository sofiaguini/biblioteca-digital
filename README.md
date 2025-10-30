<img src="https://i.imgur.com/7tG2jKp.png" alt="PUCPR 4D - Programação para Ciência de Dados" width="100%"/>

---

# Sistema de Gerenciamento de Biblioteca Digital

**Disciplina**: Programação para Ciência de Dados  
**Atividade**: Hora da Prática 2  
**Aluno(a)**: Sofia Guini  
**Instituição**: PUCPR - Graduação 4D

---

## Descrição do Projeto

Sistema em Python para gerenciar documentos digitais (PDF, ePUB, DOCX) de uma biblioteca universitária, com:

- Listagem de arquivos por **tipo** e **ano de publicação** (extraído do nome com regex)  
- Interface **CLI** para **adicionar**, **renomear** e **remover** documentos  
- Versionamento com **Git/GitHub** (commits claros, PRs prontos)  
- **Testes automatizados** com `unittest`  
- **Documentação completa** e **guia de contribuição**

---

## Estrutura do Projeto
biblioteca-digital/
├── src/                  # Código-fonte
│   ├── main.py           # Interface CLI com menu
│   ├── file_manager.py   # Funções de manipulação
│   └── utils.py          # Funções auxiliares
├── data/                 # Documentos (criada automaticamente)
├── docs/                 # Documentação
│   ├── CONTRIBUTING.md   # Guia de contribuição
│   └── REPORT.md         # Relatório final
├── tests/                # Testes unitários
│   └── test_file_manager.py
├── .gitignore
├── LICENSE               # MIT
└── README.md             # Este arquivo

---

## Links Rápidos
- [Código Principal (`main.py`)](src/main.py)
- [Manipulação de Arquivos (`file_manager.py`)](src/file_manager.py)
- [Testes Unitários](tests/test_file_manager.py)
- [Guia de Contribuição](docs/CONTRIBUTING.md)
- [Relatório Final](docs/REPORT.md)
- [Commits](https://github.com/sofiaguini/biblioteca-digital/commits/main)

---

## Como Executar

```bash
git clone https://github.com/sofiaguini/biblioteca-digital.git
cd biblioteca-digital
python src/main.py
==============================
BIBLIOTECA DIGITAL - MENU
==============================
1. Listar Documentos
2. Adicionar Novo Documento
3. Renomear Documento
4. Remover Documento
5. Sair
==============================
Escolha uma opção (1-5): 2
Nome do novo documento: artigo_2023.pdf
>> Documento 'artigo_2023.pdf' adicionado com sucesso.

Funcionalidade,Entrada,Resultado Esperado,Status
Listagem,Opção 1,Arquivos organizados por tipo e ano,OK
Adicionar documento,artigo_ciencia_2023.pdf,"""Documento adicionado com sucesso""",OK
Renomear documento,artigo_ciencia_2023.pdf → final.pdf,"""renomeado com sucesso""",OK
Remover documento,artigo_ciencia_2023.pdf,"""removido com sucesso""",OK
Criação automática,Iniciar sem pasta data/,"""Diretório 'data/' criado com sucesso""",OK

Feedback dos Usuários (Bibliotecários Fictícios)

"O sistema é muito simples de usar! Gostei da organização por ano."
— Bibliotecária Ana, PUCPR


"Seria ótimo poder buscar um documento pelo título ou autor."
— Bibliotecário João, Setor de Acervo


"A pausa com 'Enter' ajuda a ler a listagem com calma."
— Estagiária Laura

Feedback,Ação Implementada
"""Organização por ano""",Listagem ordenada por tipo → ano → nome
"""Pausa para leitura""","Adicionado input(""Pressione Enter..."") após listagem"
"""Mensagens claras""",Retorno de True/False + mensagem em todas as funções
"""Criação automática""",os.makedirs('data') no main()
Sistema validado em ambiente local com 100% de sucesso.

Testes Automatizados
python -m unittest discover tests

Saída:
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK

Integração com Git e GitHub

Commits claros e granulares (10+)
Pull Requests habilitados
Guia de contribuição completo: CONTRIBUTING.md
Licença MIT – Contribuições bem-vindas!

Relatório Final
Veja o relatório completo em: docs/REPORT.md

Licença
MIT License – Contribuições bem-vindas!

Sistema 100% funcional, testado, documentado e pronto para colaboração.
Sofia Guini – PUCPR 4D
30 de outubro de 2025


---

## COMO ATUALIZAR NO GITHUB

```powershell
git add README.md
git commit -m "docs: finaliza README com modelo PUCPR 4D, imagem, testes, feedback e estrutura completa"
git push
