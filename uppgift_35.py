from pprint import pprint
import requests
import sys

ENDPOINT = 'https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda'


class QuizzWebServiceAPI(object):

    def __init__(self):
        self.url = ENDPOINT

    def get_all_questions(self):
        r = requests.get(self.url)
        ls = r.json()['questions']
        promptls = [prompt['prompt'] for prompt in ls]
        return promptls

    def add_question(self, prompt, answer, alternatives):
        data = {
            'prompt': prompt,
            'rightAnswer': answer,
            'wrongAnswers': alternatives
        }
        r = requests.post(url=self.url, json=data)
        return True if r.status_code == 200 else False


def main():
    service = QuizzWebServiceAPI()
    while True:
        user_choice = input(f"Det finns {len(service.get_all_questions())} frågor i quizz-db. Gör ett val: \n"
                            f"1. Lägg till en fråga: \n"
                            f"2. Avsluta programmet: \n")
        if user_choice == '1':
            pprint(service.get_all_questions())
            prompt = input("Skriv en fråga: ")
            answer = input(" Vad är rätt svar?: ")
            alternatives = input("Ange några felaktiga svar (separera dom med kommatecken): ").split(",")
            print(service.add_question(prompt, answer, alternatives))
            print("Tack för ditt bidrag!")
        if user_choice == '2':
            sys.exit()


if __name__ == '__main__':
    main()
