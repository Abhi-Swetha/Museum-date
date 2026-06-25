define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")
$ global h
$ global x
$ global Tim
$ global base
label sea:
    scene sea
    with fade
    e "this one is simpler than the others."
    y"yea , your are ryt"
    e "didn't the artist fear this one might feel underwhelming compared to the other?."
    e"what do you think?"

    menu:
        "... ":
            
            y"(shii.. i completely zoned out, but staying up late to reserve this place was worth it tho )"
            y"(you can push through it !)"
            y"('you gotta agree with everything the girl says'-How to get a girlfriend 101)"
            y"I am not sure, i am sure its whatever you said !"
            e"oh..."
            e"well... maybe there was no reason behind it?."
            y"yeaa, definetly\n ;;-_- \n haha...."

            $ l += (x-h*0.25)
            $ h+=1

            if h>=3:
                e"are you alright? if you are tired we can sit and rest for a while"
                y"yea, ofc! i am fine dont worry abt me dud-Laura"
                e"..."
                e"alright"

            if h>3:
                e"are you sure you are alright?"
                y"uhhh...yeaa, I-sorry, I just zoned out"
                y"(what did she ask? )"
                y"(i think she asked smt abt the artist's motive? )"
                call sax
                e"..."
                e"i thought you were nodding to everything i said cuz you were tired"
                y"ofc ! Dude we have been friends for almost our entire lives, what makes you think {b}{i}I{/i}{/b} would be bored in an {i}Art exhibition!{/i}. -_- ?"
                e"yea , you're right. hehehe"
                e "lets go to the next one!"
                $ h=1
                jump artgallerys

        "it's simple..":
            $ l+=2
            call sax
            jump artgallerys
    return


label sax:
    y "maybe that's the point?"
    e "it's simplisity does make it stand out..."
    y "yeaaa... i really like it tho."
    y "its simple style and minimal coloring looks really good!"
    e "yea, i can almost feel the breeze through this piece"
    e "the ballerina is still my fav,"
    if base:
        e"Both the piece and the how the meaning is hinted by it are beutifull"
    else:
        e"lets go see it next !"
        $ Tim=True
    return