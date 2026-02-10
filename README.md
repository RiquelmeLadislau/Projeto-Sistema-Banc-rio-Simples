# 🏦 Projeto: Sistema Bancário Simples

## 📌 Descrição do Projeto
Este projeto consiste em um sistema bancário simples desenvolvido em **Python**, com o objetivo de simular operações básicas de uma conta bancária.

O sistema deve ser modular, organizado e utilizar recursos mais avançados da linguagem, como funções, listas e dicionários.

---

## 🧾 Requisitos do Cliente
O cliente deseja um sistema que:
- Cadastre clientes
- Crie contas bancárias
- Permita operações de saque e depósito
- Registre o histórico de transações
- Exiba relatórios simples

---

## ⚙️ Funcionalidades Obrigatórias

### 1️⃣ Cadastro de Cliente
- Cada cliente deve possuir:
  - Nome
  - CPF
- Os dados devem ser armazenados em um dicionário

---

### 2️⃣ Criação de Conta
- Cada conta deve conter:
  - Número da conta
  - CPF do titular
  - Saldo inicial
- As contas devem ser armazenadas em uma lista

---

### 3️⃣ Operações Bancárias
- **Depósito**
  - Não permitir valores negativos
  - Atualizar o saldo corretamente
- **Saque**
  - Verificar saldo disponível
  - Não permitir saque maior que o saldo

---

### 4️⃣ Histórico de Transações
- Cada conta deve manter um histórico contendo:
  - Tipo da operação
  - Valor
- O histórico deve ser uma lista de dicionários

---

### 5️⃣ Menu Principal
O sistema deve exibir um menu em loop:

```
1 - Cadastrar cliente
2 - Criar conta
3 - Depositar
4 - Sacar
5 - Exibir dados da conta
6 - Encerrar sistema
```

---

```
## 🧪 Exemplo de Execução

1 - Cadastrar cliente
2 - Criar conta
3 - Depositar
4 - Sacar
5 - Exibir dados da conta
6 - Encerrar sistema
Escolha uma opção: 1
Digite o nome: Ana
Digite o CPF: 12345678900
Cliente cadastrado com sucesso!

Escolha uma opção: 2
Conta criada com sucesso! Número: 1

Escolha uma opção: 3
Digite o número da conta: 1
Digite o valor do depósito: 500
Depósito realizado com sucesso!
```

---

## 📋 Regras Técnicas
- Utilizar:
  - Funções (`def`)
  - Listas
  - Dicionários
  - Estruturas condicionais e loops
- Código organizado e legível
- Separar responsabilidades em funções

---

## 🎯 Objetivo
Praticar estruturas de dados, modularização e controle de fluxo em Python.

---
