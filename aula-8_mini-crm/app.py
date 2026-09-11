
from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    status = input("Status do fluxo de vendas: ")

    # Validar dados
    # agora, preciso modelar os dados
    # para isso, vamos usar o modulo model.py
    #preciso modelar os dados
    print(model_lead.create(name, email, status))

    # com os dados modelados preciso enviar pro json
    # vou usar o control para enviar o dicionario do lead
    control.create_lead(model_lead.create(name, email, status))
    print("Lead adicionado com sucesso")

def list_leads():
    leads = control.read_leads()
    print(leads)

def main():
    while True:
        print("\nmini CRM de Lead")
        print("[1] Adicionar Lead")
        print("[2] Listar Lead")
        print("[0] sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    main()
