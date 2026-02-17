from jinja2 import Environment, FileSystemLoader
import markdown
from weasyprint import HTML
from pathlib import Path
from num2words import num2words

def gerar_pdf(dados, itens):
    # Caminho base para os assets, relativo a este arquivo
    pasta_assets = Path(__file__).parent / "assets"
    
    # Caminho da imagem dentro da pasta assets
    caminho_imagem = pasta_assets / "sresrabrownies.png"
    dados["caminho_imagem"] = str(caminho_imagem)  # converte para string
    dados["itens"] = itens

    print(dados)

    # Convertendo número em texto
    valor_total_geral = sum(item["Total Item"] for item in itens)
    numero_por_extenso = num2words(valor_total_geral, to='currency', lang='pt_BR')
    dados["total_extenso"] = numero_por_extenso.title()

    # --- Carrega o template Markdown da pasta assets ---
    env = Environment(loader=FileSystemLoader(str(pasta_assets)))
    template = env.get_template('template_contrato.md')

    # --- Renderiza o Markdown com os dados ---
    md_renderizado = template.render(**dados)
    
    # --- Converte Markdown → HTML ---
    html = markdown.markdown(md_renderizado, extensions=['extra'])

    # --- Gera o PDF com WeasyPrint ---
    output_pdf = pasta_assets / "ficha_evento.pdf"
    HTML(string=html, base_url=str(pasta_assets)).write_pdf(str(output_pdf))

    print(f"✅ PDF gerado com sucesso: {output_pdf}")

    # Retorna o caminho absoluto do PDF gerado
    return str(output_pdf)
