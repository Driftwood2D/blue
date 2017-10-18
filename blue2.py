def lights():
    if not _["inventory"]["blue_pearl"]["active"]:
        a = Driftwood.light.insert("lightmap_circle1.png", 2, 80, 20, 48, 48, "4444FFEE")
        b = Driftwood.light.insert("lightmap_circle1.png", 2, 20, 60, 48, 48, "4444FFEE")
        c = Driftwood.light.insert("lightmap_circle1.png", 2, 140, 60, 48, 48, "4444FFEE")
        _["lighting"].flicker(a, 0, 0, 64, 16)
        _["lighting"].flicker(b, 0, 0, 64, 16)
        _["lighting"].flicker(c, 0, 0, 64, 16)

    else:
        Driftwood.script["rumble.py"].constant_rumble(30, 2)
        Driftwood.light.reset()
        a = Driftwood.light.insert("lightmap_circle1.png", 2, 80, 56, 160, 160, "FFFFFFFF", blend=False)
        c = Driftwood.light.insert("lightmap_circle1.png", 3, 80, 56, 100, 100, "8888FFFF", blend=False)
        d = Driftwood.light.insert("lightmap_circle1.png", 3, 80, 56, 200, 200, "FF8888FF", blend=False)
        b = Driftwood.light.insert("lightmap_circle1.png", 3, 80, 56, 128, 100, "4444FFEE", blend=True)
        _["lighting"].flicker(b, 0, 0, 40, 8)
        _["lighting"].flicker(a, 0, 0, 120, 6)
        Driftwood.area.tilemap.layers[2].tile(4, 3).properties["on_tile"] = "blue2.py,leave_world"
        Driftwood.area.tilemap.layers[2].tile(4, 3).properties["on_tile"] = "blue2.py,leave_world"


def activate_pearl():
    if _["inventory"].has("blue_pearl") and not _["inventory"]["blue_pearl"]["active"]:
        _["inventory"]["blue_pearl"]["active"] = "true"
        _["inventory"].save()
        lights()


def leave_world():
    Driftwood.entity.player.teleport(1, 1, 6, area="ring7.json")
