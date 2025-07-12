extends Node2D

func _ready():
    print("Game initialized")
    var menu_scene = preload("res://scenes/MainMenu.tscn")
    var menu = menu_scene.instantiate()
    add_child(menu)
