import json
from faker import Faker

def gerar_dados_pessoas():
    fake = Faker('pt_BR')

    pessoas = []
    for _ in range(10):
        pessoa = {
            'nome': fake.name(),
            'data_nascimento': fake.date_of_birth().strftime('%Y-%m-%d'),
            'endereco': fake.address().replace('\n', ', ')
        }
        pessoas.append(pessoa)

    return pessoas

dados_pessoas = gerar_dados_pessoas()

# Salvar os dados em um arquivo JSON
with open('dados_pessoas.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados_pessoas, arquivo_json, ensure_ascii=False, indent=4)

print("Arquivo JSON gerado com sucesso!")
