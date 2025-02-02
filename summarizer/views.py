from django.shortcuts import render
from transformers import pipeline


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        # Summarize the text
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        summarized_text = summary[0]['summary_text']
        return render(request, 'summarizer/result.html', {'summary': summarized_text})
    return render(request, 'summarizer/index.html')