import random
import json
import datetime

secret = random.randint(1, 10)
attempts = 0
tent_erradas = []


print("Bem vindo ao número virtual")
nome = input("Por favor indica o teu nome:")

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read()) # [{"attempts": 6, "date": "2019-03-01 12:30:56.198449"}, {"attempts": 5, "date": "2019-03-03 18:26:19.439882"}, {"attempts": 6, "date": "2019-03-18 09:55:01.734739"}]

    high_score=sorted(score_list, key=lambda i: i["attempts"])

    print("High Scores - Top 3")

    for score_dict in high_score[:3]:
        print("O Jogador {0} conseguiu acertar em {1} tentativas. O número era o {3} e os números que ele errou foram os seguintes {4}".format(score_dict.get("jogador"), str(score_dict.get("attempts")), score_dict.get("date"), score_dict.get("segredo"), score_dict.get("tentativas")))
        

jogo = True

while jogo:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    attempts += 1


    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        score_data = {"attempts": attempts, "date": str(datetime.datetime.now()), "jogador": nome, "segredo": secret, "tentativas": tent_erradas}

        score_list.append(score_data)

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        jogo = False
    elif guess > secret:
        tent_erradas.append(guess)
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        tent_erradas.append(guess)
        print("Your guess is not correct... try something bigger")