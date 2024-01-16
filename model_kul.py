from keybert import KeyBERT
import pickle
import numpy as np
from tqdm.notebook import tqdm
from transformers import DistilBertTokenizerFast
import torch 


tokenizer = DistilBertTokenizerFast.from_pretrained('tokenizer_')

model = torch.load('distilbert_model.pt')

Kmodel = KeyBERT()

def extract_keywords(text):
    keywords = [Kmodel.extract_keywords(text, stop_words=None,top_n=int(0.7*len(text.split())))]
    return np.array([' '.join(k[0] for k in keyword_list) for keyword_list in keywords])

def result(text):
    final_test_data=extract_keywords(text)
    tokenized_final=tokenizer(final_test_data.tolist(), padding=True,truncation=True,return_tensors='pt')

    model.eval()
    with torch.no_grad():
        input_ids,attention_mask=tokenized_final['input_ids'],tokenized_final['attention_mask']
        output=model(input_ids,attention_mask=attention_mask)
        probabilities = torch.softmax(output.logits, dim=1)
        prob,ans = torch.max(probabilities, dim =1)
    return ans.item(), prob.item()






