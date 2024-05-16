#imports

from PIL import Image

def asciiConvert(image, type, saveas, scale):
    #image: image name (String)
    #type: image type (png, jpeg, etc.) (must match whats in image name) (String)
    #saveas: new ascii image name (String)
    #scale: image scale (int)

    scale = int(scale)
    
    #open and get dimensions of image
    img = Image.open(image)
    w, h = img.size

    #downscale image
    img.resize((w//scale, h//scale)).save("resized.%s" % type)

    #open and get dimensions of new image
    img = Image.open("resized.%s" % type)
    w, h = img.size

    #setting grid
    grid = []
    for i in range(h):
        grid.append(["X"] * w)
    
    #load image pixels
    pixels = img.load()

    #testing for brightness and converting (sum of pixels = brithness)
    for y in range(h):
        for x in range(w):
            if sum(pixels[x, y]) == 0:
                grid[y][x] == "#"
            elif sum(pixels[x,y]) in range(1,100):
                grid[y][x] = "X"
            elif sum(pixels[x,y]) in range(100,200):
                grid[y][x] = "%"
            elif sum(pixels[x,y]) in range(200,300):
                grid[y][x] = "&"
            elif sum(pixels[x,y]) in range(300,400):
                grid[y][x] = "*"
            elif sum(pixels[x,y]) in range(400,500):
                grid[y][x] = "+"
            elif sum(pixels[x,y]) in range(500,600):
                grid[y][x] = "/"
            elif sum(pixels[x,y]) in range(600,700):
                grid[y][x] = "("
            elif sum(pixels[x,y]) in range(700,750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "

    #writting to file
    ascii = open(saveas, "w")

    for row in grid:
        ascii.write("".join(row)+"\n")
    
    ascii.close()