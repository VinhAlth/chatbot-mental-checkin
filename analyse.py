import pandas as pd
from src.prompt import dass21
df = pd.read_csv('/workspace/ai_intern/Shine/perfect/nckh_2024_mentalhealth_chatbot/source/data/test.csv')

from src.predict import Execcute
from src.utils import VistralChatbot

model = Execcute(VistralChatbot())

new_column = []

for index, row in df.iterrows():
    print(f"Tên: {}")
    
new_df = pd.DataFrame(new_column, columns=['Ques_1', 'Ques_2', 'Ques_3', 'Ques_4', 'Ques_5', 'Ques_6', 'Ques_7', 'Ques_8', 'Ques_9', 'ans'])
df = pd.concat([df, new_df], axis=1)

df.to_csv('/workspace/vinhnq/nckh_2024_mentalhealth_chatbot/result/run/score.csv', index=False)
        
        
    