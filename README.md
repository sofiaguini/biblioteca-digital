# Sistema de Gerenciamento de Biblioteca Digital

**Disciplina**: Programação para Ciência de Dados  
**Atividade**: Hora da Prática 2  
**Aluno(a)**: Sofia Guini  
**Instituição**: PUCPR - Graduação 4D

---

## Descrição do Projeto

Sistema em Python para gerenciar documentos digitais (PDF, ePUB, etc) de uma biblioteca universitária, com:

- Listagem de arquivos por tipo e ano de publicação  
- Interface CLI para adicionar, renomear e remover documentos  
- Versionamento com Git/GitHub  
- Testes automatizados  
- Documentação completa

---

## Estrutura do Projeto

---

## Testes e Feedback

### Testes Realizados
| Funcionalidade       | Entrada                     | Resultado Esperado                     | Status |
|----------------------|-----------------------------|----------------------------------------|--------|
| Listagem             | Opção 1                     | Arquivos por tipo/ano                  | OK |
| Adicionar            | `artigo_2023.pdf`           | "adicionado com sucesso"               | OK |
| Renomear             | `artigo_2023.pdf` → `final.pdf` | "renomeado"                        | OK |
| Remover              | `artigo_2023.pdf`           | "removido com sucesso"                 | OK |
| Criação de `data/`   | Iniciar sem pasta           | "Diretório 'data/' criado"             | OK |

### Feedback dos Usuários (Bibliotecários Fictícios)
> _"O menu é simples e intuitivo. Gostaria de buscar por título."_  
> — Bibliotecária Ana

> _"A listagem por ano ajuda muito no inventário!"_  
> — Bibliotecário João

### Ajustes Feitos com Base no Feedback
- Listagem ordenada por tipo e ano
- Mensagens claras de sucesso/erro
- Pausa com `Enter` para visualizar resultados

**Sistema testado e validado em ambiente local.**

## Testes Automatizados

Executados com `unittest`:

```bash
python -m unittest discover tests

---

## Testes e Feedback

### Testes Realizados
| Funcionalidade       | Entrada                          | Resultado Esperado                          | Status |
|----------------------|----------------------------------|---------------------------------------------|--------|
| Listagem             | Opção 1                          | Arquivos organizados por tipo e ano         | OK |
| Adicionar documento  | `artigo_ciencia_2023.pdf`        | "Documento adicionado com sucesso"          | OK |
| Renomear documento   | `artigo_ciencia_2023.pdf` → `final.pdf` | "renomeado com sucesso"               | OK |
| Remover documento    | `artigo_ciencia_2023.pdf`        | "removido com sucesso"                      | OK |
| Criação automática   | Iniciar sem pasta `data/`        | "Diretório 'data/' criado com sucesso"      | OK |

### Feedback dos Usuários (Bibliotecários Fictícios)

> _"O sistema é muito simples de usar! Gostei da organização por ano."_  
> — **Bibliotecária Ana**, PUCPR

> _"Seria ótimo poder buscar um documento pelo título ou autor."_  
> — **Bibliotecário João**, Setor de Acervo

> _"A pausa com 'Enter' ajuda a ler a listagem com calma."_  
> — **Estagiária Laura**

### Ajustes Incorporados com Base no Feedback

| Feedback | Ação Implementada |
|--------|-------------------|
| "Organização por ano" | Listagem ordenada por tipo → ano → nome |
| "Pausa para leitura" | Adicionado `input("Pressione Enter...")` após listagem |
| "Mensagens claras" | Retorno de `True/False + mensagem` em todas as funções |
| "Criação automática" | `os.makedirs('data')` no `main()` |

**Sistema validado em ambiente local com 100% de sucesso.**
