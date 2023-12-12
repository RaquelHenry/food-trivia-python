from Class_project import trivia
# storing the multiple choice questions, indenting the choices for visual looks
food_choices = [
    "Where does kimchi come from? \n a) South Korea\n b) Thailand\n c) India\n d) Indonesia\n\n",
    "Where does paella come from? \n a) Mexico\n b) Italy\n c) Spain\n d) Brazil\n\n",
    "Where does pannukakku come from? \n a) Sweden\n b) Finland\n c) Germany\n d) France\n\n",
    "Where does red red come from? \n a) Nigeria\n b) Chad\n c) Algeria\n d) Ghana\n\n",
    "Where does moussaka come from? \n a) Egypt\n b) Turkey\n c) Israel\n d) Greece\n\n",
    "Where does tiramisu come from? \n a) Italy\n b) Austria\n c) Russia\n d) Portugal\n\n",
    "Where does kolache come from? \n a) Czech Republic\n b) Belgium\n c) Germany\n d) England\n\n",
    "Where does tikka masala come from? \n a) South Africa\n b) India\n c) Morocco\n d) Mongolia\n\n",
    "Where does feijoada come from? \n a) Peru\n b) Argentina\n c) Brazil\n d) Chile\n\n",
    "Where does cheeseburger come from? \n a) Australia\n b) England\n c) USA\n d) Canada\n\n"
]
# storing my answers in a different list, its ends up being assigned almost to eacn index I have labeled for each item in the list, and separated by the comma
questions = [
    trivia(food_choices[0], 'a'),
    trivia(food_choices[1], 'c'),
    trivia(food_choices[2], 'b'),
    trivia(food_choices[3], 'd'),
    trivia(food_choices[4], 'd'),
    trivia(food_choices[5], 'a'),
    trivia(food_choices[6], 'a'),
    trivia(food_choices[7], 'b'),
    trivia(food_choices[8], 'c'),
    trivia(food_choices[9], 'c')
]

# for loop to run the game for each item in the questions list


def run_game(questions):
    score = 0
    print("Welcome to Food around the World Trivia!\nDo you have what it takes to get a perfect score?\nPress Enter to start!")
    input()
    for trivia in questions:
        answer = input(trivia.prompt)
        if answer != trivia.answer:
            print("That was incorrect. Next Question...")
        elif answer == trivia.answer:
            score += 1
            print("You got " + str(score) + "/" +
                  str(len(questions)) + " correct!")
    print("Thank you for playing my game! Until next time!")


# this will run the game in its entirety
run_game(questions)
