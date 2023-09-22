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
def get_answer_for_question(question: str, knowledge_base: dict) -> Union[str, None]:       # function to find the answer to a given question from a given knwoledge base
    for q in knowledge_base["questions"]:                                                   # loop over all question-answer pair in the knowledge base
        if q["question"] == question:                                                       # check if the current question in the loop matches the user's question
            return q["answer"]                                                              # if not match is found, function will return "None" by default

# BELOW IS THE NEW, MY OWN CODES
# Display a list of questions from knowledge base
def list_all_questions(knowledge_base: dict):                                           # extract questions list from the knowledge base
    questions = knowledge_base["questions"]
    print("List of Questions:")
    for index, qa_pair in enumerate(questions, start=1):                                # enumerate through the dictionary list of question-and-answer pairs
        print(f"{index}. {qa_pair['question']}")                                        # print each question

# Display a list of answers from knowledge base
def list_all_answers(knowledge_base: dict):                                             # extract questions list from the knowledge base
    questions = knowledge_base["questions"]
    print("List of Answers:")
    for index, qa_pair in enumerate(questions, start=1):                                # enumerate through the dictionary list of question-and-answer pairs
        print(f"{index}. {qa_pair['answer']}")                                          # print each answer

# Count the total number of questions or answers
def count_questions_and_answers(knowledge_base: dict):                                  # extract questions list from the knowledge base
    questions = knowledge_base["questions"]
    total_questions = len(questions)                                                    # count the total number of questions and answers
    total_answers = sum(1 for q in questions if "answer" in q)
    print(f"Total Questions: {total_questions}")                                        # display total number of questions
    print(f"Total Answers: {total_answers}")                                            # display total number of answers

def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'list questions':
            list_all_questions(knowledge_base)
        elif user_input.lower() == 'list answers':
            list_all_answers(knowledge_base)
        elif user_input.lower() == 'count':
            count_questions_and_answers(knowledge_base)
        else:
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





# BELOW IS THE ORIGINAL CODE FROM YOUTUBE
# # chat_bot() function
# def chat_bot():                                                                             # function to run the chatbot in a continuous interaction loop
#     knowledge_base: dict = load_knowledge_base('knowledge_base.json')                       # load the JSON file, which contains the existing knowledge base

#     while True:                                                                             # create infinite loop to interact continuously with the user
#         user_input: str = input('You: ')                                                    # user input

#         if user_input.lower() == 'quit':                                                    # when user types 'quit', terminate chat
#             break

#         best_match: Union[str, None] = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])        # find the closest match to the user's question from the knowledge base

#         if best_match:                                                                       
#             answer: str = get_answer_for_question(best_match, knowledge_base)               
#             print(f'Bot: {answer}')                                                         # if a best match is found, retrieve and display answer
#         else:
#             print('Bot: I don\'t know the answer. Can you teach me?')                       # if no match is found, prompt user to 'teach' correct response
#             new_answer: str = input('Type the answer or "skip" to skip: ')

#             if new_answer.lower() != 'skip':
#                 knowledge_base["questions"].append({"question": user_input, "answer": new_answer})  # if user provides an answer, add it to the knowledge base and save it
#                 save_knowledge_base('knowledge_base.json', knowledge_base)
#                 print('Bot: Thank you! I learned a new response!')


if __name__ == '__main__':          # run the chat_bot function when script is executed
    chat_bot()

