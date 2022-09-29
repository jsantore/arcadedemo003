import arcade

arcade.open_window(1200, 900, "Lots of shapes")
arcade.set_background_color(arcade.color.DARK_BROWN)
arcade.start_render()
arcade.draw_line_strip([(20,30), (200,30), (300, 200), (200, 300), (20,40)],
                       arcade.color.ALIZARIN_CRIMSON, 3)

arcade.finish_render()

arcade.run()
