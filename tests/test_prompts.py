from prompts import create_summary_prompt


def test_create_summary_prompts():
    text = "Python is fun."

    prompt = create_summary_prompt(text)

    assert "Python is fun." in prompt
