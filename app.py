import file_utils
import api_client
import prompts

def main():
    article = file_utils.read_text("article.txt")
    prompt = prompts.create_summary_prompt(article)
    answer = api_client.ask_llm(prompt)
    print(f'this is the answer: {answer}')

if __name__ == "__main__":
    main()
