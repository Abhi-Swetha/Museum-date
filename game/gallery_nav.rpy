screen gallery_nav():
    hbox:
        yalign 0.1
        xalign 0.5
        spacing 70
        textbutton ("Artworks from Exhibition") action ShowMenu("endings"):
            text_size 54
        if persistent.good_end or persistent.bad_end :
            textbutton ("Ending's Cg's") action ShowMenu("Album"):
                text_size 54
    