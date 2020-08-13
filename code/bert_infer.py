import numpy as np
import torch
from transformers import BertTokenizer, BertForMaskedLM

MODEL_NAME = 'bert-base-multilingual-cased'


def get_topk_predictions(model, tokenizer, text, topk=5):
    encoded_input = tokenizer(text, return_tensors='pt')
    logits = model(encoded_input['input_ids'],
                   encoded_input['token_type_ids'],
                   encoded_input['attention_mask'],
                   masked_lm_labels=None)[0]

    logits = logits.squeeze(0)
    probs = torch.softmax(logits, dim=-1)

    mask_cnt = 0
    token_ids = encoded_input['input_ids'][0]
    
    top_preds = []

    for idx, _ in enumerate(token_ids):
        if token_ids[idx] == tokenizer.mask_token_id:
            mask_cnt += 1
            
            topk_prob, topk_indices = torch.topk(probs[idx, :], topk)
            topk_indices = topk_indices.cpu().numpy()
            topk_tokens = tokenizer.convert_ids_to_tokens(topk_indices)
            for prob, tok_str, tok_id in zip(topk_prob, topk_tokens, topk_indices):
                top_preds.append({'token_str': tok_str,
                                  'token_id': tok_id,
                                  'probability': float(prob)})
    
    return top_preds

def display_topk_predictions(model, tokenizer, text):
    top_preds = get_topk_predictions(model, tokenizer, text)
    for item in top_preds:
        print('{} {}'.format(item['token_str'], item['probability']))

if __name__ == '__main__':
    tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
    model = BertForMaskedLM.from_pretrained(MODEL_NAME)

    while True:
        print('')
        text = input('Input text: ').strip()
        print('-' * 40)
        display_topk_predictions(model, tokenizer, text)
        print('=' * 40)
