import arcade
import random
arcade.open_window(800, 800, "Sword in Stone")
coposx = []
coposy= []

for i in range(150):
    coposx.append(random.randint(0, 800))
    coposy.append(random.randint(0, 800))

#/ escenario
def draw_escenario():
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.csscolor.GREEN)

def draw_castillo():
    #/ MAIN frame castillo
    arcade.draw_lrtb_rectangle_filled(150, 700, 300, 20, arcade.csscolor.ANTIQUE_WHITE)
    arcade.draw_lrtb_rectangle_outline(150, 700, 300, 20, arcade.csscolor.BLACK)

    #/puerta
    arcade.draw_lrtb_rectangle_outline(361, 517, 200, 20, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(439, 200, 80, arcade.csscolor.SADDLE_BROWN )
    arcade.draw_circle_outline(439, 200 , 80, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(361, 517, 200, 20, arcade.csscolor.SADDLE_BROWN)

    #/torres laterales
    for i in range(2):
        arcade.draw_lrtb_rectangle_outline(150 + i*450, 250 + i*450, 450, 300, arcade.csscolor.BLACK)
        arcade.draw_triangle_outline(150 + i*450, 450, 250+i*450, 450, 200 + i*450, 600, arcade.csscolor.BLACK)
        arcade.draw_lrtb_rectangle_filled(150 + i*450, 250 + i*450, 450, 200, arcade.csscolor.ANTIQUE_WHITE)
        arcade.draw_triangle_filled(150 + i*450, 450, 250 + i*450, 450, 200 + i*450, 600, arcade.csscolor.DARK_RED)

    #/TORRE medio
    arcade.draw_lrtb_rectangle_outline(350, 450, 450, 300, arcade.csscolor.BLACK)
    arcade.draw_triangle_outline(350, 500, 475, 450, 412, 600, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(350, 475, 500, 300, arcade.csscolor.ANTIQUE_WHITE)
    arcade.draw_triangle_filled(350, 500, 475, 500, 412.5, 700, arcade.csscolor.DARK_RED)
    arcade.draw_lrtb_rectangle_filled(175, 225, 425, 325, arcade.csscolor.LIGHT_CYAN)
    arcade.draw_triangle_outline(412.5, 700, 470, 750, 470, 650, arcade.csscolor.BLACK, 2)
    arcade.draw_lrtb_rectangle_outline(470, 700, 750, 650, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(470, 700, 750, 650, arcade.csscolor.RED)
    arcade.draw_lrtb_rectangle_filled(470, 699, 720, 680, arcade.csscolor.YELLOW)

def draw_nieve(x,y):
#/Nieve
    for i in range (len(x)):
        arcade.draw_circle_filled(x[i], y[i], 5, arcade.csscolor.SNOW)
        coposy[i] -=4
        if coposy[i]== 0:
            coposy[i] = 800

def on_draw(delta_time):
    arcade.start_render()
    draw_escenario()
    draw_castillo()
    draw_nieve(coposx, coposy)

def main():
    arcade.set_background_color(arcade.csscolor.DARK_BLUE)
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


main()