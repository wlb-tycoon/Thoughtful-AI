# thoughtful_ai_agent.py

import json
from fuzzywuzzy import process

# Load predefined data from JSON file
def load_predefined_data(file_path):
    """Load the predefined questions and answers from a JSON file."""
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def get_most_relevant_answer(user_question, predefined_data):
    """Retrieve the most relevant answer using fuzzy matching."""
    # Extract all predefined questions
    questions = [qa["question"] for qa in predefined_data["questions"]]
    
    # Find the closest match using fuzzywuzzy
    closest_match, similarity_score = process.extractOne(user_question, questions)
    
    # If the similarity score is above a threshold, return the corresponding answer
    if similarity_score > 70:  # Adjust threshold as needed
        for qa in predefined_data["questions"]:
            if qa["question"] == closest_match:
                return qa["answer"]
    
    # Fallback response if no close match is found
    return "I'm sorry, I don't have information on that. Please contact Thoughtful AI support for further assistance."

def main():
    # Load predefined data
    predefined_data = load_predefined_data("data/predefined_data.json")
    
    print("Welcome to the Thoughtful AI Customer Support Agent!")
    print("You can ask me questions about Thoughtful AI's Agents. Type 'exit' to quit.")
    
    while True:
        user_input = input("\nWhat would you like to know? ")
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day.")
            break
        
        answer = get_most_relevant_answer(user_input, predefined_data)
        print(f"\n{answer}")

if __name__ == "__main__":
    main()