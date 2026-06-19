# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Laura", color="#ffeba9")

#all sprites
image L_straighthappy = "images/L_straighthappy.png"
image L_sidetalk = "images/L_sidetalk.png"    
image L_straightsmile = "images/L_straightsmile.png"

#all backgrounds
image bg room = "images/bg_main.png"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show L_straighthappy

    # These display lines of dialogue.

    e "I Can't believe we are finally here! This is going to be my new favorite place!"

    show L_straightsmile

    "I am glad you like it! I have been here before and the food is amazing!"

    show L_straighttalk
    e"really? you saying it definetly means its awesome! "
    show L_straighttalk
    e"I can't wait to see what kind of food they have here !"
    show L_sidetalk
    e"But first, i cant wait to look at all the diffrent kinds of artworks they have here! I heard they have some really cool stuff!"

    return