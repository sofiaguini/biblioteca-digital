<img src="https://i.imgur.com/7tG2jKp.png" alt="PUCPR 4D" width="100%"/>

---

# Relatório de Testes e Feedback  
**Hora da Prática 2 – Programação para Ciência de Dados**

**Aluno(a)**: Sofia Guini  
**Instituição**: PUCPR - Graduação 4D  
**Repositório**: [https://github.com/sofiaguini/biblioteca-digital](https://github.com/sofiaguini/biblioteca-digital)  
**Data**: 30 de outubro de 2025

---

## 1. Objetivo do Sistema
Gerenciar documentos digitais (PDF, ePUB, etc.) com:
- Listagem por **tipo** e **ano**
- Interface **CLI** para manipulação
- Criação automática do diretório `data/`

---

## 2. Testes Realizados

| Funcionalidade | Entrada | Resultado Esperado | Status |
|----------------|--------|---------------------|--------|
| Listagem | Opção 1 | Arquivos por tipo/ano | OK |
| Adicionar | `artigo_2023.pdf` | "adicionado com sucesso" | OK |
| Renomear | `artigo_2023.pdf` → `final.pdf` | "renomeado com sucesso" | OK |
| Remover | `final.pdf` | "removido com sucesso" | OK |
| Criação `data/` | Iniciar sem pasta | "Diretório criado" | OK |

---

## 3. Testes Automatizados

```bash
python -m unittest discover tests