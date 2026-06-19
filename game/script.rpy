# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Laura", color="#ffeba9")
define y = Character("You", color="#ffffff")

#all sprites
image L_straighthappy = "images/L_straighthappy.png"
image L_straighttalk = "images/L_straighttalk.png" 
image L_straightsmile = "images/L_straightsmile.png"
image L_sidetalk = "images/L_sidetalk.png" 
image L_sidesmile = "images/L_sidesmile.png"
image L_sidehappy = "images/L_sidehappy.png"
image L_closedsmile = "images/L_closedsmile.png"
image L_closedhappy = "images/L_closedhappy.png"

#all backgrounds
image bg room = "images/bg_mainplain.png"
image bg artgallery = "images/bg_main.png"

#artworks
image ballet= "images/bg_ballet.png"
image candel = "images/bg_candel.png"
image field = "images/bg_field.png"
image invert = "images/bg_invert.png"
image invertpt2 = "images/bg_invertpt2.png"
image sea = "images/bg_sea.png"
image sunpencile = "images/bg_sunpencile.png"
image slime= "images/bg_slime.png"
image uravity = "images/bg_uravity.png"
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
    e "I Can't believe we are finally here! This is going to be my new favorite place!"
    show L_straightsmile

    y "I am glad you like it! I have been here before and the food is amazing!"

    show L_straighttalk
    e"really? you saying it definetly means its awesome! "
    show L_straighthappy
    e"I can't wait to see what kind of food they have here !"
    show L_sidehappy
    e"But first, i cant wait to look at all the diffrent kinds of artworks they have here! I heard they have some really cool stuff!"

    

    return