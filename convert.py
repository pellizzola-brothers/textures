# Helper utility to transform individual sprites into spritesheets.

from PIL import Image
from os import walk, listdir, path

SHEETS = "sheets/"

player = ["characters/pellizzola/"]
blocks = ["blocks/"]
entities = ["enemies/", "interactives/", "characters/plant/"]


def images(folder):
    found = []
    for root, dirs, files in sorted(walk(folder)):
        for file in sorted(files):
            if file.endswith(".png"):
                if "erick" in path.join(root, file): continue
                found.append(Image.open(path.join(root, file)).convert("RGBA"))
    return found


def rows_of(folder):
    entries = [entry for entry in listdir(folder) if not entry.startswith(".")]
    if entries and all(path.isdir(path.join(folder, entry)) for entry in entries):
        return [images(path.join(folder, entry)) for entry in sorted(entries)]
    return [images(folder)]


def sheet(folders, name):
    rows = []
    for folder in folders:
        rows += rows_of(folder)
    rows = [row for row in rows if row]

    width = max(sum(image.width for image in row) for row in rows)
    height = sum(max(image.height for image in row) for row in rows)
    out = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    y = 0
    for row in rows:
        x = 0
        for image in row:
            out.paste(image, (x, y), image)
            x += image.width
        y += max(image.height for image in row)

    out.save(path.join(SHEETS, name))


if __name__ == "__main__":
    sheet(player, "player.png")
    sheet(entities, "entities.png")
    sheet(blocks, "blocks.png")
