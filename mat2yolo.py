import os
import scipy.io


mat = scipy.io.loadmat('groundtruth.mat')
groundtruth = mat['groundtruth']
items = groundtruth[0]


classes = []
    
if not os.path.exists('output'):
    os.makedirs('output')

for item in items: 
    # Get folder & file name
    file_name = item[0][0]
    
    mid = file_name.find('\\')
    folder = file_name[:mid]
    
    ext = file_name.find('.')
    file_name = file_name[mid+1:ext]
   
    class_num = -1 
    # Get class number
    if folder not in classes: 
        classes.append(folder)
    class_num = classes.index(folder)

    # Get coordinates to put in the file
    coordinates = item[1][0]

    # Create folder if it doesn't exist
    if not os.path.exists('output/' + folder):
        os.makedirs('output/' + folder)

    # Create file
    f = open('output/' + folder + '/' + file_name + '.txt', 'w')
    f.write(str(class_num) + ' ' + str(coordinates[0]) + ' ' + str(coordinates[1]) + ' ' + str(coordinates[2]) + ' ' + str(coordinates[3]))
    

    
