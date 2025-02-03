# -*- coding: utf-8 -*-
"""
GERADOR DE CPF PROFISSIONAL v4.1
Sistema Certificado - DevFerreiraG Security
"""

import random
import os
import hashlib
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

class CPFGeneratorPro:
    def __init__(self):
        self.log_file = 'cpf_secure_log.db'
        self._versao = "4.1.0"
        self._developer_code = "HF9G7T2P"
        self._inicializar_sistema()
        
    def _inicializar_sistema(self):
        """Configuração inicial do sistema"""
        self._limpar_console()
        self._verificar_logs()
        self._exibir_banner()

    def _verificar_logs(self):
        """Cria estrutura de logs seguros"""
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write("=== LOG SEGURO - CPF GENERATOR ===\n")
                f.write(f"Sistema inicializado em: {datetime.now()}\n\n")

    def _exibir_banner(self):
        """Exibe banner de segurança"""
        print(Fore.CYAN + Style.BRIGHT + r"""
        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
        █ ██████  ██████  ███████ ██████ █
        █ ██   ██ ██   ██ ██      ██   █ █
        █ ██████  ██████  █████   ██████ █
        █ ██      ██   ██ ██      ██   █ █
        █ ██      ██   ██ ███████ ██   █ █
        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
        """)
        print(Fore.YELLOW + f"Versão {self._versao} | Dev: {self._developer_code}\n")

    def _gerar_digito_verificador(self, cpf_parcial):
        """Algoritmo de validação avançado"""
        soma = 0
        peso = len(cpf_parcial) + 1
        for i in range(len(cpf_parcial)):
            soma += int(cpf_parcial[i]) * peso
            peso -= 1
        resto = 11 - (soma % 11)
        return '0' if resto > 9 else str(resto)

    def _criptografar_cpf(self, cpf):
        """Protege o CPF no log usando hash SHA-256"""
        return hashlib.sha256(cpf.encode()).hexdigest()

    def gerar_cpf(self, formatado=True):
        """Gera CPF válido com opção de formatação"""
        cpf_base = [str(random.randint(0, 9)) for _ in range(9)]
        cpf_base.append(self._gerar_digito_verificador(cpf_base))
        cpf_base.append(self._gerar_digito_verificador(cpf_base))
        cpf = ''.join(cpf_base)
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}' if formatado else cpf

    def _registrar_log(self, cpf):
        """Registro seguro com timestamp e hash"""
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cpf_hash = self._criptografar_cpf(cpf)
        with open(self.log_file, 'a') as log:
            log.write(f"[{data}] OPERATION: GENERATE | HASH: {cpf_hash}\n")

    def _limpar_console(self):
        """Limpa o console de forma cross-platform"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def _exibir_info_sistema(self):
        """Mostra informações técnicas do sistema"""
        self._limpar_console()
        print(Fore.GREEN + "\n=== INFORMAÇÕES DO SISTEMA ===")
        print(f"Versão: {self._versao}")
        print(f"Logs registrados: {self._contar_logs()}")
        print(f"Desenvolvedor: Sistema {self._developer_code}")
        print(f"Arquivo de log: {os.path.abspath(self.log_file)}")
        input("\nPressione Enter para continuar...")

    def _contar_logs(self):
        """Conta o número de CPFs gerados"""
        try:
            with open(self.log_file, 'r') as f:
                return sum(1 for line in f if "OPERATION: GENERATE" in line)
        except:
            return 0

    def _validar_entrada_numerica(self, mensagem, minimo=1, maximo=1000):
        """Valida entrada numérica com limites"""
        while True:
            try:
                valor = int(input(mensagem))
                if minimo <= valor <= maximo:
                    return valor
                print(Fore.RED + f"Erro: Insira um valor entre {minimo} e {maximo}!")
            except ValueError:
                print(Fore.RED + "Entrada inválida! Use apenas números.")

    def menu_principal(self):
        """Interface de usuário avançada"""
        while True:
            self._limpar_console()
            print(Fore.CYAN + " MENU PRINCIPAL ".center(50, '='))
            print(Fore.GREEN + "[1]" + Style.RESET_ALL + " Gerar CPF único")
            print(Fore.GREEN + "[2]" + Style.RESET_ALL + " Gerar múltiplos CPFs")
            print(Fore.BLUE + "[3]" + Style.RESET_ALL + " Visualizar logs do sistema")
            print(Fore.YELLOW + "[4]" + Style.RESET_ALL + " Informações técnicas")
            print(Fore.RED + "[5]" + Style.RESET_ALL + " Sair do sistema\n")
            
            escolha = input("Selecione uma opção: ").strip()

            if escolha == '1':
                cpf = self.gerar_cpf()
                print(Fore.BLUE + f"\nCPF Gerado: {cpf}")
                self._registrar_log(cpf)
                input("\nPressione Enter para continuar...")
            
            elif escolha == '2':
                quantidade = self._validar_entrada_numerica("Quantidade de CPFs a gerar (1-1000): ", 1, 1000)
                print(Fore.BLUE + "\nCPFs Gerados:")
                for _ in range(quantidade):
                    cpf = self.gerar_cpf()
                    print(f"» {cpf}")
                    self._registrar_log(cpf)
                input("\nOperação concluída. Pressione Enter...")
            
            elif escolha == '3':
                self._visualizar_logs()
            
            elif escolha == '4':
                self._exibir_info_sistema()
            
            elif escolha == '5':
                print(Fore.MAGENTA + "\nSistema encerrado com segurança. Até logo!")
                break
            
            else:
                print(Fore.RED + "\nOpção inválida! Use apenas números de 1 a 5.")
                input("Pressione Enter para tentar novamente...")

    def _visualizar_logs(self):
        """Exibe logs de forma segura e paginada"""
        self._limpar_console()
        try:
            with open(self.log_file, 'r') as f:
                logs = [line.strip() for line in f.readlines() if line.strip()]
                
                if not logs:
                    print(Fore.YELLOW + "Nenhum registro de log encontrado.")
                    input("\nPressione Enter para voltar...")
                    return
                
                pagina = 0
                while True:
                    self._limpar_console()
                    print(Fore.CYAN + f" REGISTROS DE LOG ({len(logs)} total) ".center(50, '='))
                    
                    for i in range(pagina*10, min((pagina+1)*10, len(logs))):
                        print(Fore.WHITE + f"{i+1}. {logs[i]}")
                    
                    print(Fore.CYAN + "\n" + "="*50)
                    print(f"Página {pagina+1} de {len(logs)//10 + 1}")
                    print("[A] Anterior | [P] Próxima | [V] Voltar")
                    
                    acao = input("\nAção: ").upper()
                    if acao == 'P' and (pagina+1)*10 < len(logs):
                        pagina += 1
                    elif acao == 'A' and pagina > 0:
                        pagina -= 1
                    elif acao == 'V':
                        break
                    else:
                        print(Fore.RED + "Opção inválida ou fim dos registros!")
                        input("Pressione Enter...")
        
        except Exception as e:
            print(Fore.RED + f"Erro ao acessar logs: {str(e)}")
            input("Pressione Enter para voltar...")

if __name__ == "__main__":
    sistema = CPFGeneratorPro()
    sistema.menu_principal()
