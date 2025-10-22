from jinja2 import Environment, FileSystemLoader
import markdown
from weasyprint import HTML
import os
from num2words import num2words

# --- Dados vindos do formulário ---
# dados = {
#     "cliente": "Maria Fernanda Costa",
#     "aniversariante": "João Pedro",
#     "telefone": "(91) 99999-9999",
#     "data_evento": "12/11/2025",
#     "cerimonial": "Luanna Pinotti Cerimonial",
#     "evento": "Festa de Aniversário Infantil",
#     "local_horario": "Buffet Alegria - 17h"
# }

# itens = [
#     {"quantidade": 2, "descricao": "Brownie Tradicional", "valor_unitario": 27.50, "valor_total": 55.00},
#     {"quantidade": 1, "descricao": "Brownie Chocolate Branco", "valor_unitario": 30.00, "valor_total": 30.00},
#     {"quantidade": 3, "descricao": "Brownie Meio Amargo", "valor_unitario": 28.00, "valor_total": 84.00},
# ]

def gerar_pdf(dados, itens):

    caminho_imagem = os.path.abspath("sresrabrownies.png")
    dados["caminho_imagem"] = caminho_imagem
    dados["itens"] = itens

    print(dados)

    #convertendo numero em texto
    valor_total_geral = sum(item["Total Item"] for item in itens)
    numero_por_extenso = num2words(valor_total_geral, to='currency', lang='pt_BR')
    dados["total_extenso"] = numero_por_extenso.title()

    # --- Carrega o template Markdown ---
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('sresrabrownies/template_contrato.md')

    # --- Renderiza o Markdown com os dados ---
    md_renderizado = template.render(**dados)

    # --- Converte Markdown → HTML ---
    html = markdown.markdown(md_renderizado, extensions=['extra'])

    # --- Gera o PDF com WeasyPrint ---
    HTML(string=html, base_url='.').write_pdf("ficha_evento.pdf")

    print("✅ PDF gerado com sucesso: ficha_evento.pdf")
