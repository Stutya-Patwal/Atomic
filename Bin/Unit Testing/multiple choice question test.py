from inquirer import prompt, List

questions = [
    List('choice',
         message="What's your favorite programming language?",
         choices=['Python', 'Java', 'C++', 'JavaScript'],
         carousel=True),
]

answers = prompt(questions)
print(f"You chose {answers['choice']}!")