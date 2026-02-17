import  streamlit as st
import pandas as pd
from datetime import datetime

from gerar_pdf import gerar_pdf

placeholder = "escolha a opção"
valor_total = None
forma_pag = None

data = datetime.now().strftime("%d de %B de %Y")

_, center, _ = st.columns([2,2,2])
center.image('./sresrabrownies/assets/sresrabrownies.png', width=200, use_container_width=True)

st.markdown("<h3 style='text-align: center;'>CONTRATO DE PRESTAÇÃO DE SERVIÇOS</h3>", unsafe_allow_html=True)

# CONTROLE DE TELA
if "etapa" not in st.session_state:
    st.session_state.etapa = 1  # começa no formulário 1
if "cliente" not in st.session_state:
    st.session_state.cliente = {}
if "itens" not in st.session_state:
    st.session_state.itens = []

# TELA CLIENTE
if st.session_state.etapa == 1:
    st.header("Cadastro Cliente")

    tipo_evento = st.selectbox(
        'Tipo Evento',
        ['Casamento', '15 anos', 'Outros'],
        index=['Casamento', '15 anos', 'Outros'].index(
            st.session_state.cliente.get("tipo_evento", "Casamento")
        )
    )

    if tipo_evento == "Casamento":
        label_aniversariante = "Nome dos Noivos"
    elif tipo_evento == "15 anos":
        label_aniversariante = "Nome da Debutante"
    else:
        label_aniversariante = "Nome do Aniversariante"

    with st.form('Cadastro Cliente'):
        nome_cliente = st.text_input('Cliente', value=st.session_state.cliente.get("nome_cliente", ""))
        aniversariante = st.text_input(label_aniversariante,
                                       value=st.session_state.cliente.get("aniversariante", ""))
        telefone = st.text_input('Telefone', value=st.session_state.cliente.get("telefone", ""))
        data_evento = st.date_input('Data do Evento', value=st.session_state.cliente.get("data_evento", None))
        cerimonial = st.text_input('Cerimonial', value=st.session_state.cliente.get("cerimonial", ""))
        local = st.text_input('Local do Evento/Entrega', value=st.session_state.cliente.get("local", ""))
        horario_entrega = st.text_input('Horario da Entrega', value=st.session_state.cliente.get("horario_entrega", ""))
        observacoes = st.text_input('Observações', value=st.session_state.cliente.get("observacoes", ""))

        salvar = st.form_submit_button('Salvar')

        if salvar:
            st.session_state.cliente = {
                'nome_cliente': nome_cliente,
                'tipo_evento': tipo_evento,
                'aniversariante': aniversariante,
                'telefone': telefone,
                'data_evento': data_evento,
                'cerimonial': cerimonial,
                'local': local,
                'horario_entrega': horario_entrega,
                'observacoes': observacoes,
                'data': data
            }
            st.session_state.etapa = 2
            st.rerun()

# TELA FORMAR DE PAGAMENTO E ITENS 
elif st.session_state.etapa == 2:
    st.write("### Forma de Pagamento")
    
    tipo_pag = st.selectbox(label='Tipo Pagamento',
                            options=['PIX', 'Cartão', 'Dinheiro', 'Outros'],
                            index=None, 
                            placeholder=placeholder)
    st.session_state.cliente['tipo_pag'] = tipo_pag
    if tipo_pag == 'PIX':
        st.session_state.cliente['dados_pix'] = 'CHAVE CPF: 25812580391' \
        '| Banco Inter | Francisca Carmem de Sousa Yokoyama'
    else:
        st.session_state.cliente['dados_pix'] = ''

    if tipo_pag is not None and tipo_pag != 'Outros':
        forma_pag = st.selectbox(label='Forma Pagamento',
                                    options=['50%', 'Á vista'],
                                    index=None,
                                    placeholder=placeholder)


    obs_pag = "Observações - " + st.text_input('Observações')
    st.session_state.cliente['obs_pag'] = obs_pag

    with st.form("form_itens", clear_on_submit=True):


        st.write("### Adicionar Itens")
        qtd = st.number_input("Quantidade", min_value=1, step=1)
        descricao = st.text_input("Descrição")
        valor_unit = st.number_input("Valor Unitário (R$)", min_value=0.0, step=0.01)
        add_item = st.form_submit_button("Adicionar Item")

        if add_item and descricao:
            total_item = qtd * valor_unit
            st.session_state.itens.append({
                "Quantidade": qtd,
                "Descrição": descricao,
                "Valor Unitário": valor_unit,
                "Total Item": total_item
            })
            st.success(f"Item '{descricao}' adicionado!")

    if st.session_state.itens:
        st.write("### Itens adicionados:")
        # Cabeçalho da tabela
        cabecalho = st.columns([1, 4, 2, 2, 1])
        cabecalho[0].markdown("**Qnt**")
        cabecalho[1].markdown("**Descrição**")
        cabecalho[2].markdown("**Valor Unitário**")
        cabecalho[3].markdown("**Total Item**")
        cabecalho[4].markdown("**🗑️**")

        # Linhas com dados e botão "Remover"
        for i, item in enumerate(st.session_state.itens):
            cols = st.columns([1, 4, 2, 2, 1])
            cols[0].write(item["Quantidade"])
            cols[1].write(item["Descrição"])
            cols[2].write(f"R$ {item['Valor Unitário']:.2f}")
            cols[3].write(f"R$ {item['Total Item']:.2f}")
            if cols[4].button("❌", key=f"remover_{i}"):
                st.session_state.itens.pop(i)
                st.rerun()

        # Exibe total geral
        itens_df = pd.DataFrame(st.session_state.itens)
        valor_total = itens_df['Total Item'].sum()
        st.markdown(f"**Total Geral: R$ {valor_total:.2f}**")

        st.session_state.cliente['valor_total'] = float(valor_total)
                
        if st.button("⬅️ Voltar aos Dados do Cliente"):
            st.session_state.etapa = 1
            st.rerun()
    
    if forma_pag == '50%':
        forma_pag = f"Entrada de 50% ({ valor_total / 2 }) e o restante" \
        " em até 72h ao evento."
    elif forma_pag == 'Á vista':
        forma_pag = 'Á Vista.'

    st.session_state.cliente['forma_pag'] = forma_pag
    

    if st.button('Criar Contrato'):
        caminho_pdf = gerar_pdf(st.session_state.cliente, st.session_state.itens)
        with open(caminho_pdf, "rb") as file:
            st.download_button(
                label="📄 Baixar Contrato em PDF",
                data=file,
                file_name="contrato.pdf",
                mime="application/pdf"
            )




