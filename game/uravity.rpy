define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#c88e8e",what_font="font/LiberationSerif-Regular.ttf")
$ global h
$ global x

label uravity:
    scene uravity
    with fade
    e "damn, This one's a pure master piece!"
    y"god dang, yeaa! The artist must have poured their heart and soul into this"
    e"the expresstion show clearly how she feels, man even I can feel the dispair through the page"
    e"offfhhh.."
    y"..."
    e"what do think the experssion means? like one a more specific note"
    e"I think the experssion seems deperate and dispaired"
    y"what abt you?"

    menu:
        "her expression..":
            $ l+=2
            call uax
            

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
                e "lets go to the next one!"
                $ h=1
    jump artgallerys            
    return

label uax:
    y"her experssion seems more helpless than desperate"
    e"huh? wait.."
    e"yeaa i get what you mean!"
    y"btw doesn't she remind you of a character from an anime?"
    e"oh yeaa! The one with the chubby cheeks!"
    y"yeaa, Damn, I didn't expect to see an anime inspired character here"
    e"me too, but still it looks really good!!"
    y"I want see their other works, from anime now"
    e"I guess you could check out their insta {b}{i}bumble_.b._{/i}{/b} or their yt {b}{i}Abhibi_lv1{/i}{/b}"
    y"ohh , yess!!!"
    return