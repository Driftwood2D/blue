def open_door():
    # TODO: This needs to be in the stdlib.
    Driftwood.area.tilemap.layers[2].tile(4, 0).nowalk = None
    Driftwood.area.tilemap.layers[2].tile(4, 0).setgid(27)


def open_door2():
    Driftwood.area.tilemap.layers[2].tile(2, 0).nowalk = None
    Driftwood.area.tilemap.layers[2].tile(2, 0).setgid(27)


def get_pearl():
    if not _["inventory"].has("blue_pearl"):
        Driftwood.area.tilemap.layers[2].tile(5, 3).nowalk = None
        Driftwood.area.tilemap.layers[1].tile(5, 3).setgid(0)
        _["inventory"].get("blue_pearl", 1)
        _["inventory"].save()
        if "blue_pearl_light" in Driftwood.vars and Driftwood.vars["blue_pearl_light"]:
            Driftwood.light.kill(Driftwood.vars["blue_pearl_light"])
