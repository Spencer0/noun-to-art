from PIL import Image
import wikipedia

ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
ASCII_CHARS = ASCII_CHARS[::-1]

'''
method resize():
    - takes as parameters the image, and the final width
    - resizes the image into the final width while maintaining aspect ratio
'''
def resize(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image
'''
method grayscalify():
    - takes an image as a parameter
    - returns the grayscale version of image
'''
def grayscalify(image):
    return image.convert('L')

'''
method modify():
    - replaces every pixel with a character whose intensity is similar
'''
def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

'''
method do():
    - does all the work by calling all the above functions
'''
def do(image, new_width=100):
    image = resize(image)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    # Construct the image from the character list
    new_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]

    return '\n'.join(new_image)

'''
method runner():
    - takes as parameter the image path and runs the above code
    - handles exceptions as well
    - provides alternative output options
'''
def runner(path = None):
    image = None
    searchTerm = sys.argv[1]
    searchTerm = searchTerm.replace("-"," ");
    
    for searchRes in wikipedia.search(searchTerm):
        #print("result dump:")
     #   print(searchRes)
        #if("dis" in searchRes.lower()):
            #disambiguation case, grab top link
            #print("disambiguation case, grab top link")
            #break
           #print("should ascify" + res.images())
        if(searchTerm.lower() == searchRes.lower()):
            #exact match case, find image thumbnail link
          #  print("#exact match case, find image thumbnail link " + searchRes)
            ("Downloading immages from exact match..")
            pageMatch = wikipedia.page(searchTerm)
           # print("should ascify" + searchRes + " using term " + searchTerm)   
          #  print(pageMatch.images)
            for image in pageMatch.images:
                if(".jpg" in image):
                    path = image
                  #  print("found jpg path")
                    break
                if(".png" in image):
                    path = image
                 #   print("found jpg path")
                    break
    if(path == None):
       # print("There was no jpg or png found for your search term.")
        quit()
    urllib.request.urlretrieve(path, "asciify.jpg")
    path = "asciify.jpg"
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in",path)
        #print(e)
        return
    image = do(image)

    # To print on console
    print(image)

    # Else, to write into a file
    # Note: This text file will be created by default under
    #       the same directory as this python file,
    #       NOT in the directory from where the image is pulled.
    f = open('img.txt','w')
    f.write(image)
    f.close()

'''
method main():
    - reads input from console
    - profit
'''
if __name__ == '__main__':
    import sys
    import urllib.request
    runner()
