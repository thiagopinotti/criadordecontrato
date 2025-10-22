<style type="text/css">
@page {
    margin-top: 10px;   /* remove todas as margens da página */
    margin-bottom: 10px:
}

ol li {
    list-style-type: lower-alpha;
}
ol li::marker {
    font-weight: bold;
}
.produtos {
    width: 100%;
    border-collapse: collapse;  /* importante para unir bordas */
    margin-top: 20px;
}

.produtos th, .produtos td {
    border: 1px solid #333;    /* define borda para cada célula */
    padding: 8px;              /* espaço interno */
    text-align: left;           /* alinhamento do texto */
    vertical-align: top;        /* texto no topo da célula */
}

.produtos th {
    background-color: #f0f0f0; /* cor de fundo do cabeçalho */
    font-weight: bold;
}

.produtos thead {
    display: table-row; /* cabeçalho se repete se desejar */

}
tfoot {
    display: table-row-group; /* faz o footer ser tratado como linha normal, não repetir */
}
</style>

<img src="{{ caminho_imagem }}" style="display:block; margin:0 auto; width:150px; height:auto; margin-top: 0" />
<br>
<center><h3>CONTRATO DE PRESTAÇÃO DE SERVIÇOS</h3></center>



|  |  |
|:------|:------------|
| **Cliente** | {{ nome_cliente }} |
| **Aniversariante** | {{ aniversariante }} |
| **Telefone** | {{ telefone }} |
| **Data do Evento** | {{ data_evento }} |
| **Cerimonial** | {{ cerimonial }} |
| **Tipo de Evento** | {{ tipo_evento }} |
| **Local** | {{ local }} |
|**Horário<br>Entrega ou Retirada** | {{ horario_entrega }} |

---

**CONTRATADA:**<br>
**NOME:** LUANNA ALYSSE DE SOUSA PINOTTI<br>
**CPF:** 798.595.342-68<br>
**ENDEREÇO:** Avenida Duque de Caxias, 160, Apto.301 - Ed. José Bonifácio (frente ao supermercado Formosa)<br>
**TELEFONE:** (91) 98483-6006 // 98442-8433<br>

---

**1. OBJETO DO CONTRATO:**
<p>O presente contrato tem por objetivo, a execução pela CONTRATADA, dos serviços contidos na cláusula 02, subsequente, relacionados com a referência no
presente contrato.</p>

**2. DESCRIÇÃO DOS SERVIÇOS:**
<p>Os serviços a serem executados pela CONTRATADA consistem na produção de Brownies, contemplando nos seguintes itens:</p>

<table class="produtos">
        <tr>
            <th>Quantidade</th>
            <th>Descrição</th>
            <th>Valor Unitário</th>
            <th>Valor Total</th>
        </tr>
    <tbody>
        {% for item in itens %}
        <tr>
            <td>{{ item["Quantidade"] }}</td>
            <td>{{ item["Descrição"] }}</td>
            <td>R$ {{ "%.2f"|format(item['Valor Unitário']) }}</td>
            <td>R$ {{ "%.2f"|format(item['Total Item']) }}</td>
        </tr>
        {% endfor %}
    </tbody>
    <tfoot>
        <tr>
            <td colspan="3"><strong>Total Geral</strong></td>
            <td>
                R$ {{ "%.2f"|format(itens | sum(attribute='Total Item')) }}
            </td>
        </tr>
    </tfoot>
</table>


**3. FORMA DE PAGAMENTO:**
<p> {{ tipo_pag }} – {{ forma_pag }} <br>
{{ dados_pix }}</p>

**4. OBRIGAÇÕES DO CONTRATANTE:**
<ol>
    <li>Fica a CONTRATANTE, responsável pelo pagamento do valor total equivalente a encomenda acima citada em até 48h antes do evento.</li>
    <li>Fica a CONTRATANTE, responsável pela entrega da arte das TAGS para composição da embalagem em até 48H ANTES DO EVENTO;</li>
    <li>Mudanças na embalagem padrão (celofane e laço de cetim ) devem ser informadas com pelos menos 10 dias de antecedência;</li>
</ol>

**5. RESCISÃO DE CONTRATO**<br>
<ol>
   <li>Caso haja a rescisão do contrato por parte do contratante, o mesmo deverá pagar uma multa de 50% sobre o valor total dos serviços contratados.<br>
   <li>Caso haja cancelamento do evento, o CONTRATADO possui até 90 dias após a data pré-estipulada do evento para devolução do valor total devido ao CONTRATADO, exceto 50% da multa.<br>
</ol>

<p><b>Observações</b> {{ observacoes }}</p>
<br>
<br>

<p style="text-align: right;"><b>Belém, {{ data }}</b></p>
<br><br><br><br>

<table style="width:100%; margin-top:50px; border-collapse:separate; border-spacing:40px 0; text-align:center;">
  <tr>
    <!-- Contratada -->
    <td style="width:45%; border-top:1px solid #000; padding-top:15px;">
      <strong>Contratante</strong><br>
    </td>
    <!-- Contratante -->
    <td style="width:45%; border-top:1px solid #000; padding-top:15px;">
      <strong>Contratada</strong><br>

    </td>
  </tr>
</table>





