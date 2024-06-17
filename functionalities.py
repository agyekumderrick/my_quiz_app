# import random
# from string import ascii_lowercase

# total_questions_per_quiz = 15
# questions = {"Whice of the following is not a storage medium?": [
# 		"Compact disc", "Flash drive", "Floppy disc drive", "Hard disk"
# 		],
# 	      "The process whereby computers manipulate data to produce information is known as?": [
# 			"Processing","Capturing", "Recording", "Retriving"
# 		],
# 		"A collection of seperated programs sold as a group is called?": [
# 			"Suit", "Communication", "Unit", "Command"
# 		],
# 		"What category of software is built to harm your computer": [
# 			"Malware", "Bugs", "Systems software", "Network snakes"
# 		],
# 		"Which part of the keyboard contains the alphabet,numbers, and special": [
# 			"Alphanumeric keys", "Control keys", "Function keys", "Numeric keys"
# 		],
# 		"Which key is used to captalize letters and type symbols located above the numbers n the keyboard?": [
# 			"Shift key", "Enter key", "ctrl keys", "Tab key"
# 		],
# 		"What is the primary function of the computer keyboard?": [
# 			"Input data", "Display images", "Play Music", "Print Documents"
# 		],
# 		"Which of the following keys is NOT a modifier key?": [
# 			"Spacebar", "Ctrl", "Shift", "Alt"
# 		],
# 		"The keys 'F1' to 'F12' on the keyboard are known as?": [
# 			"Function keys", "Control keys", "Escape key", "Alphanumeric keys"
# 		],
# 		"Which keyboard shortcut is commonly used for the 'copy' function in most application": [
# 			"Ctrl + C", "Ctrl + P", "Ctrl + V", "Crtl + X"
# 		],
# 		"Which of the following is an open-source operting system?": [
# 			"Linux", "iOS", "macOS", "Windows"
# 		],
# 		"Which key, when pressed along with another key, performs a specific action in software application?": [
# 			"Function key", "Control key", "Escape key", "Caps Lock key"
# 		],
# 		"Which option is used to move text or objects from one place to another within a document in microsoft word": [
# 			"Drag and Drop", "Copy", "Paste", "Cut"
# 		],
# 		"Which keyboard shortcut is used to undo the last acton in microsoft word?": [
# 			"Ctrl + Z", "Ctrl + X", "Ctrl + Ctrl + C", "Ctrl + V"
# 		],
# 		"Which keyboard shortcut is used to cut selected text in Microsoft Word": [
# 			"Ctrl + X", "Ctrl + C", "Ctrl + V","Ctrl + Z"
# 		]	 
# }


# def run_quiz():
#     questions = prepare_questions(questions, num_quetions=total_questions_per_quiz)

#     overrall_score = 0
#     for num, (question, alternatives) in enumerate(questions, start=1):
#         print(f"\nQ{num}. ")
#         overrall_score += ask_question(question, alternatives)
#         print(f"\nYou got {overrall_score} correct out of {num} questions")

# def prepare_questions(questions, num_questions):
#     num_questions = min(num_questions, len(questions))
#     return random.sample(list(questions.items()), k=num_questions)


# def ask_question(question, alternatives):
#     correct_answer = alternatives[0]
#     ordered_alternativies = random.sample(alternatives, k=len(alternatives))

#     answer = get_answer(question, ordered_alternativies)
#     if answer == correct_answer:
#         print("Correct")
#         return True
#     else:
#         print("Incorrect !!")
#         return False

# def get_answer(question, alternatives):
#     print(f"{question}")
#     labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
#     for label, alternative in labeled_alternatives.items():
#         print(f" {label}) {alternative}")

#     while (answer_label := input("\nAnswer "))not in labeled_alternatives:
#         print("Choose either a, b, c or d")
#     return labeled_alternatives[answer_label]

#         # print(f"The answer is {correct_answer} not {answer}")