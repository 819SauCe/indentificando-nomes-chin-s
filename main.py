import pandas as pd
df = pd.read_excel('Fornecedores.xlsx')

palavras_chaves = [
    'china', 'taiwan', 'Provincia da China', 'Shangai', 'Zhejiang', 
    'Pequim', 'Xangai', 'Hong Kong', 'Shenzhen', 'Guangzhou', 
    'Chengdu', 'Xi\'an', 'Hangzhou', 'Nanjing', 'Wuhan', 
    'Suzhou', 'Chongqing', 'Tianjin', 'Qingdao', 'Jinan', 
    'Xiamen', 'Dalian', 'Zhengzhou', 'Ningbo', 'Harbin',
    'ZHEJIANG', 'R.S.', 'YANCHENG', 'ZHEJIANG', 'ORIENT', 
    'SHAOXING', 'CHONGQUING', 'YANCHENG', 'YANCHENG', 
    'SHAANXI', 'ZHEJIANG', 'JIANGSU', 'SHANGHAI', 
    'TOPSCIEN', 'ZHEJIANG', 'SHANGHAI', 'BIOBASE', 
    'SUNOSTIK', 'ZHEJIANG', 'HANGZHOU', 'ZHOUSHAN', 
    'WIDESKY', 'TINKO', 'NINGBO', 'NANTONG', 'SHANGHAI', 
    'NANYANG', 'HUNAN', 'CHANGSHA', 'INESA', 
    'SHANGHAI', 'COSCO', 'SHENZHEN', 'UNITED', 
    'NINGBO', 'ZHANJIANG', 'OPTO-EDU', 'ANHUI', 
    'ZHEJIANG', 'HEREXI', 'LACHOI', 'SRATE', 
    'XINCHEG', 'FOSHAN', 'BONOMO', 'NINGBO', 
    'SHANGHAI', 'JIANGSU', 'TAIAN', 'LIAONING', 
    'ZHEJIANG', 'CITOTEST', 'QINGZHOU', 'MIULAB', 
    'WUXI', 'GUANGDONG', 'JIANGSU', 'JOAN'
]

string_cols = df.select_dtypes(include=['object']).columns
filtro = df[string_cols].apply(lambda x: x.str.contains('|'.join(palavras_chaves), case=False, na=False)).any(axis=1)
linhas_filtradas = df[filtro]
linhas_filtradas.to_excel('linhas_filtradas.xlsx', index=False)

print("Linhas filtradas salvas em 'linhas_filtradas.xlsx'.")
