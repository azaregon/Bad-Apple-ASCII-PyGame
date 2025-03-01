from PIL import Image

class Module:
    def __init__(self):
        pass


    def textify(self,filename):
        im = Image.open(filename)

        pix_val = list(im.getdata())



        for ind,x in enumerate(pix_val):
            #print(x)
            if x < (128,128,128):
                pix_val[ind] = '%'
            else:
                pix_val[ind] = '_'



        width,height = im.size

        #print(width,height)

        N = width
        sublist = [pix_val[n:n+N] for n in range(0,len(pix_val),N)]

        #print(len(sublist))

        resList = []

        for i in sublist:
            resList.append(str(i).replace("'",'').replace(",",""))
            #print(str(i).replace("'",'').replace(",",""))

        self.res = str(resList).replace(',','\n').replace("'",'')
        return self



if __name__ == '__main__':
    folder = 'BA36'

    import os



    #print(f)
    f = [i for i in range(0, 6569)]
    for i, x in enumerate(f):
        f[i] = str(x) + '.png'

    import pygame
    clk = pygame.time.Clock()
    f = ['146.png']
    for i in f:
        pass
        #clk.tick(30)
        g = Module().textify(f'{folder}/{i}').res
        print(g)
        #print(i)
        #os.system('cls')