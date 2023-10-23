
""""
o sistema vai ter as funções

adicionar contato
listar contato
editar contato
excluir contato
buscar contato

a estrutura da agenda será um dicionario de dicionarios para cada contato.


"""
cliente = {

}


planos = {
    "Starter":{
        "Sobre":"Ferramentas de vendas e atendimento ao cliente em um app",
        "Valor": "$25/mês"
    },
    "Sales Professional":{
        "Sobre":"Solução de vendas completa para equipes de qualquer tamanho",
        "Valor": "$80/mês"
    },
    "Enterprise":{
        "Sobre":"CRM de vendas altamente personalizável para o seu negócio",
        "Valor": "$165/mês"
    },
    "Unlimited":{
        "Sobre":"A plataforma definitiva para seu crescimento",
        "Valor": "$330/mês"
    }
}

funcionalidades_starter = ("Gerenciamento de conta, contato, lead e oportunidade", "Integração com Gmail ou Outlook", "Salesforce Mobile App")

funcionalidades_professional = ("Gerenciamento de conta, contato, lead e oportunidade", "Integração com Gmail ou Outlook", "Salesforce Mobile App", 
                                "Registro e pontuação de leads baseada em regras", "Previsão colaborativa")

funcionalidades_enterprise = ("Gerenciamento de conta, contato, lead e oportunidade", "Integração com Gmail ou Outlook", "Salesforce Mobile App", 
                                "Registro e pontuação de leads baseada em regras", "Previsão colaborativa", "Automação de fluxo de trabalho e aprovação")

funcionalidades_unlimited = ("Gerenciamento de conta, contato, lead e oportunidade", "Integração com Gmail ou Outlook", "Salesforce Mobile App", 
                                "Registro e pontuação de leads baseada em regras", "Previsão colaborativa", "Automação de fluxo de trabalho e aprovação",
                                "Serviços de suporte e configuração 24/7 ")

def listar_planos(planos):
    print(f"Estão disponíveis {len(planos)} planos.")
    for plano, infos in planos.items():
        print(f"\n{plano}")
        for descricao, preco in infos.items():
            print(f"{descricao}: {preco}")


def listar_funcionalidades(funcionalidades_enterprise, funcionalidades_professional, funcionalidades_starter, funcionalidades_unlimited):
    while True:
        opcao = input("\nDeseja saber as funcionalidades de um plano especifico?\n 1- Sim \n 2- Não\n")
        if opcao == "1":
            print("\n__PLANOS__\n")
            print("1- Starter \n2- Sales Professional \n3- Enterprise \n4- Unlimited")
            op_func = input("\nDeseja saber as funcionalidades de qual plano?\n")
            if op_func == "1":
                for valores in funcionalidades_starter:
                    print(f"\n{valores}")
            elif op_func == "2":
                for valores in funcionalidades_professional:
                    print(f"\n{valores}")
            elif op_func == "3":
                for valores in funcionalidades_enterprise:
                    print(f"\n{valores}")
            elif op_func == "4":
                for valores in funcionalidades_unlimited:
                    print(f"\n{valores}")
        if opcao == "2":
            break

def cadastrar(cliente, nome, email, telefone, senha):
    novo_cadastro = {}
    novo_cadastro["Email"] = email
    novo_cadastro["Telefone"] = telefone
    novo_cadastro["Senha"] = senha
    cliente[nome] = novo_cadastro
    print(f"{nome} cadastrado com sucesso!")

def excluir_cadastro(cliente):
    cliente.clear()

def menu():
    while True:
        print("\n__SALESFORCE__\n")
        print(" 1. Sobre a Salesforce")
        print(" 2. Contato")
        print(" 3. Planos")
        print(" 4. Cadastro")
        print(" 5. Sair\n")   
        navegador = input("Escolha uma opção:")

        if navegador == "1":
            print("\nA Salesforce é uma empresa de softwares que foca na solução de gerenciamento de relacionamento para aproximar empresas e pessoas. É uma plataforma de CRM integrada que oferece a todos os departamentos uma visão única e compartilhada de cada cliente.")
  
        if navegador == "2":
            print("\nPara entrar em contato, ligue 0800 891 1887. É possível também, entrar em contato através nosso site: https://www.salesforce.com/br/form/contact/contactme/")

        if navegador == "3":
            listar_planos(planos)
            listar_funcionalidades(funcionalidades_enterprise, funcionalidades_professional, funcionalidades_starter, funcionalidades_unlimited)

        if navegador == "4":
            nome  = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            telefone = input("Digite seu telefone: ")
            senha = input("Digite sua senha: ")
            cadastrar(cliente, nome, email, telefone, senha)
            while True:
                print("\n__CADASTRO__\n")
                print("1- Ver cadastro")
                print("2- Refazer cadastro")
                print("3- Excluir cadastro")
                print("4- Voltar")
                cadastro_op = input("Escolha uma opção: ")

                if cadastro_op == "1":
                    for nome, dados in cliente.items():
                        print(f"\n{nome}")
                        for valor, dado in dados.items():
                            print(f"{valor} : {dado}")

                if cadastro_op == "2":
                    excluir_cadastro(cliente)
                    nome  = input("Digite seu nome: ")
                    email = input("Digite seu email: ")
                    telefone = input("Digite seu telefone: ")
                    senha = input("Digite sua senha: ")
                    cadastrar(cliente, nome, email, telefone, senha)

                if cadastro_op == "3":
                    excluir_cadastro(cliente)
                    print("Cadastro excluido com sucesso")

                if cadastro_op == "4":
                    break



        if navegador == "5":
            print("Obrigado, até mais!")
            break
            


if __name__ == "__main__":
    menu()