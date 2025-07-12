# Development Planning

This document tracks feature milestones and planned tasks to help coordinate development. Refer to `tickets.md` for issue details and `design.md` for overall vision.

## Completed Features

- [x] Project setup and folder structure
- [x] Workflow guidelines in `AGENTS.md`
- [x] World generation prototype
- [x] Item and inventory system
- [x] Basic NPC class with movement
- [x] Player class with inventory
- [x] Map handling and pathfinding
- [x] Crafting system
- [x] Save and load functionality
- [x] Command line seed option
- [x] Logging utility
- [x] Combat helpers
- [x] NPC needs and personality traits
- [x] AI behaviors and story anchors
- [x] Modding support and asset generation
- [x] Optional LLM integration

## Roadmap and Milestones

### Step 3 - Godot migration
- [x] Create a Godot 4 project skeleton with scenes and folder structure
- [x] Port existing Python modules to GDScript or integrate via GDExtension
- [x] Hook up world generation, NPC, item and crafting systems in Godot
- [x] Configure automated tests using Godot's testing framework
- [x] Make an install and build guide for the end user


### Step 4 – Visuals and UI
- [x] Visual assets are downloaded at runtime.
- [ ] environment: https://kenney.nl/media/pages/assets/tiny-town/5e46f9e551-1735736916/kenney_tiny-town.zip
- [ ] characters: https://kenney.nl/media/pages/assets/roguelike-characters/dbeea49dc8-1729196490/kenney_roguelike-characters.zip
- [ ] ui: https://kenney.nl/media/pages/assets/ui-pack-rpg-expansion/885ad5ccc0-1677661824/kenney_ui-pack-rpg-expansion.zip
- [ ] Create a system for the characters using the assets: https://kenney.nl/assets/roguelike-characters
- [ ] Map the tilset from: https://kenney.nl/assets/tiny-town to our map generator
- [ ] Art palette and layered sprites
- [ ] UI style pass and additional screens
- [ ] NPC animation states

### Step 5 – Story and Events
- [ ] Procedural quest generator
- [ ] Expanded event system

### Step 6 – Advanced Systems
- [ ] Faction goals and group AI
- [ ] Offline LLM integration
- [ ] Weather and seasons
- [ ] Trading and economy
- [ ] NPC families and relationships
- [ ] Nested containers and volume limits
- [ ] NPC health extensions
- [ ] Social status and impressiveness
- [ ] Crafting stations
- [ ] Blueprints and skill requirements
- [ ] Reinforcement learning NPCs
- [ ] Advanced pathfinding
- [ ] NPC daily schedules
- [ ] Day/night cycle and energy
- [ ] Documentation diagrams
- [ ] Settlements and ruins generation
- [ ] Destructible tiles and tile grouping
- [ ] Expanded item definitions
- [ ] Equipment slots

Use the checkboxes to monitor progress as features are completed.
