from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageOps
import os


'''
Oct 1, 2025

Use ImageDraw to draw lines and stuff

'''

from colorfunctions import gradient_colors



class blurbify:
    def __init__(self):
        self.savepath='/Users/shalevwiden/Downloads/Coding_Files/Python/BeautifulSoup_Library/tweet_generator/image_templates'

        self.pfppath=''

        self.username='swiden.mp4'
        self.usernamefont = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Helvetica.ttc",
            40  # font size
            )

        with open('bodytext.md') as bodytextcontent:
            self.bodytext=bodytextcontent.read()

        self.bodyfont=''

        self.location=''
        
    def create_template(self):
        '''
        This is where the height and width of the image can be changed
        '''

        fullimage = Image.new("RGB", (1080, 1200), "white")

        # this draw object is used alot
        draw = ImageDraw.Draw(fullimage)

        imagewidth, imageheight = fullimage.size





        if self.pfppath:
            # Open the image to insert
            img = Image.open(self.pfppath)

            # Resize so width = 200 px, keep aspect ratio
            wpercent = 200 / float(img.size[0])
            hsize = int(float(img.size[1]) * float(wpercent))
            img = img.resize((200, hsize), Image.LANCZOS)

            # Add black border
            img = ImageOps.expand(img, border=5, fill="black")

            # Paste into background (aligned inline, say top-left corner at (50,50))
            bg.paste(img, (50, 50))

        def draw_line():
            '''
            Just use this a bunch to get it right lol

            '''
            draw.line((50, 300, 800, 300), fill="grey", width=5)

            #x1,y1,x2,y2
            bottomlineheight=imageheight-200
            draw.line((50, bottomlineheight, 800, bottomlineheight), fill="grey", width=5)


        draw_line()

        def draw_username():
            usernamex=100
            usernamey=imageheight-(imageheight-200)
            draw.text((usernamex, usernamey), self.username, fill="black", font=self.usernamefont)
        draw_username()

        def write_message():
            messagex=100
            messagey=imageheight-(imageheight-300)
            # draw.text((messagex, messagey), self.bodytext, fill="black", font=self.usernamefont)


            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/arial.ttf", 30)

            bbox = draw.textbbox((20, 20), self.bodytext, font=font)  # (x0, y0, x1, y1)

            # Draw the text
            draw.text((20, 20), self.bodytext, font=font, fill="black")

            # Visualize the bounding box
            draw.rectangle(bbox, outline="red", width=2)

        write_message()
     # Save result
        def save():
            fullimagepath=os.path.join(self.savepath,'test1.png')
            fullimage.save(fullimagepath)
        save()
        print(f"Template saved at {self.savepath}")

    def create_many_images(self):
        pass
def main():
    blurb=blurbify()
    blurb.create_template()

main()