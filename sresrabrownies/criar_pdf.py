from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER
from PIL import Image

# --- Configurações do documento ---
pdf_file = "exemplo_formatado.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
width, height = A4

# --- Caminho da imagem ---
imagem = "./sresrabrownies.png"

# --- Ajusta tamanho da imagem proporcionalmente ---
img_width = 100
img = Image.open(imagem)
aspect = img.height / img.width
img_height = img_width * aspect

# Cria objeto de imagem centralizada
img_element = RLImage(imagem, width=img_width, height=img_height)
img_element.hAlign = 'CENTER'

# --- Estilos de texto ---
styles = getSampleStyleSheet()

# Cria um estilo customizado para o corpo
body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=12,
    leading=16,  # espaçamento entre linhas
)

# --- Texto com formatação rica ---
long_text = """CONTRATO DE PRESTAÇÃO DE SERVIÇOS
Thaillane Francinete de Lisboa Castro
CLIENTE:
ANIVERSARIANTE:
TELEFONE:
NICOLE LISBOA
DATA DO EVENTO:03/06/2026
CERIMONIALMS ASSESSORIA & CERIMONIAL @scmarcelosilva
EVENTO:15 anos
LOCAL / HORÁRIO DA
ENTREGA ou RETIRADALE LYS MAISON
CONTRATADA:
NOME: LUANNA ALYSSE DE SOUSA PINOTTI
CPF: 798.595.342-68
ENDEREÇO: Avenida Duque de Caxias, 160, Apto.301 - Ed. José Bonifácio
(Bem em frente ao supermercado Formosa)
TELEFONE: (91) 98483-6006 // 98442-8433
1.
OBJETO DO CONTRATO:
O presente contrato tem por objetivo, a execução pela CONTRATADA, dos
serviços contidos na cláusula 02, subsequente, relacionados com a referência no
presente contrato.
2.
DESCRIÇÃO DOS SERVIÇOS:
Os serviços a serem executados pela CONTRATADA consistem na produção de
Brownies, contemplando nos seguintes itens:
"""

paragraph = Paragraph(long_text, body_style)

# --- Monta o conteúdo do PDF ---
content = [
    Spacer(1, 20),  # espaço superior
    img_element,
    Spacer(1, 30),  # espaço abaixo da imagem
    paragraph
]

# --- Gera o PDF ---
doc.build(content)

print("✅ PDF gerado com sucesso:", pdf_file)





