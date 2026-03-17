import pandas as pd

#ho:kills greatest predictor winning
#ha:adr/damage delta/kast% greatest predictor
#reads the csv 
df = pd.read_csv("valorant-data.csv")

#finds each teams total average kills and variances
df['Team A Average Kills'] = df[['P1 Kills', 'P2 Kills', 'P3 Kills', 'P4 Kills', 'P5 Kills']].mean(axis=1)
df['Team B Average Kills'] = df[['P6 Kills', 'P7 Kills', 'P8 Kills', 'P9 Kills', 'P10 Kills']].mean(axis=1)
df['Team A Average Kills Variance'] = df[['P1 Kills', 'P2 Kills', 'P3 Kills', 'P4 Kills', 'P5 Kills']].var(axis=1)
df['Team B Average Kills Variance'] = df[['P6 Kills', 'P7 Kills', 'P8 Kills', 'P9 Kills', 'P10 Kills']].var(axis=1)

#finds each teams total average adr and variances
df['Team A Average ADR'] = df[['P1 ADR', 'P2 ADR', 'P3 ADR', 'P4 ADR', 'P5 ADR']].mean(axis=1)
df['Team B Average ADR'] = df[['P6 ADR', 'P7 ADR', 'P8 ADR', 'P9 ADR', 'P10 ADR']].mean(axis=1)
df['Team A Average ADR Variance'] = df[['P1 ADR', 'P2 ADR', 'P3 ADR', 'P4 ADR', 'P5 ADR']].var(axis=1)
df['Team B Average ADR Variance'] = df[['P6 ADR', 'P7 ADR', 'P8 ADR', 'P9 ADR', 'P10 ADR']].var(axis=1)

#finds each teams total average damage delta and variances
df['Team A Average DDA'] = df[['P1 DDA', 'P2 DDA', 'P3 DDA', 'P4 DDA', 'P5 DDA']].mean(axis=1)
df['Team B Average DDA'] = df[['P6 DDA', 'P7 DDA', 'P8 DDA', 'P9 DDA', 'P10 DDA']].mean(axis=1)
df['Team A Average DDA Variance'] = df[['P1 DDA', 'P2 DDA', 'P3 DDA', 'P4 DDA', 'P5 DDA']].var(axis=1)
df['Team B Average DDA Variance'] = df[['P6 DDA', 'P7 DDA', 'P8 DDA', 'P9 DDA', 'P10 DDA']].var(axis=1)

#finds each teams total average kast% and variances
df['Team A Average KAST%'] = df[['P1 KAST%', 'P2 KAST%', 'P3 KAST%', 'P4 KAST%', 'P5 KAST%']].mean(axis=1)
df['Team B Average KAST%'] = df[['P6 KAST%', 'P7 KAST%', 'P8 KAST%', 'P9 KAST%', 'P10 KAST%']].mean(axis=1)
df['Team A Average KAST% Variance'] = df[['P1 KAST%', 'P2 KAST%', 'P3 KAST%', 'P4 KAST%', 'P5 KAST%']].var(axis=1)
df['Team B Average KAST% Variance'] = df[['P6 KAST%', 'P7 KAST%', 'P8 KAST%', 'P9 KAST%', 'P10 KAST%']].var(axis=1)

#finds how often the team with higher average kills wins
df['Difference Average Kills'] = df['Team A Average Kills'] - df['Team B Average Kills']
Higher_Kills_Wins = ((df['Difference Average Kills'] > 0) & (df['Winning Team'] == "A")).sum() 
Higher_Kills_Wins += ((df['Difference Average Kills'] < 0) & (df['Winning Team'] == "B")).sum() 

#finds how often the team with higher average adrs wins
df['Difference Average ADR'] = df['Team A Average ADR'] - df['Team B Average ADR']
Higher_ADR_Wins = ((df['Difference Average ADR'] > 0) & (df['Winning Team'] == "A")).sum() 
Higher_ADR_Wins += ((df['Difference Average ADR'] < 0) & (df['Winning Team'] == "B")).sum() 

#finds how often the team with higher average damage deltas wins
df['Difference Average DDA'] = df['Team A Average DDA'] - df['Team B Average DDA']
Higher_DDA_Wins = ((df['Difference Average DDA'] > 0) & (df['Winning Team'] == "A")).sum() 
Higher_DDA_Wins += ((df['Difference Average DDA'] < 0) & (df['Winning Team'] == "B")).sum() 

#finds how often the team with higher average kast% wins
df['Difference Average KAST%'] = df['Team A Average KAST%'] - df['Team B Average KAST%']
Higher_KAST_Wins = ((df['Difference Average KAST%'] > 0) & (df['Winning Team'] == "A")).sum() 
Higher_KAST_Wins += ((df['Difference Average KAST%'] < 0) & (df['Winning Team'] == "B")).sum() 

#finds how often the team with lower average kills variance wins
df['Difference Average Kills Variance'] = df['Team A Average Kills Variance'] - df['Team B Average Kills Variance']
Lower_Kills_Variance_Wins = ((df['Difference Average Kills Variance'] < 0) & (df['Winning Team'] == "A")).sum() 
Lower_Kills_Variance_Wins += ((df['Difference Average Kills Variance'] > 0) & (df['Winning Team'] == "B")).sum() 

#finds how often the team with lower average adrs variance wins
df['Difference Average ADR Variance'] = df['Team A Average ADR Variance'] - df['Team B Average ADR Variance']
Lower_ADR_Variance_Wins = ((df['Difference Average ADR Variance'] < 0) & (df['Winning Team'] == "A")).sum() 
Lower_ADR_Variance_Wins += ((df['Difference Average ADR Variance'] > 0) & (df['Winning Team'] == "B")).sum() 

#finds how often the team with lower average damage deltas variance wins
df['Difference Average DDA Variance'] = df['Team A Average DDA Variance'] - df['Team B Average DDA Variance']
Lower_DDA_Variance_Wins = ((df['Difference Average DDA Variance'] < 0) & (df['Winning Team'] == "A")).sum() 
Lower_DDA_Variance_Wins += ((df['Difference Average DDA Variance'] > 0) & (df['Winning Team'] == "B")).sum() 

#finds how often the team with lower average kast% variance wins
df['Difference Average KAST% Variance'] = df['Team A Average KAST% Variance'] - df['Team B Average KAST% Variance']
Lower_KAST_Variance_Wins = ((df['Difference Average KAST% Variance'] < 0) & (df['Winning Team'] == "A")).sum() 
Lower_KAST_Variance_Wins += ((df['Difference Average KAST% Variance'] > 0) & (df['Winning Team'] == "B")).sum() 

#correlational analysis
print(f"Higher Average Kills Winrate: {Higher_Kills_Wins/len(df):.1%}")
print(f"Higher Average ADR Winrate: {Higher_ADR_Wins/len(df):.1%}")
print(f"Higher Average DDA Winrate: {Higher_DDA_Wins/len(df):.1%}")
print(f"Higher Average KAST% Winrate: {Higher_KAST_Wins/len(df):.1%}")
print(f"Lower Average Kills Variance Winrate: {Lower_Kills_Variance_Wins/len(df):.1%}")
print(f"Lower Average ADR Variance Winrate: {Lower_ADR_Variance_Wins/len(df):.1%}")
print(f"Lower Average DDA Variance Winrate: {Lower_DDA_Variance_Wins/len(df):.1%}")
print(f"Lower Average KAST% Variance Winrate: {Lower_KAST_Variance_Wins/len(df):.1%}")


