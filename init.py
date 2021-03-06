def init():
    """Called on engine start.
    """
    # Set the logical resolution of the window.
    Driftwood.window.resize(120, 120)

    # Initialize the inventory.
    inventory = Driftwood.script["Folkdance/inventory.py"].InventoryManager()
    if not inventory.restore("inventory"):
        inventory.load("blue_pearl.item.json")
    _["inventory"] = inventory

    # Initialize special effects.
    viewport = Driftwood.script["Stageshow/viewport.py"].ViewportFX()
    lighting = Driftwood.script["Stageshow/lighting.py"].LightingFX()
    _["viewport"] = viewport
    _["lighting"] = lighting

    # Load the area.
    Driftwood.area.focus("blue1.json")

    # Play placeholder music.
    Driftwood.audio.play_music("A_Travellers_Tale.oga", loop=None)

    # Insert the player entity.
    player = Driftwood.entity.insert("player.json", layer=1, x=4, y=8)
