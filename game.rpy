# Scarlet Mansion Library
# A Game by fujiyama-volcano
# Curated and designed by fujiyama-volcano
# with additional support by sharksfan98
# (c)2013 using MIT License
# https://github.com/fujiyama-volcano/Scarlet-Mansion-Library

# You can place the script of your game in this file.

init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("godawful-beeping-noise.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
            
init python:
    def stats_frame(name, level, hp, maxhp, **properties):
    
        ui.frame(xfill=False, yminimum=None, **properties)
    
        ui.hbox() # (name, "HP", bar) from (level, hp, maxhp)
        ui.vbox() # name from ("HP", bar)
    
        ui.text(name, size=20)
    
        ui.hbox() # "HP" from bar
        ui.text("HP", size=20)
        ui.bar(maxhp, hp,
                xmaximum=150,
                left_bar=Frame("rrslider_full.png", 12, 0),
                right_bar=Frame("rrslider_empty.png", 12, 0),
                thumb=None,
                thumb_shadow=None)
    
        ui.close()
        ui.close()
    
        ui.vbox() # Level from (hp/maxhp)

        ui.text("Lv. %d" % level, xalign=0.5, size=20)
        ui.text("%d/%d" % (hp, maxhp), xalign=0.5, size=20)
    
        ui.close()
        ui.close()
            
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define f = Character('Fujiwara',color="#9F1D35")

define y = Character ('Yukko',color="#00A86B")

define speed = DynamicCharacter(passerby_boy)

    $ narrator = Character(None, window_left_padding=160)
    
scene black with dissolve

show text "Chapter 1\nA Frightening Sight" with Pause(1.5)

scene black with dissolve

scene your_scene_title

e "And now the story really begins."

                                     
    # The game starts here.
       label start:

    $ "H-hey..."

    $ "(Why is it so dark? {w}It's 15:00, isn't it?)"
    
    $ "What should I do about this situation?"

    menu:
    $ "Light a match."
       jump burn
       
    $ "Sit down."
       jump splash
       
       label splash:
           
    $ "Crud!\nI fell into the fountain...{w}(But is it really a fountain? It could be a lake or something)."
         jump speed
         
    $ passerby_boy = "???"
    
         label burn:
           
    $ "Ack! I burned my hand!"
    
    $ "Wow, this will be the best day of my entire life!\n(Not.)"
    
    $ "I guess I could just blindly wander through .\nHere I go!"
         jump splash
         
         label speed:
      play sound "sfx-thud.wav"
      
    speed:"Yo, watch it!"
    
   stop sound "sfx-thud.wav"
   
    speed: "You can't just barge into people like that, moron."
   
    $ "Who the heck are you?"
    
    speed: "The name's /Speed/."
    
    $ "(Poor guy.)"
    
    speed:"And you shouldn't have done that..."
    
    $ "(I think I should get something to defend myself with...)"
   
    menu:
    $ "A sword!"
    jump dark
    
    $ "Magic!"
    jump battle1
    
    label dark:
    
    "You picked the sword, but realize it's much too dark to use it.\nYou decide to use your magic to fight this guy."
     
    jump battle1
    
    label battle1:
       
    $ "This should be easy! \nI have 150 HP at the beginning of the game!"   
    
          python:
        charmax_HP = 150
        char_HP = 150
        
        speedmax_HP = 85
        speed_HP = 85
    
      

   
    return
