# from functionalities import *
import random
from string import ascii_lowercase

print("-------------------------------------------")
print("----     Welcome to Trial Quiz App     ----")
print("-------------------------------------------")


# participant's name.
candiate_name = input("Enter your name please...\n")
print(f"\nHello dear {candiate_name}, thank you for participating.")
print("Goodluck !!")
print("\n\n")

total_questions_per_quiz = 15
# The quiz questions
questions = {"Whice of the following is not a storage medium?": [
		"Compact disc", "Flash drive", "Floppy disc drive", "Hard disk"
		],
	      "The process whereby computers manipulate data to produce information is known as?": [
			"Processing","Capturing", "Recording", "Retriving"
		],
		"A collection of seperated programs sold as a group is called?": [
			"Suit", "Communication", "Unit", "Command"
		],
		"What category of software is built to harm your computer": [
			"Malware", "Bugs", "Systems software", "Network snakes"
		],
		"Which part of the keyboard contains the alphabet,numbers, and special": [
			"Alphanumeric keys", "Control keys", "Function keys", "Numeric keys"
		],
		"Which key is used to captalize letters and type symbols located above the numbers n the keyboard?": [
			"Shift key", "Enter key", "ctrl keys", "Tab key"
		],
		"What is the primary function of the computer keyboard?": [
			"Input data", "Display images", "Play Music", "Print Documents"
		],
		"Which of the following keys is NOT a modifier key?": [
			"Spacebar", "Ctrl", "Shift", "Alt"
		],
		"The keys 'F1' to 'F12' on the keyboard are known as?": [
			"Function keys", "Control keys", "Escape key", "Alphanumeric keys"
		],
		"Which keyboard shortcut is commonly used for the 'copy' function in most application": [
			"Ctrl + C", "Ctrl + P", "Ctrl + V", "Crtl + X"
		],
		"Which of the following is an open-source operting system?": [
			"Linux", "iOS", "macOS", "Windows"
		],
		"Which key, when pressed along with another key, performs a specific action in software application?": [
			"Function key", "Control key", "Escape key", "Caps Lock key"
		],
		"Which option is used to move text or objects from one place to another within a document in microsoft word": [
			"Drag and Drop", "Copy", "Paste", "Cut"
		],
		"Which keyboard shortcut is used to undo the last acton in microsoft word?": [
			"Ctrl + Z", "Ctrl + X", "Ctrl + Ctrl + C", "Ctrl + V"
		],
		"Which keyboard shortcut is used to cut selected text in Microsoft Word": [
			"Ctrl + X", "Ctrl + C", "Ctrl + V","Ctrl + Z"
		]	 
}

questions_num = min(total_questions_per_quiz, len(questions))
questions = random.sample(list(questions.items()), k=questions_num)

# The candidate score before starting the quiz
overrall_score = 0
# For each question and its alternatives in the questions dictionary, print questions starting from 1 till the number of questionsper quiz is met(15).From the dictionary of alternatives, labeled with ascii_lowercase(a, b, c, d), the zip function is called to iterate over them  to check and store the answer as 
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQ{num}. {question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives))))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")
# store candidate answer and compare to the labeled_alternative with the help of the walrus operator(:=)
    while (answer_label := input("\nAnswer ")) not in labeled_alternatives:
        print("Choose either a, b, c or d")
# compare if answer is correct or wrong using the comparision operator(=)
    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        overrall_score += 1
        print("correct")
    else:
        print("Incorrect")
        print(f"The answer is {correct_answer}, not {answer}")
# print total score of candidate after the quiz
#     print(f"\n\nGreat job dear {candiate_name},your total score is {overrall_score}")


