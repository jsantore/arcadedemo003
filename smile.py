import arcade

arcade.open_window(800, 800, "Smile")
arcade.set_background_color(arcade.color.DEEP_SPACE_SPARKLE)
arcade.start_render()

arcade.draw_circle_filled(400, 400, 200, arcade.color.APPLE_GREEN)
arcade.draw_xywh_rectangle_filled(200, 580, 400, 50, arcade.color.BLACK)
arcade.draw_xywh_rectangle_filled(350, 630, 100, 60, arcade.color.BLACK)
arcade.draw_arc_filled(325, 400, 100, 150, arcade.color.YELLOW, 0, 180)
arcade.finish_render()

arcade.run()