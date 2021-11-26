from matplotlib import image
import numpy as np
from PIL import Image
path = [0] * 3
path[0] = '/Users/mikhail/Desktop/python_3sem/laba/lab3/epis1/lunar01_raw.jpg'
path[1] = '/Users/mikhail/Desktop/python_3sem/laba/lab3/epis1/lunar02_raw.jpg'
path[2] = '/Users/mikhail/Desktop/python_3sem/laba/lab3/epis1/lunar03_raw.jpg'
img1 = Image.open(path[0])
img2 = Image.open(path[1])
img3 = Image.open(path[2])
def contr(img):
    data = np.array(img)
    min=np.min(data)   
    max=np.max(data) 
    LUT=np.zeros(256,dtype=np.uint8)
    LUT[min:max+1]=np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True,dtype=np.uint8)
    new_data = []
    new_data[1]= LUT[data]
    return 
    #print(data)
    #print(LUT[data])
    # запись картинки после обработки
new_im = Image.fromarray(new_data).save('result.png')


