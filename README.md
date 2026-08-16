# 🎨 Pellizzola Brothers (textures & sprites)

**Asset library for the Pellizzola Brothers platformer game and level editor.** Contains all block sprites, enemy sprites, interactive items, character designs, backdrops, UI elements, and icons used across the game and editor.

This is a **Git submodule** maintained separately and imported by both the [level editor](https://github.com/pellizzola-brothers/studio) and the [game engine](https://github.com/pellizzola-brothers/game). <br>
Keep this submodule's asset contract in sync with both consumers.

![Assets](https://img.shields.io/badge/Asset%20Library-PNG%20Sprites-important)
![Organization](https://img.shields.io/badge/Organized-By%20Category-blueviolet)
![Format](https://img.shields.io/badge/Format-PNG%20%2B%20Spritesheets-9cf)
![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red)

## Table of Contents

- [Directory Structure](#directory-structure)
- [Asset Inventory](#asset-inventory)
  - [Blocks (Structural)](#blocks-structural)
  - [Interactives (Collectibles)](#interactives-collectibles)
  - [Enemies](#enemies)
  - [Characters](#characters)
  - [Backdrops](#backdrops)
  - [UI & Icons](#ui--icons)
- [Naming Conventions](#naming-conventions)
- [Integration with Game & Editor](#integration-with-game--editor)
- [Adding New Assets](#adding-new-assets)
- [Asset Format Specifications](#asset-format-specifications)
- [Known Limitations](#known-limitations)
- [Contributing](#contributing)
- [License](#license)

## Directory Structure

```
textures/
├── blocks/              Block/tile sprites (structural elements)
├── Interactives/        Collectibles (pizza, coins, soda, stars)
├── enemies/             Enemy & hazard sprites
├── characters/          Player & NPC sprites
├── backdrops/           Scene background images
├── icons/               UI icons & buttons
├── ui/                  UI panels, HUD elements
├── block_sheet.png      Spritesheet: all blocks in column order (CRITICAL)
└── README.md            This file
```

## Asset Inventory

### Blocks (Structural)

**Location:** `blocks/` directory  
**Spritesheet:** `block_sheet.png` (critical — column order is the game contract)

Structural tiles placed by the level editor and rendered by the game. The `block_sheet.png` file is a **spritesheet where the column order defines tile IDs**:

| Tile ID | Name | File | Notes |
|---------|------|------|-------|
| 1 | START (Green Flag) | `start.png` | Unique spawn point per level |
| 4 | END (Red Flag) | `end.png` | Unique goal per level |
| 2 | Brick | `brick.png` | Basic solid block |
| 3 | Excla-Block | `excla_block.png` | Destructible block |
| 5 | Arrow Sign | `arrow_sign.png` | Passthrough directional sign |
| 6 | Bronze Block | `bronze.png` | Metallic solid block |
| 7 | Cement Block | `cement.png` | Heavy solid block |
| 8 | Diamond Block | `diamond.png` | Shiny decorative block |
| 9 | Esponja (Sponge) | `esponja.png` | Soft block |
| 10 | Floor | `floor.png` | Horizontal surface |
| 11 | Frozen Excla-Block | `frozen_excla_block.png` | Ice variant |
| 12 | Frozen Floor | `frozen_floor.png` | Ice variant |
| 13 | Gold Block | `gold.png` | Precious block |
| 14 | Ice Excla-Block | `ice_excla_block.png` | Icy destructible |
| 15 | Ice Floor | `ice_floor.png` | Icy surface |
| 16 | Note Block | `note_block.png` | Musical/bouncy block |
| 17 | Sand Block | `sand.png` | Desert theme |
| 18 | Silver Block | `silver.png` | Metallic solid block |
| 19 | Cloud Block | `cloud.png` | Sky theme block |

**⚠️ CRITICAL:** The `block_sheet.png` spritesheet column order **is the contract** between this asset library, the level editor, and the game. Changing the column order requires coordinating updates to:
- `studio/script.js` — `BLOCK_REGISTRY`, `SPRITE_PATHS`
- `game/blocks.c` and `game/blocks.h` — tile ID mappings

### Interactives (Collectibles)

**Location:** `Interactives/` directory (note the capital I)

Passthrough collectible items that players can pick up:

| Tile ID | Name | File | Effect |
|---------|------|------|--------|
| 43 | Pizza | `pizza.png` | Health/points |
| 44 | Pellizzola Coin | `coin.png` | Currency/collectible |
| 45 | Soda Can | `soda.png` | Stamina/boost |
| 46 | Star | `star.png` | Rare collectible |

### Enemies

**Location:** `enemies/` directory

Hazardous entities that damage the player (Tile IDs ≥ 50):

| Tile ID | Name | File | Behavior |
|---------|------|------|----------|
| 50 | Chapeleira | `chapeleira.png` | Floating witch-like enemy |
| 51 | Abú | `abu.png` | Jumping monkey enemy |
| 52 | Gombacrack | `gombacrack.png` | Fungal enemy |
| 53 | Pranta | `pranta.png` | Plant-like enemy |
| 54 | Pinguim | `pinguim.png` | Sliding penguin enemy |
| 55 | Bullet | `bullet.png` | Projectile hazard |

### Characters

**Location:** `characters/` directory

Playable and NPC character sprites (idle, walk, jump, etc.). Used by the game engine during play.

### Backdrops

**Location:** `backdrops/` directory

Full-screen or full-height scene backgrounds. Each backdrop is referenced by a string ID in level data:

| ID | File | Theme |
|----|------|-------|
| `dark` | `dark.png` | Default dark background |
| `sky` | `sky.png` | Blue sky theme |
| *(others)* | *(as added)* | *(theme-specific)* |

Backdrops are **per-scene** — each of the 9 scenes in a level can have a different backdrop.

### UI & Icons

**Location:** `icons/` and `ui/` directories

- `icons/` — Small UI icons (buttons, status indicators, category markers)
- `ui/` — Larger UI elements (panels, HUD frames, menus)

Used by both the level editor and the game's front-end UI.

---

## Naming Conventions

Follow these rules when adding new assets:

### File Naming
- **Lowercase with underscores**: `arrow_sign.png`, `excla_block.png`
- **No spaces or special chars** (except underscore)
- **Descriptive**: `frozen_floor.png` is clear; `ff.png` is not
- **Variant suffix**: `excla_block.png`, `frozen_excla_block.png`, `ice_excla_block.png`

### Directory Organization
- **Category folders** match the editor's `BLOCK_REGISTRY` categories:
  - `blocks/` — structural tiles
  - `Interactives/` — collectibles (keep the capital I for consistency)
  - `enemies/` — hazards and enemies
  - `characters/` — player and NPCs
  - `backdrops/` — scenes
  - `icons/`, `ui/` — interface elements

### Spritesheet Column Order
- When updating `block_sheet.png`, maintain **alphabetical order by category** (as documented in the Asset Inventory above)
- **Never insert a column in the middle** — always append new blocks at the end or rebuild the entire sheet
- **Document the change** in a commit message referencing both `studio/script.js` and `game/blocks.{c,h}`

---

## Integration with Game & Editor

### Level Editor (`studio/script.js`)

The editor loads sprites at startup via `loadSprites()`:

1. **Attempts to load** PNG files from this directory
2. **Falls back to colored rectangles** if an image fails to load
3. **References `BLOCK_REGISTRY`** to map tile IDs to file paths in `SPRITE_PATHS`

When you add a new block sprite:
- Add the file to the appropriate folder in this directory
- Update `studio/script.js`:
  - Add entry to `BLOCK_REGISTRY` (id, name, category, description)
  - Add path to `SPRITE_PATHS` (id → folder/filename)
  - Add fallback color to `TILE_COLORS`

### Game Engine (`game/`)

The game compiles block metadata from `blocks.c`/`blocks.h`, which must match this submodule's tile IDs. When adding a block:
- Add the sprite PNG to this submodule
- Update the game's tile ID enum and asset loader
- **Coordinate the update across both repos** — they must agree on tile IDs

---

## Adding New Assets

### Adding a New Block Tile

1. **Create the PNG sprite** (recommended: 32×32 px, transparent background)
2. **Place it in `blocks/`** with a descriptive lowercase name (`new_block.png`)
3. **Update `block_sheet.png`**:
   - Open in an image editor (Photoshop, GIMP, Aseprite)
   - Append the new sprite as a new column (maintain row height)
   - Save as PNG (8-bit or 32-bit with transparency)
4. **Assign a tile ID**:
   - If it's a structural block, use the next available ID in the 2–19 range
   - If it's a collectible, use 43–46
   - If it's an enemy, use ≥ 50
5. **Update `studio/script.js`**:
   ```javascript
   // In BLOCK_REGISTRY:
   { id: 20, name: "New Block", category: "estrutura", description: "...", ... }
   
   // In SPRITE_PATHS:
   20: "blocks/new_block.png",
   
   // In TILE_COLORS:
   20: "#ff00ff", // fallback color
   ```
6. **Update `game/blocks.c` and `game/blocks.h`** to include the new tile ID
7. **Test**:
   - Open the level editor (`npm start` in `studio/`)
   - Verify the new block appears in the palette
   - Verify the sprite loads (not just a colored rectangle)
   - Place a few on the grid, save, and reload
   - Test in the game engine

### Adding a New Enemy or Collectible

Follow the same process as a new block, but:
- Place the sprite in `enemies/` or `Interactives/`
- Use the reserved ID ranges (43–46 for collectibles, ≥ 50 for enemies)
- Update both `BLOCK_REGISTRY` and the game's entity system

### Adding a New Backdrop

1. **Create a full-screen PNG** (recommended: 1080×720 px or higher, landscape)
2. **Place it in `backdrops/`** with a descriptive lowercase name (`new_sky.png`)
3. **Register it in `studio/script.js`**:
   - Add an entry to the `BACKGROUNDS` constant (string ID, e.g. `"new_sky"`)
   - Add the path to `SPRITE_PATHS`
4. **Test**: Open the level editor, create a new scene, and verify the backdrop appears in the dropdown

---

## Asset Format Specifications

### Sprite Format
- **Format:** PNG with transparency (RGBA)
- **Color depth:** 8-bit indexed or 32-bit full color (transparency channel required)
- **Dimensions:** 32×32 px for blocks/enemies, 48×48 px for characters (use consistent sizes within categories)
- **Compression:** PNG, lossless — no JPG
- **Background:** Transparent (0 alpha for empty areas)

### Spritesheet Format (`block_sheet.png`)
- **Format:** PNG with transparency
- **Layout:** Single row or grid, depending on total blocks
- **Column width:** 32 px per block
- **Row height:** 32 px
- **Spacing:** 0 px (no gaps between columns)
- **Order:** Matches the tile ID order documented above

### Backdrop Format
- **Format:** PNG (transparency optional)
- **Dimensions:** Landscape, at least 1080×720 px (2× recommended for HiDPI)
- **Aspect ratio:** 16:9 or 3:2
- **Compression:** Lossless PNG

---

## Known Limitations

- **Spritesheet brittleness:** Inserting a column in the middle of `block_sheet.png` shifts all subsequent tile IDs. Always append or rebuild the entire sheet.
- **No automatic detection:** Adding a file to this directory doesn't automatically register it in the editor or game — both consumers require explicit updates to `BLOCK_REGISTRY` and tile ID mappings.
- **Single character tileset:** The game uses a fixed spritesheet for player and NPC animations — replacing character sprites requires coordination with the game engine.

---

## Contributing

Contributions welcome! When adding or updating assets:

1. **Sprite quality:**
   - Use consistent pixel art style across the category
   - Test sprites at 2× and 0.5× scale to verify readability
   - Provide clear, opaque backgrounds (or transparent where appropriate)

2. **Documentation:**
   - Update this README's asset inventory if adding a new category or tile ID
   - Include a commit message explaining the asset's purpose and tile ID
   - Reference related updates in `studio/script.js` or `game/blocks.{c,h}`

3. **Testing:**
   - Verify new sprites load in the level editor (fallback to colored rectangle if missing)
   - Test placement and visual alignment in the game
   - Confirm round-trip: place in editor → save → open in editor → play in game

4. **Coordination:**
   - If changing tile IDs or the spritesheet, update **both** `studio/` and `game/` subprojects
   - Open issues or PRs to both repos if coordinating larger asset overhauls

---

## License

Except where otherwise noted, all assets in this repository are licensed under **All Rights Reserved**. Individual asset licensing may vary — see the `LICENSE` file at the repository root for details.

Sprites are property of the Pellizzola Brothers project and may not be used without permission.

---

**Back to top:** See the [main studio README](https://github.com/pellizzola-brothers/studio/README.md) or [website README](https://github.com/pellizzola-brothers/website/README.md) for project overview and setup instructions.
