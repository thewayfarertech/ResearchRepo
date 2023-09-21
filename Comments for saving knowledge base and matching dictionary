#####################################################
# Codes to build a Chatbot that learns from the user
#####################################################


import json
from difflib import get_close_matches       # allows to match the best response to the user input into chatbot
from typing import Union


# load knowledge base from a JSON file
def load_knowledge_base(file_path: str) -> dict:    # function load_knowledge_base is created and returns as a dictionary containing loaded knowledge base
    with open(file_path, 'r') as file:              # open the file path in read mode as 'file'
        data: dict = json.load(file)                # load JSON data from file into the dictionary; JSON data changed to Python object
    return data                                     # function returns to the loaded dictionary


# save the dictionary to the knowledge base; old responses will load in the future
def save_knowledge_base(file_path: str, data: dict):        # function 'save_knowledge_base'. 'file_path' is the path to the file where the JSON file will be saved; 'data' is the Python dictionary to be saved.
    with open(file_path, 'w') as file:                      # open the file path in write mode as 'file'
        json.dump(data, file, indent=2)                     # write the 'data' into a JSON-formatted text and write into the file with 2-space indentation


# finding best match from the dictionary
def find_best_match(user_question: str, questions: list[str]) -> Union[str, None]:      #   A user question and a list of exisiting questions are taken. The function returns the best matching question or none.
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)        #   'get_close_matches' finds the best match within the 'questions' list. n = 1 is best match, and matches over 0.6 similarity will be considered
    return matches[0] if matches else None                                              #   function will return the best match or 'None' if no suitable match was found.



# function to answer each question
def get_answer_for_question(question: str, knowledge_base: dict) -> Union[str, None]:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

# chat_bot() function
def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:                                 # create infinite loop
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_match: Union[str, None] = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you! I learned a new response!')


if __name__ == '__main__':
    chat_bot()
