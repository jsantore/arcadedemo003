import arcade

arcade.open_window(1200, 900, "Lots of shapes")
arcade.set_background_color(arcade.color.DARK_BROWN)
arcade.start_render()
arcade.draw_line_strip([(20,30), (200,30), (300, 200), (200, 300), (20,40)],
                       arcade.color.ALIZARIN_CRIMSON, 3)
arcade.draw_lrtb_rectangle_filled(320, 420, 300, 50, arcade.color.ELECTRIC_INDIGO)
arcade.draw_lrtb_rectangle_outline(450, 550, 300, 50, arcade.color.BRINK_PINK, 12)
arcade.draw_xywh_rectangle_filled(380, 120, 300, 80, arcade.color.AQUAMARINE)
arcade.draw_xywh_rectangle_outline(10, 10, 680, 300, arcade.color.BRIGHT_CERULEAN, 8)


arcade.finish_render()

arcade.run()
