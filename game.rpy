# You can place the script of your game in this file.

            
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define f = Character ('Fujiwara',color="#9F1D35")
define y = Character ('Yukko',color="#00A86B")
define t = Character ('Tanaka',color="#")
define speed = DynamicCharacter(passerby_boy)
define g = Character ('Gamma',color="#")

    $ narrator = Character(None, window_left_padding=160)

                                     
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
    
    show text "Chapter 1/The Streetest Fighter" with Pause
    
    $ "(I think I should get something to defend myself with...)"
   
    menu:
    $ "A sword!"
    jump dark
    
    $ "Magic!"
    jump battle1
    
    label dark:
    "You picked the sword, but realized that you don't even have one. Why would you have a sword? You chant a sutra..."
     jump battle1

    label battle1:
    $ "This should be easy! \nI have 150 HP at the beginning of the game!"   
      
    
             
# Boss battle one goes here.
        
    speed: "What in the- you're really good at this, man. Mind if I tag along?"
    $ "...Sure? I don't mind."
    speed: "Lemme just get my-{p}HEY! You busted up my rake!"
    speed: "I can't fight until we get some more swag."
    $ "I don't think we'll be able to find any shops in the dark."
    speed: "Okay, dude.\nWhen it lights up again, we'll fight together!"
    $ "Speed and I decided to travel together."
    speed: "Before I forget..."
        $ player = renpy.input("Who're you?")

    $ player = player.strip()
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    
    if player == "":
        $ player="Lee"
      
      speed:"Nice ta meet ya,%(player)!"
      speed:"So, where to?"
      $ "I..."
      $ "(And so, Speed drags me off to some undescript location.)"
      
      show text "Chapter 2/You Can(not)Heal" with Pause
      
      $ "Speed...where the heck are we?"
      speed: "How would I know,%(player)-bro?"
      $ "I should..."
      
      menu:
          "...Punch him."
          jump punch
        
          "...facepalm."
          jump facepalm
          
          label punch:
        
      play sound sfx-slap.wav
      
      speed: "Yowza!"
      
      stop sound sfx-slap.wav
      
      speed: "Izzat a mook? I'll pummel 'em!"
      $ "(I don't think that did much.)"
         jump shop
         
          label facepalm:
      play sound sfx-slap.wav
      
      stop sound sfx-slap.wav
      
      speed: "What in the-"
       
       jump suspense
       
        label suspense:
      ???: "Excuse me."
      speed: "Huh? Who's this?"
      ???: "I think you have something I need."
      $ "(W-what?!)"
      
        menu:
            "Hey, what are you talking about?"
            jump fujiwara-kun
            
            "And that would be...?"
            jump fujiwara-kun
            
            label fujiwara-kun:
      f "They call me Fujiwara."
      f "I'm looking for the {b}Spectrum Shards{/b}."
      speed: "Spectrum...Shards?"
      f "Yes. To put it simply, Spectrum Shards are pieces of colors."
      $ "Light and color are two different things.{w}Right?"
      $ "What do colors have to do with this blackout?"
      f "I told you it wasn't that simple."
      f "Anyways, the important thing is to retrieve all {b}seven{\b} of them."
      
      play sound sfx-lightbulb.wav
      
      speed: "Hey!"
      
      stop sound sfx-lightbulb.wav
      
      speed: "I found somethin' a lil' while before the blackout."
      f "Interesting. What is it?"
      speed: "Ya see, I found a{b}red rock{/b}the other day."
      f "A red rock? What was it shaped like?"
      speed: "I got it in my pocket right now, Fujiyama."
      f "It's Fujiwara. {p}Now, let me ask {u}you{/u} a question."
      $ "Me?"
      f "%(player), this isn't the time for sarcasm."
      f "Can {u}you{/u} find color in this monochromatic wasteland?"
      
          menu:
              "Red, right?"
              jump red
              
              "What's monochrome?"
              jump definition
              
              "No fair,I'm colorblind!"
              jump colorblind
              
              label colorblind
    f "I see. I shall explain to you,then."
              jump red
              
              label definition:
    f "Monochrome usually means \"of, relating to, or made with a single color or hue\"."
    f "I used it in the sense of \"black and white\"."
              jump red
              
              label red:
    f "Right now,red is the only visible color besides black and white."
    f "My goal is to return colored sight to the population."
    $ "(What about my eyesight?!)"
    speed: "(Or mine?!)"
    $ "(...How the heck did Speed listen to my inner monologue?!)"
    f "To properly liberate ourselves from this blindness..."
    speed: "Go on, Fujiwari."
    
    play sound "sfx-stab.wav"
    
    f "F-Fujiwari!?"
    
    stop sound "sfx-stab.wav"
    
    f "I can't believe it..."
    $ "We can't just stand around."
    $ "We need to get a move on!"
    f "All right, then."
    f "We'll need to be prepared."
    f "The next shard is in the \"Hand of the Mad God\"."
             jump tanaka-kun
             
             label tanaka-kun:
    Ominous Voice: "Fuahahaha!"
    Ominous Voice: "You dare challenge ME?"
    Ominous Voice: "Seek not the Mad God, for he will seek you,if you are worthy."
    t "Fear the power of Kourindou Tanaka!"
    f "Tanaka? Where have I heard that surname before?"
    $ "...I know you..."
    speed: "Ain't he that magician guy?"
    $ "Yep, Rinnosuke \"Kourindou\" Tanaka.{p}A talented sorceror."
    $ "But he's kind of cryptic and weird, so..."
    $ "I don't think too many people like him much."
    t "...%(player).You still count me as your companion, yes?"
            menu:
                "Yeah,man."
                jump tanakadidntcare
                "You're kind of creepy..."
                jump tanakadidntcare
    
             label tanakadidntcare:
    $ "Y-"
    t "Silence, foolish mortal!"
    t "(Hey, is that gangster guy gone yet?)"
    $ "(That's kind of rude...)"
    speed: "I heard that,Tankaya!"
    t "T-Tankaya!?"
    f "He seems to do that with everyone's names. Think nothing of it."
    t "..."
    t "%(player),I didn't anticipate you coming to this place..."
    $ "Me neither, Tanaka."
    t "I've been loitering here, in {b}Jin City{\b}."
    t "It's nice, I guess, but it's kind of crowded, man."
    speed: " 'ey, you! You can't just take my speech patterns!"
    t "Like the investigative one said, \"think nothing of it\"."
    $ "Calm down."
    f "Kourindou Tanaka. Do you have the second Spectrum Shard?"
    t "With the aid of my spellcard, \"Search Sign: Heaven-piercing Drill\", I found a peculiar structure."
    t "It was an amber crystal of the highest caliber. In fact, I..."
    t "Um...{p=1.0)uh...{p=1.0)er..."
    t "I'm afraid my powers have failed me."
    speed: "You lost it!?"
    ???: "Ahahahaha!"
          menu:
              "I-investigate the v-voice."
              jump frightened
              "Tanaka can investigate the voice."
              jump tanakatalk
              
              label frightened:
   $ "H-hey, y-y-you-"
   t "Allow me."
   f "Is this really a good idea?"
   t "Do you not know fear, Kyouya Fujiwara?"
   speed: "(Why does everyone here have a Japanese name?!)"
             jump tanakatalk
             
             label tanakatalk
   ???: "Kyouya Fujiwara! I bring important news from the lord Yama."
   f "Pardon?"
   t "Mortal! Announce your prescence to Rinnosuke Tanaka!"
   ???:"Of course, it wouldn't be right for me to ask such a vast favor without introducing myself."
   ??? "My name is Guan Yu. I am the general of Liu Bei."
   speed: "What? Who?"
   f "..."
   f "An imposter..."
   ??? "What?! Aw... you caught me- whoops! Yeah, I'm Gamma, and I'm just a gatekeeper."
   g "I'm really sorry, but I can't let you pass this point!"
   t "Shall we fight for that honor, then?"
   g "Uh, sure. G-g-go ahead..."
   #Boss Battle 2 is here.
   
   g "Gosh, you guys are strong..."
   g "Hey, can y-you do me a favor?"
   f "Yes?"
   g "My little sister has been training."
   g "She wants to become a guard at the {b}Jade Palace{\b}."
   t "And where might this...Jade Palace be?"
   t "...What? Why are you giving me such a strange look, Speed?"
   speed: "An' what's with you an' switching speech patterns?"
   g "E-excuse m-me, but the Jade Palace is,uh, nearby."
   g "It's located near the Yellow River."
   $ "(If I'm in China, why does everyone have Japanese names?)"
    
      

   
    return
