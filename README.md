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
