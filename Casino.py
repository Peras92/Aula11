import random
import json
import datetime

secret = random.randint(1, 10)
attempts = 0

print("Bem vindo ao casino virtual")
nome = input("Por favor indica o teu nome:")

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read()) # [{"attempts": 6, "date": "2019-03-01 12:30:56.198449"}, {"attempts": 5, "date": "2019-03-03 18:26:19.439882"}, {"attempts": 6, "date": "2019-03-18 09:55:01.734739"}]

    for score_dict in score_list:
        print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

jogo = True
while jogo:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        if attempts not in score_list:
            data = datetime.datetime.today()
            score_data = {"attempts": attempts, "date": str(data.strftime("%X"))}
            score_list.append(score_data)
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

        jogo = False
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")