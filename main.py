import json
import pygame
screen = pygame.display.set_mode((620, 620))
wall = pygame.image.load("wall2.png")
menu = pygame.image.load("menu.png")
slct = pygame.image.load("slct2.png")
mode = "none"

def renderMap():
    screen.fill((0x40, 0x40, 0x40))
    for i in d["map"]["cells"]:
        if (i["isWall"]):
            screen.blit(wall, (i["row"] * 20, i["column"] * 20))
        if (i["isInFirstRespawnZone"]):
            pygame.draw.rect(screen, (0x00, 0x00, 0xFF, 0x7F), (i["row"] * 20, i["column"] * 20, 20, 20))
        if (i["isInSecondRespawnZone"]):
            pygame.draw.rect(screen, (0xFF, 0x00, 0x00, 0x7F), (i["row"] * 20, i["column"] * 20, 20, 20))
        if (i["isInFirstRespawnZone"] and i["isInSecondRespawnZone"]):
            pygame.draw.rect(screen, (0xFF, 0x00, 0x7F), (i["row"] * 20, i["column"] * 20, 20, 20))
        if (i["isInObjectiveZone"]):
            pygame.draw.rect(screen, (0x00, 0xFF, 0x00), (i["row"] * 20, i["column"] * 20, 20, 20))


d = {"map" : {"cells" : [[0 for j in range(31)] for i in range(31)] }}
with open ("data.map") as json_data:
    d = json.load(json_data)

sx = sy = 0
while True:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if mode == "none":
                    mode = "view"
            if e.key == pygame.K_RETURN:
                if mode == "none":
                    mode = "edit"
                    sx = sy = 0;
            if e.key == pygame.K_ESCAPE:
                    mode = "none"
            if e.key == pygame.K_UP:
                if (sy > 0):
                    sy -= 1
            if e.key == pygame.K_DOWN:
                if (sy < 30):
                    sy += 1
            if e.key == pygame.K_LEFT:
                if (sx > 0):
                    sx -= 1
            if e.key == pygame.K_RIGHT:
                if (sx < 30):
                    sx += 1
            if mode == "edit":
                if (e.key == pygame.K_1):
                    d["map"]["cells"][sx * 31 + sy]["isWall"] = not(
                        d["map"]["cells"][sx * 31 + sy]["isWall"]);

                if (e.key == pygame.K_2):
                    d["map"]["cells"][sx * 31 + sy]["isInFirstRespawnZone"] = not(
                        d["map"]["cells"][sx * 31 + sy]["isInFirstRespawnZone"]);

                if (e.key == pygame.K_3):
                    d["map"]["cells"][sx * 31 + sy]["isInSecondRespawnZone"] = not(
                        d["map"]["cells"][sx * 31 + sy]["isInSecondRespawnZone"]);
                if (e.key == pygame.K_4):
                    d["map"]["cells"][sx * 31 + sy]["isInObjectiveZone"] = not(
                    d["map"]["cells"][sx * 31 + sy]["isInObjectiveZone"]);

                if (e.key == pygame.K_s):
                    with open('data.map', 'w') as outfile:
                        json.dump(d, outfile)
                    print ("saved")


    if (mode == "none"):
        screen.blit(menu, (0, 0))

    if (mode == "edit"):
        renderMap()
        screen.blit(slct, (sx * 20, sy * 20))

    if (mode == "view"):
        renderMap()

    pygame.display.update()
