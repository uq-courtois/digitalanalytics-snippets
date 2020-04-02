df = pd.read_csv('imdb_data_recoded.csv', sep = ';') # Import data

df['sfxgenre'] = df['genres'].apply(lambda x: 'higher sfx' if 'Action' in x or 'Fantasy' in x or 'Sci-Fi' in x or 'Adventure' in x or 'Animation' in x else 'lower sfx')

print(df[['genres','sfxgenre']])
