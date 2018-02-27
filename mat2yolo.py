import os
import scipy.io
# http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz
from imaging.PIL import Image

img_dir = 'images/'
output_dir = 'output/'

mat = scipy.io.loadmat('groundtruth.mat')
groundtruth = mat['groundtruth']
items = groundtruth[0]

# Taken from https://github.com/Guanghan/darknet/blob/master/scripts/convert.py
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


classes = []
    
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for item in items: 
    # Get folder & file name
    img_path = item[0][0]
    
    mid = img_path.find('\\')
    folder = img_path[:mid]
    
    ext = img_path.find('.')
    file_name = img_path[mid+1:ext]
   
    class_num = -1 
    # Get class number
    if folder not in classes: 
        classes.append(folder)
    class_num = classes.index(folder)

    # Get coordinates to put in the file
    coordinates = item[1][0]
    
    # Convert coordinates to yolo format
    xmin = coordinates[0]
    xmax = coordinates[2]
    ymin = coordinates[1]
    ymax = coordinates[3]

    image = Image.open(img_dir + folder + '/' + file_name + '.jpg')
    width = int(image.size[0])
    height = int(image.size[1])

    b = (float(xmin), float(xmax), float(ymin), float(ymax))
    bb = convert((width, height), b)
    
    # Create folder if it doesn't exist
    if not os.path.exists(output_dir + folder):
        os.makedirs(output_dir + folder)

    # Create file
    f = open(output_dir + folder + '/' + file_name + '.txt', 'w')
    f.write(str(class_num) + " " + " ".join([str(a) for a in bb]) + '\n')
    

    
