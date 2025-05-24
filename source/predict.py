import pandas as pd
from src.prompt import dass21
df = pd.read_csv('/workspace/ai_intern/Shine/perfect/nckh_2024_mentalhealth_chatbot/source/data/final.csv')

from src.predict import Execcute
from src.utils import VistralChatbot

model = Execcute(VistralChatbot())

new_column = []

for index, row in df.iterrows():
    column = []
    ans = 0
    name = row[1]
    i1 = 2
    i2 = 11
    for i in range(9):
         
        conv = dass21[i+1] + "\nSinh viên: " + row[i2]
        pred = model.execcute(conv)
        print(f"Predict: {pred}. Ans1: {row[i1][0]}. Answer: {row[i2]}")
        ans += +(str(pred) == str(row[i1][0]))
        i1+=1
        i2+=1
        column.append(pred)
    column.append(ans)
    new_column.append(column)
    # break
    
new_df = pd.DataFrame(new_column, columns=['Ques_1', 'Ques_2', 'Ques_3', 'Ques_4', 'Ques_5', 'Ques_6', 'Ques_7', 'Ques_8', 'Ques_9', 'ans'])
df = pd.concat([df, new_df], axis=1)

df.to_excel('/workspace/vinhnq/nckh_2024_mentalhealth_chatbot/result/run/final.xlsx', index=False)
        
        
    