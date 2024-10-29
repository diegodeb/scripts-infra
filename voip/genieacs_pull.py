import requests
import json

# Defina a URL do servidor GenieACS
base_url = "http://ifrit.sti.ufrn.br:7557"

def format_script(script):
    """Formata o script para adicionar quebras de linha e identação."""
    return "\n".join(line.strip() for line in script.splitlines())

def get_provisions():
    """Faz uma requisição GET para buscar todas as provisions e salva em um JSON formatado."""
    url = f"{base_url}/provisions/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        provisions = response.json()  # Converte a resposta para um dicionário JSON

        # Formatar o campo script em cada provision
        for provision in provisions:
            if "script" in provision:
                provision["script"] = format_script(provision["script"])

        # Salva o conteúdo formatado em um arquivo JSON legível
        with open("provisions_formatted.json", "w", encoding="utf-8") as f:
            json.dump(provisions, f, indent=4, ensure_ascii=False)

        print("Dados das provisions salvos em 'provisions_formatted.json'.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar provisions: {e}")

if __name__ == "__main__":
    get_provisions()

