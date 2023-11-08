import requests
import random
import json

valid_categories = ['artliterature', 'language', 'sciencenature',
                   'general', 'fooddrink', 'geography', 'music',
                   'mathematics', 'religionmythology', 'sportsleisure']


def check_category(category):
    return category if category in valid_categories else 'general'


def get_trivia_question(category):
    api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(check_category(category))
    response = requests.get(api_url, headers={'X-Api-Key': '80fg7kamj8LQY0D1dvSHRQ==3700fJ7RUnN7n8T9'})

    if response.status_code == requests.codes.ok:
        return json.loads(response.text)
    else:
        return 'Error'


def ask_question(question_data):
    if question_data:
        question = random.choice(question_data)
        print("")
        print("Category:", question['category'])
        print("Question:", question['question'])
        print("")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == question['answer'].lower():
            print("Good answer!")
        else:
            print("Sorry, it'snt correct, it was:", question['answer'])
    else:
        print('Error')


def main():
    while True:
        print("Choose a category :")
        for i, category in enumerate(valid_categories, 1):
            print(f"{i}. {category}")

        category_choice = input("Number of the category : ").strip()

        if category_choice.isdigit():
            category_choice = int(category_choice)
            if 1 <= category_choice <= len(valid_categories):
                selected_category = valid_categories[category_choice - 1]
                question_data = get_trivia_question(selected_category)
                if question_data:
                    ask_question(question_data)
                else:
                    print('Error')
            else:
                print("Category invalid")
        else:
            print("Category invalid.")

        play_again = input("Wanna play again ? (yes/no): ").strip().lower()
        if play_again != "yes":
            break


if __name__ == '__main__':
    main()
