define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")
$ global h
$ global x

label slime:
    scene slime
    with fade
    e "OMG! it looks so cuteeeee!!!"
    e"I want to bite it!!!"
    e "dhxgfsuixgaisfgi ugh! cuteness overload!"
    e "what do you think?"

    menu:
        "zzzzz..":
            
            y"(shii.. i completely zoned out, but staying up late to reserve this place was worth it tho )"
            y"(you can push through it !)"
            y"('you gotta agree with everything the girl says'-how to get a girlfriend 101)"
            y"yea totally! *yawn*"
            y"(shit)\n ~(^.^)"
            e"oh..."
            e"are you sleepy?"
            y"noooo,\n ;;-_- \n haha...."

            $ l += (x-h*0.25)
            $ h+=1

            if h>=3:
                e"are you alright? if you are tired we can sit and rest for a while"
                y"yea, ofc! i am fine dont worry abt me dud-Laura"
                e"..."
                e"alright"

            if h>3:
                e"you sure?"
                y"uhhh..."
                y"(... )"
                e"..."
                call slx
                

        "It does look cute af":
            $ l+=2
            call slx
    jump artgallerys        
    return

label slx:
    y "It looks cute af"
    e"ofc, jus-just look at it !!!!"
    e "aghhhhh!!!"
    y"your weak against cute stuff huh?"
    e"extremly"
    y"what abt me?"
    e"huh?"
    y"i have been called cute by quite a few people, myself"
    y"don't you think i am cute?"
    e">////<"
    e"ye-yeah"
    y"OoO"
    y"O///o"
    e"..."
    y"..."
    "...."
    e"lets go to the next one..."
    y"yeaa.."
    return