from PIL import Image
from os import walk, path

SHEETS = "sheets/"

player = ["characters/pellizzola/"]
blocks = ["blocks/"]
entities = ["enemies/", "interactives/", "characters/plant/"]


def sheet(folders, name):
    rows = []
    for folder in folders:
        for root, dirs, files in sorted(walk(folder)):
            row = [Image.open(path.join(root, file)).convert("RGBA") for file in sorted(files) if file.endswith(".png")]
            if row:
                rows.append(row)

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
