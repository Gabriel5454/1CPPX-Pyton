from operator import truediv

endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

def erros_seguidos(requisicoes):
    for i in range(len(requisicoes) -1):
        codigo_atual = requisicoes[i]
        prox_codigo = requisicoes[i+1]
        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

def analisar_endpoint(requisicoes):
    qtd_sucesoos = 0
    for codigo in requisicoes:
        if eh_sucesso(codigo):
            qtd_sucesoos += 1
    qtd_total_req = len(requisicoes)
    qtd_erros = qtd_total_req - qtd_sucesoos
    percentual_sucessos = (qtd_sucesoos / qtd_total_req) * 100

    tem_erros_seguidos = erros_seguidos(requisicoes)

    if tem_erros_seguidos:
        classificacao = "Critico"
    elif percentual_sucessos >= 80:
        classificacao = "Estavel"
    else:
        classificacao = "Instável"
    return (qtd_sucesoos, qtd_erros, percentual_sucessos, classificacao)

maior_qtd_erros = -1
endpoint_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    reqs_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(reqs_endpoint)

    print(f'Endpoint: {nome_endpoint}')
    print(f'Requisições: {reqs_endpoint}')
    print(f'Sucessos: {sucessos}')
    print(f'Erros: {erros}')
    print(f'Percentual: {percentual}')
    print(f'Classificao: {classificacao}')
    print("-"* 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erro = nome_endpoint

print(f"Endpoin + erros: {endpoint_maior_erro}")