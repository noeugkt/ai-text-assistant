def create_summary_prompt(text):
    prompt = f"""
Summarize the following text.

Also provide the 3-5 main key points.

Text:
    {text}
    """
    return prompt
