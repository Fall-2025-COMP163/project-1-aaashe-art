[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21265597&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# Abraheem Ashe - my breakdown
I based my RPG world on a game I play called Diablo, and that was the format I took inspiration from when coming up with my stats formula. My game has a maximum level of 50, and the stats multiplier is strictly based on level and has a high stat multiplier based on what each class is and its specialty. I added in gear for the starting classes that would help boost their speciality stats as well. If I were to work on this game long term, I would continue to draw inspiration from Diablo and try to make the game more gear/ability reliant than just level, hence why I wanted to have a level cap of 50. I didn't add a level cap. When I tried adding it, the test cases didn't pass. For AI assistance, I used chat gpt, I ran into some logic errors where in my create character functio,n the outputs would be of the wrong class, and I was having trouble with that. The only other time I used ChatGPT was in the save character function, where I was having trouble returning a false boolean when an error occurred. Chat gpt walked me through the logic of I took the file names either from windows or a txt file and made sure all the delimiters where the same usingf a replace function, now that the delimiter is the same for the windows file and txt file I split them extracting on the file name part and checking if that is in my directory, if not it would return false, if it was it would continue to my with open function.

# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge
