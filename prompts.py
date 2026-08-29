def create_summary_prompt(text):
    prompt = f"""
Summarize the following text.

Also provide the main key points.

Text:
    {text}
    """
    return prompt
