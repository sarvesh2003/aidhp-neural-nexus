import pandas as pd
import numpy as np
from langchain.docstore.document import Document

# Data Loading and Modifications
df = pd.read_csv("../data/enriched_accounts_new.csv", delimiter='\t')
df['queryFormat'] = df.apply(lambda row: f"Based on the following customer data: {row.to_dict()}, suggest suitable banking lending products", axis=1)
print(df.head(4)['queryFormat'][0])
# # Langchain
# documents = []
# for _, row in df.iterrows():
#     documents.append(Document(row['queryFormat'], metadata={"class": row["Age"]}))


# For every query by the user, try to include some product recommendations if possible
df.to_csv('../data/enriched_accounts_new_with_queryFormat.csv')
