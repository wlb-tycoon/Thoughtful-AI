# Thoughtful AI Customer Support Agent

Welcome to the **Thoughtful AI Customer Support Agent** repository! This project is a simple conversational AI agent designed to assist users with basic questions about Thoughtful AI's suite of automation agents. The agent uses a predefined dataset of questions and answers stored in a JSON file to provide relevant responses.

---

## Features

- **Predefined Dataset**: The agent uses a JSON file (`data/predefined_data.json`) to store questions and answers about Thoughtful AI's agents.
- **Fuzzy Matching**: The agent uses fuzzy string matching to find the most relevant answer even if the user's input isn't an exact match.
- **User-Friendly CLI**: The agent runs in a command-line interface (CLI), making it easy to interact with.
- **Fallback Response**: If no relevant answer is found, the agent provides a generic fallback response.

---

## Getting Started

### Prerequisites

- Python 3.x
- `fuzzywuzzy` library (for fuzzy string matching)
- `python-Levenshtein` (optional, for faster performance)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/thoughtful-ai-agent.git
   cd thoughtful-ai-agent
   ```

2. Install the required dependencies:

   pip install -r requirements.txt

### Usage

1. Run the AI agent:

```
python thoughtful_ai_agent.py
```

2. Interact with the agent by typing your questions. For example:

```
What does the eligibility verification agent (EVA) do?
```

3. Type `exit` to quit the conversation.

### Predefined Dataset

The predefined dataset is stored in data/predefined_data.json. You can modify this file to add or update questions and answers.

### Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.

2. Create a new branch (`git checkout -b feature/YourFeatureName`).

3. Commit your changes (`git commit -m 'Add some feature'`).

4. Push to the branch (`git push origin feature/YourFeatureName`).

5. Open a pull request.
