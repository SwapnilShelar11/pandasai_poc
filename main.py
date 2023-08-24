import time

import pandas as pd
from pandasai import PandasAI


# Sample DataFrame
df = pd.read_csv(r'/Users/Swapnil179353/PycharmProjects/practice/gen_ai_usecase/Product Dataset.csv')
print(df.head(10))

# from pandasai.llm.openai import OpenAI
#
# # Assigning API key
# llm = OpenAI(api_token="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")
#
# # Calling PandasAI
# pandas_ai = PandasAI(llm)
#
# response = pandas_ai(df, prompt='latitude of AM country')
#
# print(response)

# pandas_ai([employees_df, salaries_df], "Which employee has the largest salary?")