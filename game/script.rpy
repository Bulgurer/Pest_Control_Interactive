# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rat:", kind=nvl, color="#b30000")
define narrator = nvl_narrator


# The game starts here.

label start:
    scene black
    "{i}hello i am the narrator{\i}"
    "{i}look at me speak{\i}"
    "{i}is this working?{\i}"
    r "You are a rat"
    r "rats are dope"
    r "Enjoyghhhhhhhhhhhhhhhhhhhhhhhh\nhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\nhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    menu:
        "Where do I go?"
        "Go left.":
            "there was a monster"
        "Go right.":
            "there was cheese"


    "{i}hello i am the narrator{\i}"
    "{i}look at me speak{\i}"
    "{i}is this working?{\i}"

    r "You are a rat"
    r "rats are dope"
    r "Enjoy"

    "{i}hello i am the narrator{\i}"
    "{i}look at me speak{\i}"
    "{i}is this working?{\i}"

    r "You are a rat"
    r "rats are dope"
    r "Enjoy"

    # This ends the game.

    return
