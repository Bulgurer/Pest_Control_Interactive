screen nvl_ish():
    viewport:
        yinitial 1.0
        mousewheel True
        scrollbars "vertical"
        area (150, 100, 1200, 600)
        frame:
            has vbox
            xfill True
            for i in phrases:
                text i

init python:
    def txt(t):
        # This function makes the screen to automatically disappear 
        #    when another interaction occurs
        phrases.append(t)
        renpy.show_screen('nvl_ish', _transient=True)
        renpy.pause()

    def txt2(t):
        # With this function the screen do not disappear,
        #   "hide screen nvl_ish" is requiered in the label
        renpy.hide_screen('nvl_ish')
        phrases.append(t)
        renpy.show_screen('nvl_ish')
        renpy.pause()

define r = Character("Rat:", kind=nvl, color="#b30000")
define narrator = nvl_narrator

label start:
    $ phrases = [ ]
    #$ txt("{i}hello i am the narrator{\i}")
    #$ txt("{i}look at me speak{\i}")
    #$ txt("{i}is this working?{\i}")
    $ txt("You are a rat")
    $ txt("rats are dope")
    $ txt("Enjoy")
    $ txt("hi")
    $ txt("# You can place the script of your game in this file.")
    $ txt("# Declare images below this line, using the image statement.")
    $ txt("# eg. image eileen happy = eileen_happy.png")
    $ txt("# Declare characters used by this game.")

    $ txt("# You can place the script of your game in this file.")
    $ txt("# Declare characters used by this game.")
    $ txt("# eg. image eileen happy = eileen_happy.png")
    $ txt("# Declare images below this line, using the image statement.")
    $ txt("# Declare characters used by this game.")
    $ txt("# eg. image eileen happy = eileen_happy.png")
    $ txt("# You can place the script of your game in this file.")
    $ txt("# Declare characters used by this game.")
    $ txt("# Declare characters used by this game.")
    $ txt("# Declare images below this line, using the image statement.")
    $ txt("!")
    $ txt("# You can place the script of your game in this file.")
    $ txt("?")


    $ txt("# Declare characters used by this game.")
    $ txt("# Declare characters used by this game.")
    $ txt("??")
    $ txt("# Declare images below this line, using the image statement.")
    $ txt("!!")
    $ txt("# eg. image eileen happy = eileen_happy.png")
    $ txt("!!!")
    $ txt("???")
    $ txt("# Declare images below this line, using the image statement.")
    $ txt("END")


    return