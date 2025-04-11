# The script of the game goes in this file.

image Au_left = "Au_left.png"
image Au_right = "Au_right.png"


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("บิดา")
define a = Character("ด้วง")

transform small_left:
    zoom 0.25
    xalign -0.0
    yalign 1.0

transform small_right:
    zoom 0.25
    xalign 1.0
    yalign 1.0

transform small_center:
    zoom 0.5
    xalign 0.5
    yalign 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_home at small_center

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Au_right at small_left
    show Au_left at small_right
    

    
    # These display lines of dialogue.

    e "ไอ้ด้วง เอ็งก็อายุอาณาขนาดนี้แล้ว หาคู่หาเมียได้แล้ว เอ็งจะครองโสดอยู่ผู้เดียวมิได้"

    a "พ่อก็รีบเร่ง ฉันน่ะมีงานเยอะ ยังมิได้แลผู้ใดดอก"

    e "เช่นนั้นก็รีบเสีย แล้วก็วันวิสาขบูชา ข้าจะไปวัดใกล้ๆ เอ็งอยากไปฟังเทศน์ด้วยกันก็ได้นะ"

    a "ไม่ล่ะ ฉันอยากไปฟังเทศน์ที่วัดศรีชุม"

    # This ends the game.

    return
