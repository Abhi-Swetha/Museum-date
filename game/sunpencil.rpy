define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")
$ global h
$ global x

label sunpencil:
    scene sunpencil
    with fade
    e "another pencile work?"
    e"It is still really pretty"
    e "I didn't expect these many pencil drawings tho..."
    e"I wonder what this is trying to convey..."
    e"what do you think?"

    menu:
        "mmm.... ":    
            y"(shii.. i completely zoned out, but staying up late to reserve this place was worth it tho )"
            y"(you can push through it !)"
            y"('you gotta agree with everything the girl says'-how to get a girlfriend 101)"
            y"I am not sure, i am sure its whatever you said !"
            e"oh..."
            e"well... it could be just a simple painting..."
            y"yeaa, definetly\n ;;-_- \n haha...."

            $ l += (x-h*0.25)
            $ h+=1

            if h>=3:
                e"are you alright? if you are tired we can sit and rest for a while"
                y"yea, ofc! i am fine dont worry abt me dud-Laura"
                e"..."
                e"alright"

            if h>3:
                e"but still dont you think there might be more to it?"
                y"uhhh..."
                y"(i think i may have seemed uninterseted, fak... )"
                call spa
                

        "freedom..?":
            $ l +=2
            call spa
    jump artgallerys       
    return
    

label spa:
    y"i Think it is trying to convey freedom ?"
    e"why?"
    y"the artwork seems rather rough on the sides"
    y"The pencil stocks add to it"
    e"so her being translusent is too convey she has become free?"
    y"yesss"
    e"ohhh~~"
    e"makes sence makes sence!"
    y"yesss,then shall we go to the next one?"
