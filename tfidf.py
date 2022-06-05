from sklearn.feature_extraction.text import TfidfVectorizer
import json
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import numpy as np
import pandas as pd


df = pd.read_csv('news_data.csv')
print(len(df))
len(df)
corpus = [x for x in df.to_dict(orient='index').values()]
docs = [row['title'] for row in corpus if len(str(row.get('title'))) > 10]
print(len(docs))
len(docs)
    

vectorizer = TfidfVectorizer()
tfidf_docs = vectorizer.fit_transform(docs)
print(tfidf_docs.shape, len(vectorizer.vocabulary_))
print(list(vectorizer.vocabulary_.keys())[:10])

# query
query = 'حذف فقر'
tfidf_query = vectorizer.transform([query])[0]

# similarities
cosines = []
for d in tqdm(tfidf_docs):
  cosines.append(float(cosine_similarity(d, tfidf_query)))
  
# sorting
k = 10
sorted_ids = np.argsort(cosines)
for i in range(k):
  cur_id = sorted_ids[-i-1]
  print(docs[cur_id], cosines[cur_id])
  