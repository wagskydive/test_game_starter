# Basic UI Setup

This project now includes a minimal Godot 4 scene setup to serve as the starting point for UI work.

## Scenes

- `MainMenu.tscn` provides a simple menu with **Start Game**, **Inventory**, and **Quit** buttons.
- `Inventory.tscn` shows a placeholder panel for displaying inventory items.

Both scenes live under the `godot/scenes/` directory. The project configuration is stored in `godot/project.godot` with `MainMenu.tscn` set as the main scene.

## Manual Test Steps

1. Open the Godot editor and choose `godot/project.godot`.
2. Run the project. The main menu should display three buttons.
3. Open `Inventory.tscn` in the editor to verify the inventory panel layout.

Automated tests are not included because Godot's test framework is not available in this environment. The steps above can be used to manually confirm the UI loads correctly.
