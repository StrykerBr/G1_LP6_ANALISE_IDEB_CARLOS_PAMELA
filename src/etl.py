import os
import zipfile
import pandas as pd

def extrair_e_tratar_dados(zip_path, extract_to="data/raw"):
    """Extrai o ZIP do INEP, lê a planilha e executa o tratamento tabular."""
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(extract_to)
    
    excel_file = [f for f in os.listdir(extract_to) if f.endswith(('.xlsx', '.xls'))][0]
    file_path = os.path.join(extract_to, excel_file)
    
    df = pd.read_excel(file_path, header=9)
    df.iloc[:, 0] = df.iloc[:, 0].fillna('Brasil / Consolidado').ffill()
    df.iloc[:, 1] = df.iloc[:, 1].fillna('Total / Geral')
    df['Regiao_Rede'] = df.iloc[:, 0].astype(str) + ' — ' + df.iloc[:, 1].astype(str)
    
    colunas_ideb = [c for c in df.columns if 'OBSERVADO' in str(c)]
    
    df_melted = pd.melt(df, id_vars=['Regiao_Rede'], value_vars=colunas_ideb, var_name='Ano', value_name='IDEB')
    df_melted['Ano'] = df_melted['Ano'].str.extract(r'(\d{4})')
    df_melted['IDEB'] = pd.to_numeric(df_melted['IDEB'], errors='coerce')
    
    return df_melted.dropna(subset=['IDEB'])

def salvar_dados_processados(df, output_path="data/processed/ideb_regioes_limpo.parquet"):
    """Persiste os dados tratados em formato universal aberto (Parquet)."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"Dados salvos com sucesso em {output_path}")

if __name__ == "__main__":
    print("Módulo ETL carregado com sucesso.")
