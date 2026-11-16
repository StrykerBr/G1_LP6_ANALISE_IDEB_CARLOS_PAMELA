# Dicionário de Dados - Análise do IDEB (2005–2025)

Este documento descreve as variáveis presentes no conjunto de dados processado (`data/processed/ideb_regioes_limpo.parquet`), atendendo aos princípios FAIR de interoperabilidade.

| Nome da Variável | Significado de Pesquisa / Negócio | Tipo Primitivo | Domínio / Formato |
| :--- | :--- | :--- | :--- |
| `Regiao_Rede` | Grande região geográfica combinada com a rede de ensino | `string` | Categoria textual |
| `Ano` | Ano de referência da medição oficial do IDEB | `int64` | Anos de 2005 a 2025 |
| `IDEB` | Nota ou projeção observada no indicador de qualidade | `float64` | Escala contínua de 0.0 a 10.0 |
