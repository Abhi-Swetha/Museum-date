# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Laura",color="#ffeba9")
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

screen artgallerys():
    add "bg artgallery"
    modal True

    imagebutton auto "art_option/ballet_%s.png":
        focus_mask True
        hovered SetVariable("ballet", "ballet")
        idle SetVariable("ballet", None)
        action jump("ballet")

    imagebutton auto "art_option/candel_%s.png":
        focus_mask True
        hovered SetVariable("candel", "candel")
        idle SetVariable("candel", None)
        action jump("candel")

default l = 0
label start:
    scene bg room
    with fade
    
    show L straighthappy 
    
    e "I Can't believe we are finally here! This is going to be my next new favorite place!"
    show L straightsmile 

    y "I am glad you like it! I have been here with my friends before and the food is amazing!"

    show L straighttalk
    e"really? you saying it definetly means its awesome! "
    show L straightsmile

    y"They changed the art gallery a bit since the last time I was here, so I am excited to see what they have now!"

    show L straighttalk
    y"This time its also completely new artworks from the last time I was here...>///<"
    y"i thought it would be cool if i seemed like i knew what i was talking about, but i really dont know much about art"
    show L straightsmile
    show L closedhappy
    e"Half the fun of going to an art gallery is just looking at the art and seeing what you like and dont like! You dont have to know anything about art to enjoy it!"
    show L straightsmile
    for i in range(1):
        show L straighthappy
        show L closedhappy
    e"Still , i am happy you put so much thought into this, "
    for i in range(1):
        show L closedsmile
        show L sidesmile
        show L sidetalk
    e"and here i thought your confession was a mean prank you pulled, and you agreed to the date to clear your name "
    y"(;><)     \n Well, I expected as much when you agreed to date me if today went well, but I really wanted to ask you out on a date. I really like you, and I wanted to spend time with you..."
    y"i will prove it to you by making this date the best date ever!"
    show L straightsmile
    show L straighthappy
    e"Thanks.."
    e"Then why dont we get started? I am so excited to see what the inside looks like!"
    show L sidehappy
    e" i cant wait to look at all the diffrent kinds of artworks they have here! I heard they have some really cool stuff!"
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

label artgallerys:
    scene bg artgallery 
    with fade
    show L straighthappy 
    e "Wow, this place is amazing! I can't wait to see all the different kinds of art they have here!"
    show L straighttalk

    call screen artgallerys 

label ballet:
    scene ballet
    with fade
    show L straighthappy 
    e "Wow, this is beautiful! I love the way the ballerina is captured in mid-air. The colors are so vibrant and the movement is so graceful."
    show L straightsmile
    e "I could stare at this painting for hours!"
    jump artgallerys

label candel:
    scene candel
    with fade
    show L straighthappy
    e "This painting is so unique! I love the way the candle is depicted in such a realistic way, but the background is so abstract. It really makes the candle stand out."
    jump artgallerys