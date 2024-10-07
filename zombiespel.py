import random

def generate_question(math_type, value, asked_questions, num_questions):
    # Kontrollerar att en unik fråga genereras baserat på antal gånger en fråga har förekommit.
    while True:
        factor = random.randint(0, 12)
        if math_type == "multiplikation":
            question = f"{factor} * {value}"
        elif math_type == "heltalsdivision":
            question = f"{factor} // {value}"
        elif math_type == "modulus":
            question = f"{factor} % {value}"

        # Kontrollera antalet gånger en fråga har förekommit
        if num_questions <= 13:
            if question not in asked_questions:
                asked_questions[question] = 1
                break
        else:
            if asked_questions.get(question, 0) < 2:
                asked_questions[question] = asked_questions.get(question, 0) + 1
                break

    # Returnerar den unika frågan och dess svar
    if math_type == "multiplikation":
        return question, factor * value
    elif math_type == "heltalsdivision":
        return question, factor // value
    elif math_type == "modulus":
        return question, factor % value

def choose_door(num_doors):
    while True:
        try:
            choice = int(input(f"Välj en dörr (1 till {num_doors}): "))
            if 1 <= choice <= num_doors:
                return choice
            else:
                print("Ogiltigt val, försök igen.")
        except ValueError:
            print("Ange ett heltal.")

def play_game(num_questions, math_type, value):
  correct_answers = 0
  asked_questions = {}
  remaining_doors = num_questions

  for i in range(num_questions):
      question, answer = generate_question(math_type, value, asked_questions, num_questions)
      user_answer = int(input(f"Fråga {i + 1}: {question} = "))
      if user_answer == answer:
          correct_answers += 1
          if i < num_questions - 1:
              door = random.randint(1, remaining_doors)
              user_choice = choose_door(remaining_doors)
              if user_choice != door:
                  print(f"Korrekt! Zombiesarna var bakom dörr {door}.")
                  remaining_doors -= 1
              else:
                  print(f"Du valde fel dörr. Zombiesarna var bakom dörr {door}.")
                  return False
          else:
              print("Grattis! Du har klarat spelet!")
              return True
      else:
          print(f"Fel svar. Du svarade rätt på {correct_answers} frågor. Spelet är över.")
          return False
        
def start_game():
      num_questions = int(input("Välj antal frågor (12 - 26): "))
      while num_questions < 12 or num_questions > 26:
          print("Fel inmatning. Antal frågor måste vara mellan 12 och 26.")
          num_questions = int(input("Välj antal frågor (12 - 26): "))

      math_type = input("Välj räknesätt (multiplikation, heltalsdivision, modulus): ")
      while math_type not in ["multiplikation", "modulus", "heltalsdivision"]:
          print("Fel format.")
          math_type = input("Välj räknesätt (multiplikation, heltalsdivision, modulus): ")

      if math_type != "heltalsdivision":
          value = int(input("Välj divisor (2 - 5): "))
          while value < 2 or value > 5:
              print("Fel inmatning. Divisor måste vara mellan 2 och 5.")
              value = int(input("Välj divisor (2 - 5): "))
      else:
          value = int(input("Välj tabell/divisor: "))

      # Spela spelet och fråga om att spela igen baserat på utfallet
      while True:
          game_won = play_game(num_questions, math_type, value)
          if game_won:
              response = input("Grattis! Vill du spela igen med nya inställningar? (ja/nej): ").lower()
              if response == "nej":
                  break  # Avslutar loopen och spelet
              else:
                  start_game()  # Användaren vill starta ett nytt spel med nya inställningar
                  break  # Se till att bryta loopen efter att ha startat om spelet för att undvika att återgå till den tidigare loopen
          else:
              response = input("Du förlorade. Vill du försöka igen med samma inställningar? (ja/nej): ").lower()
              if response == "nej":
                  break  # Avslutar loopen och spelet om användaren inte vill spela igen
# Kör spelet
start_game()