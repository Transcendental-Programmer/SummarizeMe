from transformers import T5Tokenizer, T5ForConditionalGeneration


def t5_summarizer(raw_text):
    t5_model = T5ForConditionalGeneration.from_pretrained('t5-small')
    t5_tokenizer = T5Tokenizer.from_pretrained('t5-small')
    
    inputs = t5_tokenizer.encode("summarize: " + raw_text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = t5_model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = t5_tokenizer.decode(summary_ids[0])
    return summary
