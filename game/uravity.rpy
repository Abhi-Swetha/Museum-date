define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")
$ global h
$ global x

label uravity:
    scene uravity
    with fade
    e "damn, This one's a pure master piece!"
    y"god dang , yeaa! The artist must have poured their heart and soul into this"

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
                y"yea, ofc! i am completely finee!"
                e"..."
                e"alright"

            if h>3:
                e"are you sure you are alright?"
                y"uhhh...yeaa"
                y"(what did she ask? )"
                y"(i think se asked smt abt the artist's motive? )"
                call uax
                e"so you {b}{i}DID{/b}{/i} think there was more to it! "
                e"i thought you were nodding to everything i said cuz you were tired"
                y"ofc ! Dude we have been friends for almost our entire lives, what makes you think {b}{i}I{/i}{/b} would be bored in an {i}Art exhibition!{/i}. -_- ?"
                e"yea , you're right. hehehe"
                e "lets go to the next one!"
                $ h=1
                jump artgallerys

        "her expression..":
            $ l+=2
            call uax
            jump artgallerys

label uax:
    y""

    