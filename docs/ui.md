# Basic UI Setup

The initial UI consists of a main menu and an inventory screen. Both scenes live
under `godot/scenes/`.

* **MainMenu.tscn** loads when the game starts and contains placeholder Start and
  Inventory buttons.
* **Inventory.tscn** is a simple Control with an `ItemList` to display player
  items.
* **CharacterStats.tscn** shows basic stats for the selected character.
* **Crafting.tscn** lists available recipes.

All scenes share `assets/ui/theme.tres` for consistent styling.

Open the project in the Godot editor to modify layouts or connect signals.
