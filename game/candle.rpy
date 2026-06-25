define e = Character("Laura",color="#ffeba9")
define y = Character("You", color="#ffffff")

$ global h
$ global x

label candle:
    scene candle
    with fade
    e "i love the use of watercolor for the background!"
    y "This is also really nicely blends the background with the characters"
    e "it adds a lot of dimention and creates a soft vibe around the painting"
    y "i think the girl standing could have been drawn slightly better.."
    y"..."
    e "yeaa, but over all it looks really good!!"
    e "don't you think?"

    menu:
        "..... ":

            y"(shii.. i completely zoned out, stareing at the artwork)"
            y"(what did she ask ? )"
            y"('you gotta agree with everything the girl says'-How to get a girlfriend 101)"
            y"I am not sure, "
            e"oh..."
            e"well..--\('^')/--"
            y "yeaa,\n ;;-_- \n haha...."

            $ l += (x-h*0.25)
            $ h+=1

            if h>=3:
                e"dude, are you okey? you have been zoning out for a while now"

            if h>3:
                e"are you sure you are alright?"
                y"uhhh...yeaa, I-sorry,was admireing the piece and..zoned out (;'')~"
                y"(what did she ask? )"
                y"(i think she asked smt , ryt? )"
                call cax
                e"so you {b}{i}DID{/b}{/i} think there was more to it! "
                e"i thought you were nodding to everything i said cuz you were tired"
                y"ofc ! Dude we have been friends for almost our entire lives, what makes you think {b}{i}I{/i}{/b} would be bored in an {i}Art exhibition!{/i}. -_- ?"
                e"yea , you're right. hehehe"
                e "lets go to the next one!"
                $ h=1
                jump artgallerys

        "yeaa.....":
            $ l+=2
            call cax
            jump artgallerys
    return

label cax:
    y "yea...."
    y "The composition looks really nice, the colors are complementing the piece as a whole and the use of color theory and the flow of fabrics teh artist has crearted an really well made piece worth being displayed !"
    y"apart from that the fact that the girl behide is holding a knife is something you only notice once you really look , even tho the knife is given extra detail!!"
    y"this might be my most favorite piece!!!"
    e"sure seems like it!!"
    e"hehe"
    y"ugh.. come on.. -//^//-"
    e"I personnally love the way the curtains are drawn !, they give the feel of a soft midnight brezee, !"
    e" the artist has a way in drawing fabrics , that i love ! i have seen their work a lot in insta "
    y"really??"
    e"yea, they are called {b}bumble_.b._{/b}, you should check them out!!"
    return