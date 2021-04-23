"""
File: my_drawing
Name: Shu-Ping Chen
----------------------
Because I like to play 動物森友會 with SWITCH, so I use the similar display of the start of 動物森友會 to draw this.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: Draw a picture that is similar with the display of the start of 動物森友會.
    """
    window = GWindow(width=1000, height=600, title='drawing')

    # Set sea
    sea = GRect(1000, 300, x=0, y=150)
    sea.filled = True
    sea.fill_color = 'LightSkyBlue'
    sea.color = 'LightSkyBlue'
    window.add(sea)

    # Set ground
    for i in range(20):
        wood = GRect(50, 150, x=i * 50, y=450)
        wood.filled = True
        wood.fill_color = 'grey'
        window.add(wood)

    # Set wood
    for i in range(10):
        wood = GRect(40, 150, x=i * 100 + 30, y=350)
        wood.filled = True
        wood.fill_color = 'SaddleBrown'
        wood.color = 'SaddleBrown'
        window.add(wood)

    wood_long = GRect(1000, 40, x=0, y=375)
    wood_long.filled = True
    wood_long.fill_color = 'SaddleBrown'
    wood_long.color = 'SaddleBrown'
    window.add(wood_long)

    for i in range(10):
        triangle = GPolygon()
        triangle.add_vertex((i * 100 + 30 + 20, 325))
        triangle.add_vertex((i * 100 + 30, 350))
        triangle.add_vertex((i * 100 + 30 + 40, 350))
        triangle.filled = True
        triangle.fill_color = 'SaddleBrown'
        triangle.color = 'SaddleBrown'
        window.add(triangle)

    # Set 哆啦A夢
    # hand's line
    a_l_hand_1 = GOval(52, 30, x=81.5, y=415.5)
    a_l_hand_1.filled = True
    a_l_hand_1.fill_color = 'blue'
    window.add(a_l_hand_1)

    a_r_hand_1 = GOval(52, 30, x=186.5, y=415.5)
    a_r_hand_1.filled = True
    a_r_hand_1.fill_color = 'blue'
    window.add(a_r_hand_1)

    # body
    a_body_1 = GOval(97.5, 170, x=110, y=380)
    a_body_1.filled = True
    a_body_1.fill_color = 'blue'
    window.add(a_body_1)

    a_body_2 = GRect(100, 100, x=110, y=515)
    a_body_2.filled = True
    a_body_2.fill_color = 'grey'
    a_body_2.color = 'grey'
    window.add(a_body_2)

    a_body_ground_1 = GLine(150, 510, 150, 600)
    window.add(a_body_ground_1)
    a_body_ground_2 = GLine(200, 510, 200, 600)
    window.add(a_body_ground_2)

    # hand
    a_l_hand_1 = GOval(50, 22, x=82, y=420)
    a_l_hand_1.filled = True
    a_l_hand_1.fill_color = 'blue'
    a_l_hand_1.color = 'blue'
    window.add(a_l_hand_1)

    a_l_hand_2 = GOval(35, 35, x=65, y=420)
    a_l_hand_2.filled = True
    a_l_hand_2.fill_color = 'white'
    window.add(a_l_hand_2)

    a_r_hand_1 = GOval(50, 25, x=186, y=420)
    a_r_hand_1.filled = True
    a_r_hand_1.fill_color = 'blue'
    a_r_hand_1.color = 'blue'
    window.add(a_r_hand_1)

    a_r_hand_2 = GOval(35, 35, x=220, y=420)
    a_r_hand_2.filled = True
    a_r_hand_2.fill_color = 'white'
    window.add(a_r_hand_2)

    # face
    a_face_1 = GOval(120, 120, x=100, y=300)
    a_face_1.filled = True
    a_face_1.fill_color = 'blue'
    window.add(a_face_1)

    a_face_2 = GOval(100, 95, x=110, y=320)
    a_face_2.filled = True
    a_face_2.fill_color = 'white'
    window.add(a_face_2)

    # left eye
    a_l_eye_1 = GOval(25, 30, x=135, y=310)
    a_l_eye_1.filled = True
    a_l_eye_1.fill_color = 'white'
    window.add(a_l_eye_1)

    a_l_eye_2 = GOval(10, 12, x=145, y=320)
    a_l_eye_2.filled = True
    window.add(a_l_eye_2)

    a_l_eye_3 = GOval(5, 5, x=149, y=322.5)
    a_l_eye_3.filled = True
    a_l_eye_3.fill_color = 'white'
    window.add(a_l_eye_3)

    # right eye
    a_r_eye_1 = GOval(25, 30, x=160, y=310)
    a_r_eye_1.filled = True
    a_r_eye_1.fill_color = 'white'
    window.add(a_r_eye_1)

    a_r_eye_2 = GOval(10, 12, x=165, y=320)
    a_r_eye_2.filled = True
    window.add(a_r_eye_2)

    a_r_eye_3 = GOval(5, 5, x=166, y=322.5)
    a_r_eye_3.filled = True
    a_r_eye_3.fill_color = 'white'
    window.add(a_r_eye_3)

    # mouse
    mouse = GOval(80, 45, x=120, y=350)
    window.add(mouse)

    white_space = GRect(80, 25, x=120, y=350)
    # build the white space to cover the upper part of the circle, 'line_5',  that draw as the mouse.
    white_space.filled = True
    white_space.fill_color = 'white'
    white_space.color = 'white'
    window.add(white_space)

    # nose
    a_nose1 = GOval(20, 20, x=150, y=334)
    a_nose1.filled = True
    a_nose1.fill_color = 'red'
    window.add(a_nose1)

    a_nose2 = GOval(5, 5, x=155, y=340)
    a_nose2.filled = True
    a_nose2.fill_color = 'white'
    a_nose2.color = 'white'
    window.add(a_nose2)

    # beard
    a_r_1 = GLine(150, 355, 115, 345)
    window.add(a_r_1)
    a_r_2 = GLine(150, 365, 110, 365)
    window.add(a_r_2)
    a_r_3 = GLine(150, 375, 115, 385)
    window.add(a_r_3)
    a_l_1 = GLine(170, 355, 205, 345)
    window.add(a_l_1)
    a_l_2 = GLine(170, 365, 210, 365)
    window.add(a_l_2)
    a_l_3 = GLine(170, 375, 205, 385)
    window.add(a_l_3)
    a_4 = GLine(160, 355, 160, 395)
    window.add(a_4)

    # stomach
    a_stomach = GOval(80, 80, x=119, y=410)
    a_stomach.filled = True
    a_stomach.fill_color = 'white'
    window.add(a_stomach)

    # pocket
    a_pocket_1 = GOval(60, 50, x=127.5, y=430)
    a_pocket_1.filled = True
    a_pocket_1.fill_color = 'white'
    window.add(a_pocket_1)

    a_pocket_2 = GRect(60, 25, x=127.5, y=430)
    a_pocket_2.filled = True
    a_pocket_2.fill_color = 'white'
    a_pocket_2.color = 'white'
    window.add(a_pocket_2)

    a_pocket_3 = GLine(128, 455, 190, 455)
    window.add(a_pocket_3)

    # red ring
    a_ring = GRect(80, 5, x=120, y=410)
    a_ring.filled = True
    a_ring.fill_color = 'red'
    window.add(a_ring)

    # bell
    a_bell_1 = GOval(25, 25, x=147, y=415)
    a_bell_1.filled = True
    a_bell_1.fill_color = 'yellow'
    window.add(a_bell_1)

    a_bell_2 = GRect(21, 3, x=149, y=420)
    a_bell_2.filled = True
    a_bell_2.fill_color = 'yellow'
    window.add(a_bell_2)

    a_bell_3 = GOval(5, 5, x=158, y=428)
    a_bell_3.filled = True
    a_bell_3.fill_color = 'yellow'
    window.add(a_bell_3)

    a_bell_4 = GLine(159.5, 432.5, 159.5, 440)
    window.add(a_bell_4)

    # shoe
    a_l_shoe = GOval(60, 25, x=100, y=500)
    a_l_shoe.filled = True
    a_l_shoe.fill_color = 'white'
    window.add(a_l_shoe)

    a_r_shoe = GOval(60, 25, x=160, y=500)
    a_r_shoe.filled = True
    a_r_shoe.fill_color = 'white'
    window.add(a_r_shoe)

    # Set 大嘴鳥
    # body
    b_body_1 = GRect(98.75, 40, x=400.5, y=340)
    b_body_1.filled = True
    b_body_1.fill_color = 'FireBrick'
    b_body_1.color = 'FireBrick'
    window.add(b_body_1)

    b_body_2 = GOval(100, 100, x=400, y=355)
    b_body_2.filled = True
    b_body_2.fill_color = 'Sienna'
    b_body_2.color = 'Sienna'
    window.add(b_body_2)

    b_body_3 = GOval(100, 100, x=400, y=300)
    b_body_3.filled = True
    b_body_3.fill_color = 'FireBrick'
    b_body_3.color = 'FireBrick'
    window.add(b_body_3)

    b_body_4 = GRect(98.75, 35, x=400.5, y=380)
    b_body_4.filled = True
    b_body_4.fill_color = 'goldenrod'
    b_body_4.color = 'goldenrod'
    window.add(b_body_4)

    # body's texture
    b_texture_1 = GRect(5, 19, x=400.5, y=400)
    b_texture_1.filled = True
    b_texture_1.fill_color = 'Sienna'
    b_texture_1.color = 'Sienna'
    window.add(b_texture_1)

    b_texture_2 = GRect(10, 19, x=425.5, y=400)
    b_texture_2.filled = True
    b_texture_2.fill_color = 'Sienna'
    b_texture_2.color = 'Sienna'
    window.add(b_texture_2)

    b_texture_3 = GRect(15, 19, x=440.5, y=410)
    b_texture_3.filled = True
    b_texture_3.fill_color = 'goldenrod'
    b_texture_3.color = 'goldenrod'
    window.add(b_texture_3)

    b_texture_4 = GPolygon()
    b_texture_4.add_vertex((440.5, 429))
    b_texture_4.add_vertex((455.5, 415))
    b_texture_4.add_vertex((455.5, 429))
    b_texture_4.filled = True
    b_texture_4.fill_color = 'Sienna'
    b_texture_4.color = 'Sienna'
    window.add(b_texture_4)

    b_texture_5 = GPolygon()
    b_texture_5.add_vertex((455.5, 415))
    b_texture_5.add_vertex((470, 390))
    b_texture_5.add_vertex((470, 415))
    b_texture_5.filled = True
    b_texture_5.fill_color = 'Sienna'
    b_texture_5.color = 'Sienna'
    window.add(b_texture_5)

    b_texture_6 = GRect(5, 25, x=470, y=390)
    b_texture_6.filled = True
    b_texture_6.fill_color = 'Sienna'
    b_texture_6.color = 'Sienna'
    window.add(b_texture_6)

    b_texture_7 = GRect(10, 15, x=490, y=400)
    b_texture_7.filled = True
    b_texture_7.fill_color = 'Sienna'
    b_texture_7.color = 'Sienna'
    window.add(b_texture_7)

    b_texture_8 = GPolygon()
    b_texture_8.add_vertex((496, 400))
    b_texture_8.add_vertex((500, 400))
    b_texture_8.add_vertex((500, 390))
    b_texture_8.filled = True
    b_texture_8.fill_color = 'Sienna'
    b_texture_8.color = 'Sienna'
    window.add(b_texture_8)

    # mouse
    b_mouse_1 = GOval(80, 40, x=380, y=345)
    b_mouse_1.filled = True
    b_mouse_1.fill_color = 'DarkOrange'
    b_mouse_1.color = 'DarkOrange'
    window.add(b_mouse_1)

    b_mouse_2 = GOval(30, 30, x=430, y=351)
    b_mouse_2.filled = True
    b_mouse_2.fill_color = 'DarkOrange'
    b_mouse_2.color = 'DarkOrange'
    window.add(b_mouse_2)

    b_mouse_3 = GOval(28, 28, x=382, y=353)
    b_mouse_3.filled = True
    b_mouse_3.fill_color = 'DarkOrange'
    b_mouse_3.color = 'DarkOrange'
    window.add(b_mouse_3)

    # eye
    b_l_eye_1 = GOval(35, 35, x=412, y=310)
    b_l_eye_1.filled = True
    b_l_eye_1.fill_color = 'white'
    window.add(b_l_eye_1)

    b_r_eye_1 = GOval(37, 37, x=447, y=317)
    b_r_eye_1.filled = True
    b_r_eye_1.fill_color = 'white'
    window.add(b_r_eye_1)

    b_l_eye_2 = GOval(25, 25, x=422, y=315)
    b_l_eye_2.filled = True
    window.add(b_l_eye_2)

    b_r_eye_2 = GOval(27, 27, x=447, y=322)
    b_r_eye_2.filled = True
    window.add(b_r_eye_2)

    # leg
    b_l_leg_1 = GRect(3, 40, x=440, y=455)
    b_l_leg_1.filled = True
    window.add(b_l_leg_1)

    for i in range(5):
        b_l_leg_2 = GLine(443 - 0.5 * i, 495 + 0.5 * i, 413 - 0.5 * i, 485 + 0.5 * i)
        window.add(b_l_leg_2)
        b_l_leg_3 = GLine(443 - 0.5 * i, 495 + 0.5 * i, 410 - 0.5 * i, 495 + 0.5 * i)
        window.add(b_l_leg_3)
        b_l_leg_4 = GLine(443 - 0.5 * i, 495 + 0.5 * i, 413 - 0.5 * i, 505 + 0.5 * i)
        window.add(b_l_leg_4)

    b_r_leg_1 = GRect(3, 40, x=455, y=455)
    b_r_leg_1.filled = True
    window.add(b_r_leg_1)
    for i in range(5):
        b_r_leg_2 = GLine(458 - 0.5 * i, 495 + 0.5 * i, 488 - 0.5 * i, 485 + 0.5 * i)
        window.add(b_r_leg_2)
        b_r_leg_3 = GLine(458 - 0.5 * i, 495 + 0.5 * i, 488 - 0.5 * i, 495 + 0.5 * i)
        window.add(b_r_leg_3)
        b_r_leg_4 = GLine(458 - 0.5 * i, 495 + 0.5 * i, 488 - 0.5 * i, 505 + 0.5 * i)
        window.add(b_r_leg_4)

    # Set Open Chan
    # hair

    o_hair_1 = GOval(190, 190, x=655, y=300)
    o_hair_1.filled = True
    o_hair_1.fill_color = 'DeepSkyBlue'
    window.add(o_hair_1)

    o_hair_1 = GOval(160, 160, x=670, y=315)
    o_hair_1.filled = True
    o_hair_1.fill_color = 'Red'
    o_hair_1.color = 'white'
    window.add(o_hair_1)

    o_hair_1 = GOval(130, 130, x=685, y=330)
    o_hair_1.filled = True
    o_hair_1.fill_color = 'LimeGreen'
    o_hair_1.color = 'white'
    window.add(o_hair_1)

    for i in range(4):
        wood = GRect(50, 150, x=650 + i * 50, y=450)
        wood.filled = True
        wood.fill_color = 'grey'
        window.add(wood)

    o_hair_2 = GRect(400, 25, x=600, y=390)
    o_hair_2.filled = True
    o_hair_2.fill_color = 'SaddleBrown'
    o_hair_2.color = 'SaddleBrown'
    window.add(o_hair_2)

    o_hair_3 = GRect(40, 120, x=730, y=380)
    o_hair_3.filled = True
    o_hair_3.fill_color = 'SaddleBrown'
    o_hair_3.color = 'SaddleBrown'
    window.add(o_hair_3)

    for i in range(2):
        o_hair_4 = GRect(40, 90, x=630 + i * 200, y=410)
        o_hair_4.filled = True
        o_hair_4.fill_color = 'SaddleBrown'
        o_hair_4.color = 'SaddleBrown'
        window.add(o_hair_4)

    for i in range(2):
        o_hair_5 = GRect(60, 34, x=670 + i * 100, y=415)
        o_hair_5.filled = True
        o_hair_5.fill_color = 'LightSkyBlue'
        o_hair_5.color = 'LightSkyBlue'
        window.add(o_hair_5)

    # hand
    for i in range(2):
        o_hand = GOval(50, 10, x=680 + 90 * i, y=425)
        o_hand.filled = True
        o_hand.fill_color = 'Moccasin'
        window.add(o_hand)

    # leg
    for i in range(2):
        o_hand = GOval(10, 50, x=730 + 30 * i, y=470)
        o_hand.filled = True
        o_hand.fill_color = 'Moccasin'
        window.add(o_hand)

    # tail
    o_tail = GOval(30, 10, x=705, y=470)
    o_tail.filled = True
    o_tail.fill_color = 'Moccasin'
    window.add(o_tail)

    # body
    o_body = GOval(80, 90, x=710, y=400)
    o_body.filled = True
    o_body.fill_color = 'Moccasin'
    window.add(o_body)

    # head
    o_head = GOval(100, 80, x=700, y=350)
    o_head.filled = True
    o_head.fill_color = 'Moccasin'
    window.add(o_head)

    # mouth
    o_mouth_1 = GOval(40, 30, x=730, y=390)
    o_mouth_1.filled = True
    o_mouth_1.fill_color = 'Moccasin'
    window.add(o_mouth_1)

    o_mouth_2 = GRect(40, 15, x=730, y=390)
    o_mouth_2.filled = True
    o_mouth_2.fill_color = 'Moccasin'
    o_mouth_2.color = 'Moccasin'
    window.add(o_mouth_2)

    # eye
    o_l_eye = GOval(20, 20, x=715, y=370)
    o_l_eye.filled = True
    window.add(o_l_eye)

    o_r_eye = GOval(20, 20, x=765, y=370)
    o_r_eye.filled = True
    window.add(o_r_eye)

    # nose
    o_nose = GOval(20, 15, x=740, y=390)
    o_nose.filled = True
    o_nose.fill_color = 'Peru'
    window.add(o_nose)

    # Set flag
    for i in range(15):
        flag_1 = GLine(950 + 0.5 * i, 500, 950 + 0.5 * i, 199)
        window.add(flag_1)

    flag_2 = GRect(350, 80, x=600, y=200)
    flag_2.filled = True
    flag_2.fill_color = 'red'
    window.add(flag_2)

    flag_text = GLabel('三人團購,即可享優惠價', x=635, y=255)
    flag_text.font = '-20'
    window.add(flag_text)

    # Set slogan
    slogan_text = GLabel('stanCode 校友會', x=70, y=130)
    slogan_text.font = '-80'
    window.add(slogan_text)

    # Set switch
    switch = GRect(135, 135, x=810, y=10)
    switch.filled = True
    switch.fill_color = 'red'
    window.add(switch)

    for i in range(2):
        for j in range(2):
            switch_1 = GOval(25, 25, x=833 + 60 * i, y=16 + 60 * j)
            switch_1.filled = True
            switch_1.fill_color = 'white'
            switch_1.color = 'white'
            window.add(switch_1)
        switch_2 = GRect(25, 85, x=843 + 40 * i, y=16)
        switch_2.filled = True
        switch_2.fill_color = 'white'
        switch_2.color = 'white'
        window.add(switch_2)
        switch_3 = GRect(15, 58, x=832.5 + 70 * i, y=28)
        switch_3.filled = True
        switch_3.fill_color = 'white'
        switch_3.color = 'white'
        window.add(switch_3)
        switch_4 = GOval(20, 20, x=840, y=20 + 55 * i)
        switch_4.filled = True
        switch_4.fill_color = 'red'
        switch_4.color = 'red'
        window.add(switch_4)
        switch_5 = GRect(10, 75, x=850, y=20)
        switch_5.filled = True
        switch_5.fill_color = 'red'
        switch_5.color = 'red'
        window.add(switch_5)
        window.add(switch_4)
        switch_6 = GRect(10, 55, x=840.25, y=25.5)
        switch_6.filled = True
        switch_6.fill_color = 'red'
        switch_6.color = 'red'
        window.add(switch_6)
        switch_7 = GOval(15, 15, x=842, y=31)
        switch_7.filled = True
        switch_7.fill_color = 'white'
        switch_7.color = 'white'
        window.add(switch_7)
        switch_8 = GOval(15, 15, x=890, y=50)
        switch_8.filled = True
        switch_8.fill_color = 'red'
        switch_8.color = 'red'
        window.add(switch_8)

    switch_text_1 = GLabel('N I N T E N D O', x=825, y=120)
    switch_text_1.font = '-11'
    switch_text_1.color = 'white'
    window.add(switch_text_1)

    switch_text_2 = GLabel('SWITCH', x=825, y=145)
    switch_text_2.font = '-21'
    switch_text_2.color = 'white'
    window.add(switch_text_2)

    switch_text_2 = GLabel('TM', x=928, y=140)
    switch_text_2.font = '-7'
    switch_text_2.color = 'white'
    window.add(switch_text_2)




if __name__ == '__main__':
    main()
