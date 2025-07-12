class_name NPC
extends Node2D

var name: String = ""
var health: int = 100
var hunger: int = 100
var thirst: int = 100

func tick(hunger_rate: int = 1, thirst_rate: int = 1):
    hunger = max(0, hunger - hunger_rate)
    thirst = max(0, thirst - thirst_rate)
