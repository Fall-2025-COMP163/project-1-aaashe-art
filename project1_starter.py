"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Abraheem Ashe
Date: 10-24-2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import math
import os


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    
    
    player_info = {
        "name": name, 
        "class": character_class, 
        "level": 1,
        }
    
    str_mag_hlth = calculate_stats(character_class, player_info['level'])
    
    player_info.update({
        'strength': str_mag_hlth[0],
        'magic': str_mag_hlth[1],
        'health': str_mag_hlth[2],
    })
    player_info['gold'] = 100
    print(player_info)
    #(f"name: {player_info['name']}, Class: {player_info['class']}, Level: {player_info['level']}, Strength: {player_info['strength']}, Magic: {player_info['magic']}, Health: {player_info['health']}, gold: {player_info['gold']}")
    return player_info

        
    #TDO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    #pass

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    if character_class == "Warrior":
        strength = 10 + (level * 2)
        magic = 2 + (level * .5)
        health = 100 + (level * 5)
        return (math.ceil(strength), math.ceil(magic), math.ceil(health))
    elif character_class == "Mage":
        strength = 4 + (level * 1)
        magic = 10 + (level * 2)
        health = 80 + (level * 2)
        return (math.ceil(strength), math.ceil(magic), math.ceil(health))
    elif character_class == "Rogue":
        strength = 7 + (level * 1.3)
        magic = 5 + (level * 1)
        health = 70 + (level * 3)
        return (math.ceil(strength), math.ceil(magic), math.ceil(health))
    elif character_class == "Cleric":
        strength = 6 + (level * .5)
        magic = 8 + (level * 2)
        health = 90 + (level * 4)
        return (math.ceil(strength), math.ceil(magic), math.ceil(health))
    else:
        print('Error')
        return (0,0,0)
     
    # : Implement this function
    # Return a tuple: (strength, magic, health)
    #pass

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    
    required_info = ['name', 'class', 'level', 'strength', 'magic', 'health', 'gold']

# Check that all required fields exist in the dictionary
    for info in required_info:
        if info not in character:
            print('Error')
            return False

    
    with open (filename, 'w') as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True
    
    # : Implement this function
    # Remember to handle file errors gracefully
    #pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    
    if not os.path.exists(filename):
        return None
    
    character = {}
    with open (filename, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        line = line.strip()
        parts = line.split(':')
        key_part = parts[0].strip()
        value_part = parts[1].strip()
        if key_part ==  'Character Name':
            character['name'] = value_part
        elif key_part == 'Class':
            character['class'] = value_part
        elif key_part == 'Level':
            character['level'] = int(value_part)
        elif key_part == 'Strength':
            character['strength'] = int(value_part)
        elif key_part == 'Magic':
            character['magic'] = int(value_part)
        elif key_part == 'Health':
            character['health'] = int(value_part)
        elif key_part == 'Gold':
            character['gold'] = int(value_part)
    return character
    # : Implement this function
    # Remember to handle file not found errors
    #pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print(f'=== CHARACTER SHEET ===')
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    # : Implement this function
    #pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    if 'level' in character:
        character['level'] += 1
        str_mag_hlth = calculate_stats(character['class'], character['level'])
        character['strength'] = str_mag_hlth[0]
        character['magic'] = str_mag_hlth[1]
        character['health'] = str_mag_hlth[2]
        
    
    # : Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    char = create_character("Abraheem", "Cleric")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")
