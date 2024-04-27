import re
import unittest
from flask import Flask, request, jsonify

app = Flask(__name__)

class Funcionario:
    
    @staticmethod
    def formatar_nome(self, nome):
        self.nome = nome
        if nome.strip():
            palavras = nome.split()
            palavras_formatadas = [palavra.capitalize() for palavra in palavras]
            nome_formatado = ' '.join(palavras_formatadas)
            return nome_formatado
        else:
            raise ValueError("Um nome deve ser digitado.")
 
    @staticmethod
    def formatar_salario(self, valor):
        self.valor = valor
        try:
            salario_formatado = f'R${float(valor):,.2f}'
            return salario_formatado
        except ValueError:
            raise ValueError("Por favor, digite um valor numérico válido para o salário.")

    @staticmethod
    def nivel_profissional(self, valor):
        self.valor = valor
        if valor <= 2000:
            return "Junior"
        elif 2001 <= valor <= 8000:
            return "Pleno"
        else:
            return "Sênior"

    @staticmethod
    def validate_cpf(self, cpf: str) -> str:
        self.cpf = cpf
        cpf = re.sub(r'[^\d]', '', cpf)
        
        if len(cpf) != 11:
            return "CPF inválido"
    
        total = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digit1 = (total * 10) % 11
        if digit1 == 10:
            digit1 = 0
    
        total += digit1 * 2
        digit2 = (total * 10) % 11
        if digit2 == 10:
            digit2 = 0
    
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    @staticmethod
    def validar_habilidades(self, habilidades):
        self.habilidades = habilidades
        habilidades_lista = habilidades.split(';')
        habilidades_unicas = set(habilidades_lista)
        if len(habilidades_unicas) >= 3:
            return True
        else:
            return False


def adicionar_funcionario(lista_funcionarios):
    while True:
        try:
            nome_digitado = input("Digite o nome do funcionário: ")
            salario_digitado = input("Digite o salário: ")
            numero_cpf = input("Digite um CPF (11 dígitos): ")
            habilidades_digitadas = input("Digite as habilidades (mínimo 3, separadas por ';'): ")

            nome_formatado = Funcionario.formatar_nome(nome_digitado)
            salario_formatado = Funcionario.formatar_salario(salario_digitado)
            nivel = Funcionario.nivel_profissional(float(salario_digitado))
            cpf_formatado = Funcionario.validate_cpf(numero_cpf)
            habilidades_validas = Funcionario.validar_habilidades(habilidades_digitadas)
            if habilidades_validas:
                funcionario = {
                    "Nome": nome_formatado,
                    "Salário": salario_formatado,
                    "Nível": nivel,
                    "CPF": cpf_formatado,
                    "Habilidades": habilidades_digitadas
                }
                lista_funcionarios.append(funcionario)
                print("\nFuncionário adicionado com sucesso!")
            else:
                print("Funcionário inválido")

            opcao = input("\nDeseja adicionar outro funcionário? (1 - Sim, 2 - Voltar ao menu): ")
            if opcao != '1':
                break
        except ValueError as ve:
            print(ve)
            break

class TestFuncionarioMethods(unittest.TestCase):
    def test_formatar_nome(self):
        self.assertEqual(Funcionario.formatar_nome("joao da silva"), "Joao Da Silva")
        self.assertEqual(Funcionario.formatar_nome("maria"), "Maria")
        with self.assertRaises(ValueError):
            Funcionario.formatar_nome("")

    def test_formatar_salario(self):
        self.assertEqual(Funcionario.formatar_salario("2000"), "R$2,000.00")
        self.assertEqual(Funcionario.formatar_salario("3500.50"), "R$3,500.50")
        with self.assertRaises(ValueError):
            Funcionario.formatar_salario("dois mil")
    
    def test_nivel_profissional(self):
        self.assertEqual(Funcionario.nivel_profissional(1500), "Junior")
        self.assertEqual(Funcionario.nivel_profissional(4000), "Pleno")
        self.assertEqual(Funcionario.nivel_profissional(10000), "Sênior")

    def test_validate_cpf(self):
        self.assertEqual(Funcionario.validate_cpf("123.456.789-09"), "123.456.789-09")
        self.assertEqual(Funcionario.validate_cpf("12345678909"), "123.456.789-09")
        self.assertEqual(Funcionario.validate_cpf("00000000000"), "000.000.000-00")
        self.assertEqual(Funcionario.validate_cpf("999.999.999-99"), "999.999.999-99")
        self.assertEqual(Funcionario.validate_cpf("1234567890"), "CPF inválido")

    def test_validar_habilidades(self):
        self.assertTrue(Funcionario.validar_habilidades("Python;Java;SQL"))
        self.assertFalse(Funcionario.validar_habilidades("Python;Python;Python"))
        self.assertFalse(Funcionario.validar_habilidades("Python"))
        self.assertFalse(Funcionario.validar_habilidades("Python;Java"))

if __name__ == '__main__':
    app.run(debug=True)