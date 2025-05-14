import csv
import os
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    cpf: int
    cargo: str
    salario: float

    def exibir_detalhes(self):
        print(f"\nDetalhes do Funcionário:")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario:,.2f}")

funcionarios = []

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("3. Excluir Funcionário")
    print("4. Sair")

def exibir_resultados():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print(f"\n{'Nome':<20} {'CPF':<15} {'Cargo':<15} {'Salário':<10}")
        print("-" * 60)
        for funcionario in funcionarios:
            print(f"{funcionario.nome:<20} {funcionario.cpf:<15} {funcionario.cargo:<15} R$ {funcionario.salario:,.2f}")

def cadastrar_funcionario():
    nome = input("Nome do Funcionário: ")
    cpf = int(input("CPF do Funcionário: "))
    cargo = input("Cargo do Funcionário: ")
    salario = float(input("Salário do Funcionário: R$ "))
    funcionario = Funcionario(nome, cpf, cargo, salario)
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")
    salvar_dados_csv()

def excluir_funcionario():
    cpf = int(input("Digite o CPF do funcionário que deseja excluir: "))
    funcionario_a_excluir = None

    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            funcionario_a_excluir = funcionario
            break

    if funcionario_a_excluir:
        funcionarios.remove(funcionario_a_excluir)
        print("Funcionário excluído com sucesso!")
        salvar_dados_csv()
    else:
        print("Funcionário não encontrado.")

def salvar_dados_csv():
    if funcionarios:
        with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "CPF", "Cargo", "Salário"])
            for funcionario in funcionarios:
                writer.writerow([funcionario.nome, funcionario.cpf, funcionario.cargo, funcionario.salario])
        print("Dados salvos em 'funcionarios.csv'.")
    else:
        print("Nenhum funcionário para salvar.")

def carregar_dados_csv():
    if os.path.exists('funcionarios.csv'):
        with open('funcionarios.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Pular cabeçalho
            for row in reader:
                nome, cpf, cargo, salario = row
                funcionarios.append(Funcionario(nome, int(cpf), cargo, float(salario)))
        print("Dados carregados de 'funcionarios.csv'.")
    else:
        print("Arquivo 'funcionarios.csv' não encontrado.")

carregar_dados_csv()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_funcionario()
    elif opcao == '2':
        exibir_resultados()
    elif opcao == '3':
        excluir_funcionario()
    elif opcao == '4':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")


        #aluno nicolas ricardo
