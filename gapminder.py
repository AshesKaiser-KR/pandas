import pandas as pd

df = pd.read_csv('data/gapminder.tsv', sep = '\t')

print(df.head()) # 처음 5개 행
print(type(df)) # dataframe
print(df.shape) # 행, 열
print(df.columns) # 열 이름
print(df.dtypes) # 구성요소 자료형
print(df.info()) # 해당 데이터프레임에 관한 전반적인 정보

country_df = df['country'] # country열만 저장 -> 시리즈형

print(type(country_df)) # series
print(country_df.head())
print(country_df.tail())


