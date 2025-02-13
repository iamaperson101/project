from flask import Flask, render_template, jsonify, request
import sqlite3
import random

app = Flask(__name__)
randomword = ''


def setup():
    global randomword
    wordsd = sqlite3.connect("words.db")
    wcursor = wordsd.cursor()

    wcursor.execute('CREATE INDEX IF NOT EXISTS idx_word ON words(word);')
    wordsd.commit()

    wcursor.execute('SELECT word FROM words ORDER BY RANDOM() LIMIT 1;')
    result = wcursor.fetchone()

    if result:
        randomword = result[0].lower()
    else:
        randomword = None

    print(f"Random word: {randomword}")

    wcursor.close()
    wordsd.close()

@app.route("/")
def home():
    setup()
    return render_template('index.html')


@app.route('/check_word', methods=['POST'])
def check_word():
    data = request.get_json()
    word = data.get('word', '').strip().lower()


    print(f"user word: {word}, correct word: {randomword}")

    # SQL setup
    wordsdata = sqlite3.connect("words.db")
    wcursor = wordsdata.cursor()


    wcursor.execute('SELECT * FROM words WHERE LOWER(word) = ?', (word,))
    userinput = wcursor.fetchone()
    wordsdata.close()

    if not userinput:  # Check if word is valid
        print("Word not valid")
        return jsonify({"error2": "Word not valid, try again!"})

    # Convert words to lists
    CorrectWordCharacters = list(randomword)
    UserInputCharacters = list(word)

    LetterInfo = ['absent'] * 6
    correct_counts = {}  # Tracks counted occurrences of letters

    # First pass: Green check (correct letters in correct positions)
    for i in range(6):  # Assuming 6-letter words (adjust if needed)
        if UserInputCharacters[i] == CorrectWordCharacters[i]:
            print(f"{i+1}th letter '{UserInputCharacters[i]}' is correct.")
            LetterInfo[i] = 'correct'
            correct_counts[UserInputCharacters[i]] = correct_counts.get(UserInputCharacters[i], 0) + 1

    # Second pass: Yellow check (right letter, wrong position)
    for i in range(6):  # Assuming 6-letter words (adjust if needed)
        if LetterInfo[i] == 'correct':
            continue  # Skip already matched green letters

        if UserInputCharacters[i] in CorrectWordCharacters:
            # Count the occurrences of UserInputCharacters[i] in CorrectWordCharacters
            # and ensure we don't overcount based on previous green matches
            if CorrectWordCharacters.count(UserInputCharacters[i]) > correct_counts.get(UserInputCharacters[i], 0):
                print(f"{i+1}th letter '{UserInputCharacters[i]}' is present but in the wrong position.")
                LetterInfo[i] = 'present'
                correct_counts[UserInputCharacters[i]] = correct_counts.get(UserInputCharacters[i], 0) + 1


    # Return structured response
    response = {
        "message": "Correct guess!" if word == randomword else "Incorrect guess!",
        "result": LetterInfo,
        "correctguess": randomword
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
