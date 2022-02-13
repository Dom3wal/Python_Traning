#-------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key,value in questions.items():
        print("------------------------")
        print(key)
        print(" Options:  ")
        for i in options[question_num-1]:
            print(i)
        guess= input("Enter A, B or C:  ").upper()
        guesses.append(guess)
        # print(questions[key])
        # print(questions.get(key))
        correct_guesses += check_answer(value, guess)
        question_num += 1

    display_score(correct_guesses,guesses)



#-------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
#-------------------------
def display_score(correct_guesses,guesses):
    print("------------------------")
    print("Results")
    print("------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("You score is: "+str(score)+ "%")


#-------------------------
def play_again():
        response = (input("Do you want to play again? (yes or no): ")).upper()
        if response == "YES":
            return True
        else:
            return False

    

questions = {
    "Who is Dominik ? ":"A",
    "Jak se mosz? ":"B",
    "Je Zeme kulata? ":"C",
    "Je Iza pierda? ":"A"
}

options = [["A. Dominik", "B. Radek","C. Iza"],
           ["A. Dobrze", "B. Eszcze lepi","C. Nanic"],
           ["A. Nima", "B. Hranto","C. Je"],
           ["A. Ja", "B. Ni","C. Mozna"]]

new_game()

while(play_again()):
    new_game()

print("BEY")