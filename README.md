# AI Text Assistant

A simple command-line Python application that reads a text file, sends the content to an LLM API, and returns a summary and a few key points.

## Features

- Read text from a txt file
- Builds a summary prompt
- Send requests to an LLM API
- Load API keys from a `.env` file
- Handle HTTP errors
- Extract the generated text from the API response
- Includes automated tests with `pytest`

## Project Structure

```text
ai-text-assistant/
├── app.py
├── api_client.py
├── file_utils.py
├── prompts.py
├── article.txt
├── requirements.txt
├── tests/
└── .gitignore 
```

## Setup

Clone the repository: 

```bash
git clone https://github.com/noeugkt/ai-text-assistant.git
cd ai-text-assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## API Key

Create a `.env` file in the project directory:

```text
OPENAI_API_KEY=your_api_key_here
```

## Usage 

Put the text that you want to summarize inside `article.txt`

Then run:

```bash 
python app.py
```

the program will return a summary along with key points.

## Example

Example input:
```

Artificial intelligence is increasingly used in software applications..

```

Example Output:

```
Summary: 
Artificial intelligence is becoming widely used...

Key points:
- AI is used in many applications
- AI systems process large amounts of data
- Software engineering is important for AI systems
```

## Running Tests

Run the tests with:

```bash
python -m pytest
```

## What I learned 

- Python functions and modules
- File handling
- HTTP APIs
- JSON
- Environment variables
- Error handling
- Git and GitHub
- Virtual environments
- Automated testing with pytest
