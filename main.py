def on_overlap_tile(sprite, location):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_player4_connected():
    global easter_bunny_4
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile1
    """)):
        easter_bunny_4 = sprites.create(img("""
                ..................................................
                            ...................aaa............................
                            ..................aaaa........aa..................
                            ..................aaaaa......aaa..................
                            .................aaaaaa.....aaaaa.................
                            ................aaaaaaa....aaaaaaa................
                            ................aaaaaaa....aaaaaaa................
                            ...............aaaaccaa....aaaaaaa................
                            ...............aaaaccaa...aaaaccaa................
                            ...............aaacccca...aaacccaa................
                            ...............aaaccccaa..aaacccaa................
                            ...............aaaccccaa..aaacccaa................
                            ...............aacccccaa..aaccccaa................
                            ...............aacccccaa..aacccaaa................
                            ...............aaccccaaa.aaacccaaa................
                            ...............aaccccaaaaaaacccaa.................
                            ...............aaaaccaaaaaaaaaaaa.................
                            ............aaaaaaaacaaaaaaaaaaaaaa...............
                            ............aaaaaaaaaaaaaaaaaaaaaaaa..............
                            ...........aaaaaaaaffaaaaaaffaaaaaaaa.............
                            ..........aaaaaaaafffaaaaaaffffaaaaaa.............
                            ..........aaaaaaaafffaaaaaffffaaaaaaa.............
                            ..........aaaaaaaafffaaaaaaffaaaaaaaa.............
                            ..........aaaaaaaaffaaaaaaafaaaaaaaaa.............
                            ..........aaaaaaaaaaaaaaaaaaaaaaaaaaa.............
                            ..........aaaaaaaaaaaaaaffaaaaaaaaaaa.............
                            ..........aaaaaaaaaaaaaaffaaaaaaaaaa..............
                            ...........aaaaaaaaaaaaafaaaaaaaaaaa..............
                            ............aaaaaaaaaafafaaaaaaaaaa...............
                            .............aaaaaaaaaffafafaaaaaa................
                            ..............aaaaaaaaaaaafaaaaaa.......aaa.......
                            .....aaa......aaaaaaaaaaaaaaaaaaaa.....aaaa.......
                            ....aaaaa....aaaaaaaaaaaaaaaaaaaaaaa..aaaaa.......
                            ....aaaaaa..aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.......
                            ....aaaaaaaaaaaaaaaaaaaacccccaaaaaaaaaaaaaa.......
                            ....aaaaaaaaaaaaaaaaaaacccccccaaaaaaaaaaaa........
                            ....aaaaaaaaaaaaaaaaaccccccccccaaaaaaaaaaa........
                            .....aaaaaaaaaaaaaaaccccccccccccaaaaaaaaa.........
                            ......aaaaaaaaaaaaaaccccccccccccaaaaaaaaa.........
                            ......aaaaaaaaaaaaacccccccccccccaaaaaaaaa.........
                            .......aaaaaaaaaaaacccccccccccccaaaaaaa...........
                            ........aaaaaaaaaaacccccccccccccaaaaaaa...........
                            ........aaaaaaaaaaaccccccccccccaaaaaaaa...........
                            ........aaaaaaaaaaaccccccccccccaaaaaaaa...........
                            ........aaaaaaaaaaaacccccccccaaaaaaaaaa...........
                            .........aaaaaaaaaaaccccccccaaaaaaaaaaa...........
                            .........aaaaaaaaaaaacccccaaaaaaaaaaaaa...........
                            .........aaaaaaa.aaaaaaa.........aaaaa............
                            .........aaaaaa...................aaaa............
                            .........aaaaa....................aaaa............
            """),
            SpriteKind.player)
        controller.player4.move_sprite(easter_bunny_4)
        scene.camera_follow_sprite(easter_bunny_4)
        tiles.place_on_tile(easter_bunny_4, value)
        tiles.set_tile_at(value, assets.tile("""
            transparency16
        """))
controller.player4.on_event(ControllerEvent.CONNECTED, on_player4_connected)

def on_overlap_tile2(sprite2, location2):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile2)

def on_player3_connected():
    global easter_bunny_3
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile5
    """)):
        easter_bunny_3 = sprites.create(img("""
                ..................................................
                            ...................555............................
                            ..................5555........55..................
                            ..................55555......555..................
                            .................555555.....55555.................
                            ................5555555....5555555................
                            ................5555555....5555555................
                            ...............55554455....5555555................
                            ...............55554455...55554455................
                            ...............55544445...55544455................
                            ...............555444455..55544455................
                            ...............555444455..55544455................
                            ...............554444455..55444455................
                            ...............554444455..55444555................
                            ...............554444555.555444555................
                            ...............554444555555544455.................
                            ...............555544555555555555.................
                            ............55555555455555555555555...............
                            ............555555555555555555555555..............
                            ...........55555555ff555555ff55555555.............
                            ..........55555555fff555555ffff555555.............
                            ..........55555555fff55555ffff5555555.............
                            ..........55555555fff555555ff55555555.............
                            ..........55555555ff5555555f555555555.............
                            ..........555555555555555555555555555.............
                            ..........55555555555555ff55555555555.............
                            ..........55555555555555ff5555555555..............
                            ...........5555555555555f55555555555..............
                            ............5555555555f5f5555555555...............
                            .............555555555ff5f5f555555................
                            ..............555555555555f555555.......555.......
                            .....555......55555555555555555555.....5555.......
                            ....55555....55555555555555555555555..55555.......
                            ....555555..5555555555555555555555555555555.......
                            ....555555555555555555554444455555555555555.......
                            ....55555555555555555554444444555555555555........
                            ....55555555555555555444444444455555555555........
                            .....555555555555555444444444444555555555.........
                            ......55555555555555444444444444555555555.........
                            ......55555555555554444444444444555555555.........
                            .......55555555555544444444444445555555...........
                            ........5555555555544444444444445555555...........
                            ........5555555555544444444444455555555...........
                            ........5555555555544444444444455555555...........
                            ........5555555555554444444445555555555...........
                            .........555555555554444444455555555555...........
                            .........555555555555444445555555555555...........
                            .........5555555.5555555.........55555............
                            .........555555...................5555............
                            .........55555....................5555............
            """),
            SpriteKind.player)
        controller.player3.move_sprite(easter_bunny_3)
        scene.camera_follow_sprite(easter_bunny_3)
        tiles.place_on_tile(easter_bunny_3, value2)
        tiles.set_tile_at(value2, assets.tile("""
            transparency16
        """))
controller.player3.on_event(ControllerEvent.CONNECTED, on_player3_connected)

def on_on_overlap(sprite3, otherSprite):
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_player2_connected():
    global easter_bunny_2
    for value3 in tiles.get_tiles_by_type(assets.tile("""
        myTile4
    """)):
        easter_bunny_2 = sprites.create(img("""
                ..................................................
                            ...................222............................
                            ..................2222........22..................
                            ..................22222......222..................
                            .................222222.....22222.................
                            ................2222222....2222222................
                            ................2222222....2222222................
                            ...............22223322....2222222................
                            ...............22223322...22223322................
                            ...............22233332...22233322................
                            ...............222333322..22233322................
                            ...............222333322..22233322................
                            ...............223333322..22333322................
                            ...............223333322..22333222................
                            ...............223333222.222333222................
                            ...............223333222222233322.................
                            ...............222233222222222222.................
                            ............22222222322222222222222...............
                            ............222222222222222222222222..............
                            ...........22222222ff222222ff22222222.............
                            ..........22222222fff222222ffff222222.............
                            ..........22222222fff22222ffff2222222.............
                            ..........22222222fff222222ff22222222.............
                            ..........22222222ff2222222f222222222.............
                            ..........222222222222222222222222222.............
                            ..........22222222222222ff22222222222.............
                            ..........22222222222222ff2222222222..............
                            ...........2222222222222f22222222222..............
                            ............2222222222f2f2222222222...............
                            .............222222222ff2f2f222222................
                            ..............222222222222f222222.......222.......
                            .....222......22222222222222222222.....2222.......
                            ....22222....22222222222222222222222..22222.......
                            ....222222..2222222222222222222222222222222.......
                            ....222222222222222222223333322222222222222.......
                            ....22222222222222222223333333222222222222........
                            ....22222222222222222333333333322222222222........
                            .....222222222222222333333333333222222222.........
                            ......22222222222222333333333333222222222.........
                            ......22222222222223333333333333222222222.........
                            .......22222222222233333333333332222222...........
                            ........2222222222233333333333332222222...........
                            ........2222222222233333333333322222222...........
                            ........2222222222233333333333322222222...........
                            ........2222222222223333333332222222222...........
                            .........222222222223333333322222222222...........
                            .........222222222222333332222222222222...........
                            .........2222222.2222222.........22222............
                            .........222222...................2222............
                            .........22222....................2222............
            """),
            SpriteKind.player)
        controller.player2.move_sprite(easter_bunny_2)
        scene.camera_follow_sprite(easter_bunny_2)
        tiles.place_on_tile(easter_bunny_2, value3)
        tiles.set_tile_at(value3, assets.tile("""
            transparency16
        """))
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def on_player1_connected():
    global easter_bunny_1
    for value4 in tiles.get_tiles_by_type(assets.tile("""
        myTile2
    """)):
        easter_bunny_1 = sprites.create(assets.image("""
            myImage
        """), SpriteKind.player)
        controller.player1.move_sprite(easter_bunny_1)
        scene.camera_follow_sprite(easter_bunny_1)
        tiles.place_on_tile(easter_bunny_1, value4)
        tiles.set_tile_at(value4, assets.tile("""
            transparency16
        """))
controller.player1.on_event(ControllerEvent.CONNECTED, on_player1_connected)

def on_on_overlap2(sprite4, otherSprite2):
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

easter_bunny_1: Sprite = None
easter_bunny_2: Sprite = None
easter_bunny_3: Sprite = None
easter_bunny_4: Sprite = None
egg: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
"""))
scene.set_background_image(img("""
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
"""))
for value5 in tiles.get_tiles_by_type(assets.tile("""
    myTile
""")):
    egg = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 3 3 3 3 . . . . . . 
                    . . . . . 3 9 9 9 9 3 . . . . . 
                    . . . . 3 9 4 4 4 4 9 3 . . . . 
                    . . . 3 9 4 5 5 5 5 4 9 3 . . . 
                    . . . 3 9 4 5 b b 5 4 9 3 . . . 
                    . . . 3 9 4 5 b b 5 4 9 3 . . . 
                    . . . 3 9 4 5 b b 5 4 9 3 . . . 
                    . . . 3 9 4 5 b b 5 4 9 3 . . . 
                    . . . 3 9 4 5 b b 5 4 9 3 . . . 
                    . . . 3 9 4 5 5 5 5 4 9 3 . . . 
                    . . . . 3 9 4 4 4 4 9 3 . . . . 
                    . . . . . 3 9 9 9 9 3 . . . . . 
                    . . . . . . 3 3 3 3 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
    tiles.place_on_tile(egg, value5)
    tiles.set_tile_at(value5, assets.tile("""
        transparency16
    """))