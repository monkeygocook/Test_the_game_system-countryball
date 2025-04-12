# The script of the game goes in this file.
init python:
    day = 1
    dayname = "วันจันทร์"
    monthname = "มกราคม"
    time_of_day = "เช้า"  # หรือ "บ่าย", "เย็น", "กลางคืน"
    year = 0000
    work_progress = 0  # กำหนดตัวแปรความคืบหน้า
    inventory = []  # กำหนดตัวแปรคลังไอเท็ม



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

transform big_center:
    zoom 1.0
    xalign 0.5
    yalign 1.0

# The game starts here.

label update_time:
    if time_of_day == "เช้า":
        $ time_of_day = "บ่าย"
    elif time_of_day == "บ่าย":
        $ time_of_day = "เย็น"
    elif time_of_day == "เย็น":
        $ time_of_day = "กลางคืน"
    else:
        $ time_of_day = "เช้า"
        $ day += 1
    return


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
    
    $ day = 8
    $ dayname = "วันศุกร์"
    $ monthname = "พฤษภาคม"
    $ time_of_day = "ค่ำ"
    $ year = 2310

    show screen date_time_overlay

    # These display lines of dialogue.

    e "ไอ้ด้วง เอ็งก็อายุอาณาขนาดนี้แล้ว หาคู่หาเมียได้แล้ว เอ็งจะครองโสดอยู่ผู้เดียวมิได้"

    a "พ่อก็รีบเร่ง ฉันน่ะมีงานเยอะ ยังมิได้แลผู้ใดดอก"

    e "เช่นนั้นก็รีบเสีย แล้วก็วันวิสาขบูชา ข้าจะไปวัดใกล้ๆ เอ็งอยากไปฟังเทศน์ด้วยกันก็ได้นะ"

    a "ไม่ล่ะ ฉันอยากไปฟังเทศน์ที่วัดศรีชุม"

    jump home_day


label home_day:
    scene bg_home_day at small_center

    show screen date_time_overlay
    show screen work_progress_overlay

    menu:
        "ทำงาน":
            $ work_progress += 25  # เพิ่มความคืบหน้า
            if work_progress >= 100:
                $ work_progress = 0  # รีเซ็ตความคืบหน้า
                $ new_item = "เหรียญทอง"  # ไอเท็มที่ได้รับ
                $ inventory.append(new_item)  # เพิ่มไอเท็มในคลัง
                a "งานเสร็จแล้ว! ฉันได้รับ [new_item]!"
            jump home_day

        "ไปตลาด":
            a "ไปตลาดกันเถอะ!"
            jump home_day

        "ดูคลังไอเท็ม":
            call screen inventory_screen
            jump home_day

    
label temple:
    $ day = 12
    $ dayname = "วันอังคาร"
    $ monthname = "พฤษภาคม"
    $ time_of_day = "เช้า"
    $ year = 2310

    show screen date_time_overlay

    scene 134 at big_center

    a "ถึงวัดศรีชุมสักที"





    # This ends the game.
    return
