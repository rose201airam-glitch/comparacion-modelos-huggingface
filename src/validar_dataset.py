import pandas as pd
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data'/'mensajes.csv'
df=pd.read_csv(p,encoding='utf-8-sig')
assert len(df)==36 and df.id.is_unique
assert set(df.etiqueta)=={'positivo','neutral','negativo'}
assert not df.isna().any().any()
print('Dataset validado:',len(df),'registros')
