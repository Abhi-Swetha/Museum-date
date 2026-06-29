# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#c88e8e",what_font="font/LiberationSerif-Regular.ttf")
define both = Character("You and Laura",color="#8595d1ff")

#all sprites
image L straighthappy = "images/L straighthappy.png"
image L straighttalk = "images/L straighttalk.png" 
image L straightsmile = "images/L straightsmile.png"
image L sidetalk = "images/L sidetalk.png" 
image L sidesmile = "images/L sidesmile.png"
image L sidehappy = "images/L sidehappy.png"
image L closedsmile = "images/L closedsmile.png"
image L closedhappy = "images/L closedhappy.png"
image L straightblushhappy=im.Scale("images/L straightblushhappy.png",607.50,1080)
image L straightnortalk="images/L straightcnortalk.png"
image L straightnor="images/L straightnor.png"
image L closedblushhappy=im.Scale("images/L closedblushhappy.png",607.50,1080)
image L sidenortalk="images/L sidenortalk.png"
image L downhappy=im.Scale("images/L downhappy.png",607.50,1080)
image L downtalk=im.Scale("images/L downtalk.png",607.50,1080)


#all backgrounds
image bg room = "images/bg mainplain.png"
image bg artgallery = "images/bg nodoor.png"

#artworks
image ballet= "images/bg ballet.png"
image candle = "images/bg candle.png"
image field = "images/bg field.png"
image invert = "images/bg invert.png"
image invertpt2 = "images/bg invertp2.png"
image sea = "images/bg sea.png"
image sunpencil = "images/bg sunpencil.png"
image slime= "images/bg slime.png"
image uravity = "images/bg uravity.png"

# The game starts here.
default l = 0
default h=0
default x=1
default art=0

default Tim=False

$ global h
$ global x


screen artgallerys():
    add "bg artgallery"
    modal True
    
    imagebutton :
        auto "art_options/ballet_%s.png"
        focus_mask True
        hovered SetVariable("ballet", "ballet")
        unhovered SetVariable("ballet", None)
        action Jump("b_c")

    imagebutton :
        auto "art_options/candle_%s.png"
        focus_mask True
        hovered SetVariable("candle", "candle")
        unhovered SetVariable("candle", None)
        action Jump ("c_c")
        
    imagebutton :
        auto "art_options/field_%s.png"
        focus_mask True
        hovered SetVariable("field", "field")
        unhovered SetVariable("field", None)
        action Jump("f_c")

    imagebutton :
        auto "art_options/invert_%s.png"
        focus_mask True
        hovered SetVariable("invert", "invert")
        unhovered SetVariable("invert", None)
        action Jump("i_c")

    imagebutton :
        auto "art_options/door_%s.png"
        xalign 0.5
        yalign 1
        focus_mask True
        hovered SetVariable("door", "door")
        unhovered SetVariable("door", None)
        action Jump("door_c")

    imagebutton :
        auto "art_options/sea_%s.png"
        focus_mask True
        hovered SetVariable("sea", "sea")
        unhovered SetVariable("sea", None)
        action Jump("S_c")
 
    imagebutton :
        auto "art_options/sunpencil_%s.png"
        focus_mask True
        hovered SetVariable("sunpencil", "sunpencil")
        unhovered SetVariable("sunpencil", None)
        action Jump("sp_c")

    imagebutton :
        auto "art_options/slime_%s.png"
        focus_mask True
        hovered SetVariable("slime", "slime")
        unhovered SetVariable("slime", None)
        action Jump("sl_c")

    imagebutton :
        auto "art_options/uravity_%s.png"
        focus_mask True
        hovered SetVariable("uravity", "uravity")
        unhovered SetVariable("uravity", None)
        action Jump("u_c")

label start:
    play music "adiou/Art_gallery.mp3" volume 0.5 fadein 0.5 loop
    scene black
    centered "{color=#ffffff}{size=50} You just confesses to your childhood friend, Laura Jane, \n and both have you decided to go on a date together after which she will give her answer based on how the date went.{/size}{/color} "
    scene bg room
    show L straighthappy 
    with fade
    pause(0.5)  
    e "I Can't believe we are finally here! This is going to be my next new favorite place!"
    show L straightsmile 

    y "I am glad you like it! I have been here with my friends before and the food is amazing!"

    show L straighttalk
    e"really? you saying it definetly means its awesome! "
    show L straightsmile

    y"They changed the art gallery a bit since the last time I was here, so I am excited to see what they have now!"

    show L straighttalk
    y"This time its also completely new artworks from the last time I was here...>///<"
    show L closedsmile
    y"i thought it would be cool if i seemed like i knew what i was talking about, but i really dont know much about art"
    show L straightsmile
    show L closedhappy
    e"Half the fun of going to an art gallery is just looking at the art and seeing what you like and dont like! You dont have to know anything about art to enjoy it!"
    show L straightsmile
    show L closedhappy
    e"Still , i am happy you put so much thought into this ,"
    show L sidetalk
    e"and here i thought your confession was a mean prank you pulled, and you agreed to the date to clear your name "
    show L sidesmile
    y"(;><)     \n Well, I expected as much when you agreed to date me if today went well, but I really wanted to ask you out on a date. I really like you, and I wanted to spend time with you..."
    show L closedsmile
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
    with Pause(0.5)
    transform left2:
        xanchor 0.5
        xpos 0.3
        yanchor 1.0
        ypos 1.0
    show L straightsmile at left2
    with move
    pause (0.5)
    

    menu:
        "Look at the art first":
            show L straightsmile at center
            with move
            pause (0.5)
            y "Alright, lets go look at the art first!"
            $ l += 1
            stop music fadeout 0.2
            jump artgallery
        "Go eat first":
            show L straightsmile at center
            with move
            pause (0.5)
            y "Alright, lets go eat first!"
            stop music fadeout 0.2
            jump food

    return

label food:
    play music "adiou/Art_gallery.mp3" fadein 0.5 volume 0.5 loop
    scene bg room
    show L straighttalk 
    e"Alright...."
    scene black
    centered "{color=#ffffff}{size=50}You and Laura both go and eat a hearthy meal, and come back.\nBoth of enter the Art gallery Room {/size}{/color}"
    jump artgallery
    stop music fadeout 0.5

label artgallery:
    play music "adiou/Art_gallerytrue.mp3" fadein 0.5 volume 0.5
    scene black
    centered "{color=#ffffff}{size=50}You and Laura both enter the Art gallery Room {/size}{/color}"
    scene bg artgallery 
    show L straighthappy
    with fade
    pause(0.5)
    e "Wow, this place is amazing! I can't wait to see all the different kinds of art they have here!"
    e"which art work do you wanna see first?"
    hide L straightsmile
    with moveoutleft
    pause(0.3)
    stop music fadeout 0.2
    jump artgallerys

label artgallerys:
    play music "adiou/Art_gallerytrue.mp3" volume 0.5 loop
    scene bg artgallery
    if art >=8:
        show L sidehappy
        e"we finished seeing all the artworks,already?"
        show L straightsmile
        y"waht do you mean already?, its the evening! we came here during the afternoon"
        show L closedhappy
        e"hehe, you are ryt!"
        jump end 
    
    call screen artgallerys 

label alreadyseen:
    play music "adiou/Art_gallerytrue.mp3" volume 0.5 fadein 0.5 loop
    y "(didn't we already see that one?)"
    y "(lets choose smt else)"
    stop music fadeout 0.2
    jump artgallerys
    return

#check if seen
label door_c:
    play music "adiou/Art_gallerytrue.mp3" volume 0.5 fadein 0.5 loop
    if art >= 4:
        stop music fadeout 0.2
        jump end
    else:
        y "(leave already??, we haven't even seen 4 artworks yet)"
        y "(we can leave after a while)"
        y "(lets see what artwork to look at next!)"
        stop music fadeout 0.2
        jump artgallerys
    return
        

default b_see=False
default c_see=False
default f_see=False
default i_see=False
default s_see=False
default Sp=False
default Sl=False
default u_see =False
$ global b_see 
label b_c:
    if not b_see:
        $ b_see = True 
        $ persistent.ballet=True
        $ art +=1
        jump ballet
    else:
        jump alreadyseen
    return

label c_c:
    if not c_see:
        $ c_see = True 
        $ persistent.candle=True
        $ art +=1
        jump candle
    else:
        jump alreadyseen
    return

label f_c:
    if not f_see:
        $ f_see = True 
        $ persistent.field=True
        $ art +=1
        jump field
    else:
        jump alreadyseen
    return

label i_c:
    if not i_see:
        $ i_see = True 
        $ persistent.invert=True
        $ art +=1
        jump invert
    else:
        jump alreadyseen
    return

label S_c:
    if not s_see:
        $ s_see = True 
        $ persistent.sea=True
        $ art +=1
        jump sea
    else:
        jump alreadyseen
    return

label sl_c:
    if not Sl:
        $ Sl = True 
        $ persistent.slime=True
        $ art +=1
        jump slime
    else:
        jump alreadyseen
    return

label sp_c:
    if not Sp:
        $ Sp = True 
        $ persistent.sun=True
        $ art +=1
        jump sunpencil
    else:
        jump alreadyseen
    return

label u_c:
    if not u_see:
        $ u_see = True 
        $ persistent.uravity=True
        $ art +=1
        jump uravity
    else:
        jump alreadyseen    
    return

label end:
    play music "adiou/Art_gallerytrue.mp3" volume 0.5 fadein 0.5 
    scene bg artgallery
    show L sidehappy
    with moveinleft
    e"I didn't realise so much time had passed ! today was really fun!"
    show L straightsmile
    y"I had a lot of Fun too"
    show L straighthappy
    e"Thank you for taking me out"
    show L sidesmile
    play sound "adiou/bildend.wav" volume 0.2 fadein 0.5
    y"Its fine,I asked you out anyway..."
    y"soo...?"
    scene black
    centered "{color=#ffffff}{size=50}You and Laura, leave the exhibition hall and go back to the waiting room.\nyou can feel your hands grow cold with both exictment and fear.\n \"Today wasn't that bad!\" you think, ofc you dozed off in the middle sometimes from being not able to sleep yesterday... but apart from that today went pretty well, ryt?!\n but now it is time to see if today actually went well... {/size}{/color}"
    if l >=12:
        jump goodend
    else:
        jump badend
    return

label badend:
    play sound "adiou/bildend.wav" volume 0.5 fadein 0.5
    scene bg mainplain
    show L straightnor
    with dissolve 
    pause(0.7)
    show L straightnortalk
    play music "adiou/rejectbef.mp3" volume 0.5 fadein 0.5
    e"I-uhh, I first want to thank you for confessing to me..."
    show L sidetalk
    stop sound fadeout 0.7
    e"I didn't think anyone would think of me that way, espeacialy {i}you{/i}"
    show L straightnortalk
    e"But I dont have any romantic feelings toward you, even now I only see you as a friend"
    show L straightnor
    y"oh..."
    show L sidenortalk
    e"I know you feelings are genuine, which is why i don't want to give you false hope."
    show L straightnortalk
    e"I don't think I can accept you confession, because i don't feel the same way"
    y"I see,('—_—)"
    y"I mean i expected it but, still ..(T_T)"
    play sound "adiou/rejectafter.mp3" volume 0.5 fadein 0.5
    stop music fadeout 0.7
    y"Still,"
    show L sidesmile
    y"do you think we can continue being friends?"
    show L sidenortalk
    e"Ofc, But..."
    show L sidetalk
    e"Not for now, not until you get over me..."
    show L straighttalk
    e"as I said before I don't want to give you false hope"
    show L straightnor
    y"yes..."
    y"I understand, Thank you for considering my feelings. But ..."
    show L straightsmile
    y"don't worry, when i feel ready i will talk to you myself"
    show L straighthappy
    e"then i will be waiting"
    scene black
    with fade
    pause(0.5)
    centered "{color=#ffffff}{size=50}It takes you a couple of months to get over the rejection and \n\na few more before you could face Laura without the lingering feelings..."
    centered "{color=#ffffff}{size=50}Both of you get buzy with life and after almost 5 years you ask her out to a drink,\n\n this time as a friend {/size}{/color}"
    stop sound fadeout 0.8
    play music "adiou/bar.mp3" volume 0.5 fadein 1
    play sound "adiou/barback.wav" volume 0.3 fadein 0.5
    #scene bg badend with fade 
    #with pause (0.5)
    e"took you long enough to contact me again"
    y"Moving on from your first love is harder than you think... \n(;-n-)"
    y"its even harder to get rid of the lingering feeling,haaa......"
    y"btw congrats on getting engaged! I heard you got proposed on the same day you got your promotion"
    e"oh, YES!!! That is officially the {i}happiest{/i} day of my life!!!"
    e"Ahh...That was the first time i cried tears of joy (> . <)♡"
    e"I heard you got a girlfrienddd~!, who is the lucky girl??"
    e"I saw her on insta, how did you bag such a badddie?"
    y"Hey!! \n(>///<)\nwell Shraya,my girlfriend was the one who confessed to me..."
    y"and to be honest, i thought i was dreaming, and it was just around the time i had gotton open to dating again"
    y"so I said yes, and I have grown to love her a {b}LOT{/b}"
    y"don't tell her but, I am planning on proposeing to her on our 3rd year anniversary...(^///^)!"
    e"(,,>7<,,) eekkkk!"
    centered "{color=#ffffff}{size=50}time flows by just as it has, 10 minutes turn to an hour then two ...{/size}{/color}" 
    centered "{color=#ffffff}{size=50}Catching up on the things you missed ,laughing, chatting ,it felt like the 5 years you were apart were nothing...{/size}{/color}"
    y"..."
    e"A lot can change in 5 years, huh?"
    y"yea,"
    y"..."
    e"let's toast to that?"
    y":)"
    y"and for your engaement!"
    e"and for {i}you{/i} proposing to your girlfriend!"
    e"ready?"
    y"ready as I will ever be!"
    stop sound fadeout 0.5
    centered "{color=#ffffff}{size=90}CHEERS!!!!!{/size}{/color}" 
    $ persistent.bad_end = True 
    centered "{color=#ffffff}{size=100}✦•┈⋅⋯ ⋯⋅┈•✦\n\nFRIENDSHIP END\n\n✦•┈⋅⋯ ⋯⋅┈•✦{/size}{/color}" 
    return

label goodend:
    play sound "adiou/bildend.wav" volume 0.2 fadein 0.5
    scene bg mainplain
    with fade
    show L straightsmile
    with fade 
    pause(0.3)
    show L sidehappy
    play music "adiou/rejectbef.mp3" volume 0.5 fadein 0.5
    stop sound fadeout 0.7
    e"I-uhh, I first want to thank you for confessing to me..."
    show L sidetalk
    e"I didn't think anyone would think of me that way, espeacialy {i}you{/i}"
    show L straightnortalk
    e"But I dont have any romantic feelings toward you, even now I only see you as a friend"
    show L straightnor
    y"...."
    show L straightsmile
    y"I see-"
    show L downtalk
    play music "adiou/good_end.mp3" volume 0.5 fadein 1.0 
    e"-That being said, if {b}you{/b} are okey with it..."
    e"I would like us to keep hanging out like this, not as friends but something more..."
    show L downhappy
    e"because, today felt like every other time we have hung out, it was fun and comfortable yes, but didn't feel like a date.."
    show L straightblushhappy
    e"I belive we can make it work, but i want to approch it as a proper date"
    show L closedblushhappy
    e"soo what do you think?, i know this is not a proper answer but..."
    e"i wanna try and make this work..."
    scene black
    with fade
    pause(0.5)
    centered "{color=#ffffff}{size=50}you guys go on a second date to an Rock Climbing studio, This felt more like your usual hang out then the Art exhibition date,\n\nBut maybe thats not so bad?{/size}{/color} "
    centered "{color=#ffffff}{size=50}Through the second date you both got closer, after which you went on 3 more diffrents date with her, each one getting more fun than before...{/size}{/color}"
    centered "{color=#ffffff}{size=50}before long both of you had gotten closer, and the initial akwardness was no where to be seen\n\nYou decided to ask her out again...at 8 in the night\n\n both you meet at a park near her house.{/size}{/color}"
    centered "{color=#ffffff}{size=50}seems that Laura had also thought the same thing and both you end up confessing to each other at the same time.{/size}{/color}"
    #scene bg park
    #with fade
    #pause (0.5)
    play sound "adiou/park back.mp3" volume 0.2 fadein 0.5
    play musiv "adiou/park.mp3" volume 0.5 fadein 0.5
    e"I never thought i would ever fall in love with the most cowardly, nerdy guy i knew..."
    y"and I never thought i would fall in love with the most unrully reckless girl i knew.."
    e"but people change, and with those changes come new feelings"
    y"and sometimes, no matter how someone changes you can't help but love them.."
    "..."
    centered "{color=#ffffff}{size=50}To be honest, there was no flying flower petals or fireworks, not even stars... {/size}{/color}"
    centered "{color=#ffffff}{size=50}But that park with its floresent street light shinging down on Laura, {/size}{/color}"
    #show bg goodend
    #with fade
    #pause (0.5)
    e"I love you..."
    centered "{color=#ffffff}{size=50}was the most beutifull sight you had seen in your life{/size}{/color}"
    y"I love you too"
    e"('.////.')"
    y"(^///^)"
    scene black with fade
    pause (0.5)
    $ persistent.good_end = True
    centered "{color=#ffffff}{size=90}-----------------\n\nLOVER END\n\n-----------------{/size}{/color}"
    return