import arcade

arcade.open_window(800, 800, "Smile")
arcade.set_background_color(arcade.color.DEEP_SPACE_SPARKLE)
arcade.start_render()
signature = arcade.Text("Comp151 003 Jack-o-Lantern", 200, 700, arcade.color.LIGHT_CRIMSON, 20)
signature.draw()
arcade.draw_circle_filled(400, 400, 200, arcade.color.APPLE_GREEN)
arcade.draw_xywh_rectangle_filled(200, 580, 400, 50, arcade.color.BLACK)
arcade.draw_xywh_rectangle_filled(350, 630, 100, 60, arcade.color.BLACK)
arcade.draw_arc_filled(325, 400, 100, 150, arcade.color.YELLOW, 0, 180)
arcade.draw_arc_filled(475, 400, 100, 150, arcade.color.YELLOW, 0, 180)
arcade.draw_triangle_filled(350, 350, 450, 350, 400, 420, arcade.color.YELLOW)
#arcade.draw_arc_outline(400, 300, 200, 100, arcade.color.YELLOW, -180, 0, 15)
arcade.draw_arc_filled(400, 300, 200, 100, arcade.color.YELLOW, -180, 0)
arcade.finish_render()

arcade.run()