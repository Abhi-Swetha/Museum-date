# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Laura", image=" L %s" ,color="#ffeba9")
define y = Character("You", color="#ffffff")

#all sprites
image L straighthappy = "images/L straighthappy.png"
image L straighttalk = "images/L straighttalk.png" 
image L straightsmile = "images/L straightsmile.png"
image L sidetalk = "images/L sidetalk.png" 
image L sidesmile = "images/L sidesmile.png"
image L sidehappy = "images/L sidehappy.png"
image L closedsmile = "images/L closedsmile.png"
image L closedhappy = "images/L closedhappy.png"

image L sh = "images/side L straighthappy.png"
image L st = "images/side L straighttalk.png" 
image L ss = "images/side L straightsmile.png"
image L sdt = "images/side L sidetalk.png" 
image L sds = "images/side L sidesmile.png"
image L sdh = "images/side L sidehappy.png"
image L cs= "images/side G closedsmile.png"
image L ch = "images/side G closedhappy.png"

#all backgrounds
image bg room = "images/bg mainplain.png"
image bg artgallery = "images/bg main.png"

#artworks
image ballet= "images/bg ballet.png"
image candel = "images/bg candel.png"
image field = "images/bg field.png"
image invert = "images/bg invert.png"
image invertpt2 = "images/bg invertpt2.png"
image sea = "images/bg sea.png"
image sunpencile = "images/bg sunpencile.png"
image slime= "images/bg slime.png"
image uravity = "images/bg uravity.png"
# The game starts here.
default l = 0
label start:
    scene bg room
    with fade

    show L straighthappy 
    
    e "I Can't believe we are finally here! This is going to be my new favorite place!"
    show L straightsmile 

    y "I am glad you like it! I have been here before and the food is amazing!"

    show L straighttalk

    e"really? you saying it definetly means its awesome! "
    show L straighthappy
    e"I can't wait to see what kind of food they have here !"
    show L sidehappy
    e"But first, i cant wait to look at all the diffrent kinds of artworks they have here! I heard they have some really cool stuff!"
    scene bg room
    show L straighthappy
    e"but What do you wanna do first? look at the art or go eat?"
    show L straightsmile

    menu:
        "Look at the art first":
            y "Alright, lets go look at the art first!"
            $ l += 1
            jump artgallery
        "Go eat first":
            y "Alright, lets go eat first!"
            jump food

label food:
    scene bg room
    show L straighttalk 
    e"Alright...."
    scene bg room 
    jump artgallery
    

label artgallery:

    scene bg artgallery 
    with fade
    show L sh 
    e "Wow, this place is amazing! I can't wait to see all the different kinds of art they have here!"
    show L st 