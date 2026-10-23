# 🎨 Pellizzola Brothers (textures & sprites)

**Asset library for the Pellizzola Brothers platformer game and level editor.** Contains all block sprites, enemy sprites, interactive items, character designs, backdrops, UI elements used across the game and editor.

This is a **Git submodule** maintained separately and imported by both the [level editor](https://github.com/pellizzola-brothers/studio) and the [game engine](https://github.com/pellizzola-brothers/game). <br>
Keep this submodule's asset contract in sync with both consumers.

![Assets](https://img.shields.io/badge/Asset%20Library-PNG%20Sprites-important)
![Organization](https://img.shields.io/badge/Organized-By%20Category-blueviolet)
![Format](https://img.shields.io/badge/Format-PNG%20%2B%20Spritesheets-9cf)
![License](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)

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
├── blocks/              Block sprites, 00.png to 11.png, in column order
├── enemies/             Enemy & hazard sprites
├── interactives/        Collectibles (pizza, coin, energy drink)
├── characters/          Player & NPC sprites
├── backdrops/           Scene background images
├── ui/                  UI panels, HUD elements
├── sheets/              Spritesheets the game reads: blocks, entities, player
└── README.md            This file
```

## Asset Inventory

### Blocks (Structural)

**Location:** `blocks/` directory
**Spritesheet:** `sheets/blocks.png` (critical — column order is the contract)

Structural tiles placed by the level editor and rendered by the game. `blocks/` holds one PNG per block, numbered in column order. `sheets/blocks.png` packs them left to right into one 32 px row, and the column order defines block IDs. An ID is the block's column plus one, because `000` is air:

| Block ID | Name | File | Notes |
|----------|------|------|-------|
| 1 | Brick | `blocks/00.png` | Basic solid block |
| 2 | Floor Block | `blocks/01.png` | Horizontal surface |
| 3 | Ice Floor Block | `blocks/02.png` | Icy surface |
| 4 | Exclamation Block | `blocks/03.png` | Destructible block |
| 5 | Arrow Sign | `blocks/04.png` | Passthrough directional sign |
| 6 | Sponge | `blocks/05.png` | Soft block |
| 7 | Gravel | `blocks/06.png` | Heavy solid block |
| 8 | Frozen Floor Block | `blocks/07.png` | Ice variant |
| 9 | Ice Exclamation Block | `blocks/08.png` | Icy destructible |
| 10 | Note Block | `blocks/09.png` | Musical/bouncy block |
| 11 | Sand | `blocks/10.png` | Desert theme |
| 12 | End Sign | `blocks/11.png` | Unique goal block, one per level |

The start, diamond, silver and cloud blocks were removed in the restructure, and the lucky, gold and bronze blocks were removed before it.

**⚠️ CRITICAL:** The column order of `sheets/blocks.png` **is the contract** between this asset library, the level editor and the game. Changing it requires coordinating updates to:
- `studio/catalog.js` — `BLOCKS`, `ENDTILE`
- `game/blocks.c` and `game/blocks.h` — block ID mappings

### Interactives (Collectibles)

**Location:** `interactives/` directory

Collectibles are entities, not block tiles: they are dragged into place like an enemy and each runs an `_item` script. Each one is a directory of frames, `00.png` being the idle one:

| Definition | Folder | Script | Effect |
|------------|--------|--------|--------|
| `pizza` | `interactives/pizza/` | `pizza_item` | Health/points |
| `coin` | `interactives/coin/` | `coin_item` | Currency/collectible |
| `soda` | `interactives/energy_drink/` | `soda_item` | Stamina/boost |

Levels written before the change stored these as block ids 43–45, and the studio converts them on open. Those ids stay reserved and must not be given to a block. The star (46) was removed with its sprite.

### Enemies

**Location:** `enemies/` directory

Hazardous entities that damage the player, each a directory of frames. Like the interactives, they are named by definition, not by number:

| Definition | Folder | Script | Behavior |
|------------|--------|--------|----------|
| `chapeleira` | `enemies/chapeleira/` | `chapeleira_ai` | Floating witch-like enemy |
| `abu` | `enemies/erick/` | `abu_ai` | Jumping monkey enemy |
| `pranta` | `enemies/pranta/` | `pranta_ai` | Plant-like enemy |
| `pinguim` | `enemies/tux/` | `pinguim_ai` | Sliding penguin enemy |
| `bullet` | `enemies/bullet/` | `bullet_ai` | Projectile hazard |

The gombacrack sprites were removed from the library.

### Characters

**Location:** `characters/` directory

Playable and NPC character sprites, each a directory of frames. `characters/pellizzola/` is the player (`sheets/player.png`). Used by the game engine during play.

### Backdrops

**Location:** `backdrops/` directory

Full-screen or full-height scene backgrounds. The level schema allows only three presets, `foo`, `bar` and `baz`, which `BGS` in `studio/catalog.js` maps onto the art:

| Preset | File | Notes |
|--------|------|-------|
| `foo`, `bar`, `baz` | `backdrops/00.png` | All three share the one backdrop the library ships |

The schema gives a level one backdrop for all its scenes. Per-scene backdrops need a schema change first.

### UI & Icons

**Location:** `ui/` directory

Larger UI elements (menus, win and lose scenes). Used by the game's front-end UI.

---

## Naming Conventions

Follow these rules when adding new assets:

### File Naming
- **Lowercase with underscores**: `energy_drink/`, `main_menu.png`
- **No spaces or special chars** (except underscore)
- **Descriptive**: `frozen_floor.png` is clear; `ff.png` is not
- **Frames**: `00.png`, `01.png`, … in walk order, so `00.png` is the idle frame

### Directory Organization
- **Category folders:**
  - `blocks/` — structural tiles, numbered in column order
  - `interactives/` — collectibles
  - `enemies/` — hazards and enemies
  - `characters/` — player and NPCs
  - `backdrops/` — scenes
  - `ui/` — interface elements

### Spritesheet Column Order
- Block files are numbered `NN.png` in column order, so a new block takes the next free number
- **Never insert a column in the middle** — always append new blocks at the end or rebuild the entire sheet
- **Document the change** in a commit message referencing `studio/catalog.js` and `game/blocks.{c,h}`

---

## Integration with Game & Editor

### Level Editor (`studio/catalog.js`)

The editor reads `BLOCKS` in `studio/catalog.js` to map block IDs to the files in `blocks/`, and draws each block from its own file. On startup it checks that `sheets/blocks.png` is one row of 12 columns, and warns if it is not as wide as `BLOCKS` is long.

When you add a new block:
- Add the file to `blocks/` and its column to `sheets/blocks.png`
- Add an entry to `BLOCKS` in `studio/catalog.js` (id, name, file)
- Update `ENDTILE` only if the new block is the goal

### Game Engine (`game/`)

The game compiles block metadata from `blocks.c`/`blocks.h`, which must match this submodule's block IDs. When adding a block:
- Add the sprite PNG to this submodule
- Update the game's block ID enum and asset loader
- **Coordinate the update across both repos** — they must agree on block IDs

---

## Adding New Assets

### Adding a New Block Tile

1. **Create the PNG sprite** (recommended: 32×32 px, transparent background)
2. **Place it in `blocks/`** with the next number (`12.png`)
3. **Update `sheets/blocks.png`**:
   - Open in an image editor (Photoshop, GIMP, Aseprite)
   - Append the new sprite as a new column (maintain row height)
   - Save as PNG (8-bit or 32-bit with transparency)
4. **Assign a block ID**: the number plus one (`12.png` is `13`)
5. **Update `studio/catalog.js`**:
   ```javascript
   // In BLOCKS:
   {id: 13, name: 'new block', file: 'blocks/12.png'},
   ```
6. **Update `game/blocks.c` and `game/blocks.h`** to include the new block ID
7. **Test**:
   - Open the level editor (`npm start` in `studio/`)
   - Verify the new block appears in the palette
   - Verify the sprite loads (not just a colored rectangle)
   - Place a few on the grid, save, and reload
   - Test in the game engine

### Adding a New Enemy or Collectible

1. **Create a folder** in `enemies/` or `interactives/` with its frames as `00.png`, `01.png`, …
2. **Rebuild `sheets/entities.png`** with `convert.py`. It packs folders in alphabetical order, so a new folder shifts the rows after it. Then run `npm run map_animations` in `studio/`.
3. **Update `ENTS` or `ITEMS`** in `studio/catalog.js` (id, script, file, sheet, row, frame).
4. **Update the game's entity table.** The script name must match the game's: `*_ai` for enemies, `*_item` for collectibles.

### Adding a New Backdrop

The level schema allows only the presets `foo`, `bar` and `baz`, so a new backdrop is a schema change. Coordinate it across the game, the website and the studio first, then:

1. **Place the PNG** in `backdrops/` (see Backdrop Format)
2. **Map the new preset** to it in `BGS` in `studio/catalog.js`

---

---

## Asset Format Specifications

### Sprite Format
- **Format:** PNG with transparency (RGBA)
- **Color depth:** 8-bit indexed or 32-bit full color (transparency channel required)
- **Dimensions:** 32×32 px for blocks and most entities (`erick`'s frames are 64×64). Each sheet row's `frame` in `studio/catalog.js` gives its size.
- **Compression:** PNG, lossless — no JPG
- **Background:** Transparent (0 alpha for empty areas)

### Spritesheet Format (`sheets/blocks.png`)
- **Format:** PNG with transparency
- **Layout:** Single row, one column per block
- **Column width:** 32 px per block
- **Row height:** 32 px
- **Spacing:** 0 px (no gaps between columns)
- **Order:** Column N holds `blocks/(N-1).png`, so block ID = column + 1

### Backdrop Format
- **Format:** PNG (transparency optional)
- **Dimensions:** Landscape, at least 1080×720 px (2× recommended for HiDPI)
- **Aspect ratio:** 16:9 or 3:2
- **Compression:** Lossless PNG

---

## Known Limitations

- **Spritesheet brittleness:** Inserting a column in the middle of `sheets/blocks.png` shifts all subsequent block IDs. Always append or rebuild the entire sheet.
- **No automatic detection:** Adding a file to this directory doesn't automatically register it in the editor or game — both consumers require explicit updates to `studio/catalog.js` and block ID mappings.
- **Single character tileset:** The game uses a fixed spritesheet for player and NPC animations — replacing character sprites requires coordination with the game engine.

---

## Contributing

Contributions welcome! When adding or updating assets:

1. **Sprite quality:**
   - Use consistent pixel art style across the category
   - Test sprites at 2× and 0.5× scale to verify readability
   - Provide clear, opaque backgrounds (or transparent where appropriate)

2. **Documentation:**
   - Update this README's asset inventory if adding a new category or block ID
   - Include a commit message explaining the asset's purpose and block ID
   - Reference related updates in `studio/catalog.js` or `game/blocks.{c,h}`

3. **Testing:**
   - Verify new sprites load in the level editor (fallback to colored rectangle if missing)
   - Test placement and visual alignment in the game
   - Confirm round-trip: place in editor → save → open in editor → play in game

4. **Coordination:**
   - If changing block IDs or the spritesheet, update **both** `studio/` and `game/` subprojects
   - Open issues or PRs to both repos if coordinating larger asset overhauls

---

## License

Except where otherwise noted, all assets in this repository are licensed under **All Rights Reserved**. Individual asset licensing may vary — see the `LICENSE` file at the repository root for details.

Sprites are property of the Pellizzola Brothers project and may not be used without permission.

---

**Back to top:** See the [main studio README](https://github.com/pellizzola-brothers/studio/README.md) or [website README](https://github.com/pellizzola-brothers/website/README.md) for project overview and setup instructions.
