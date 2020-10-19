import os

def read_file_list(path):
    '''
        Read file list in directory.
    '''
    return os.listdir(path)

def filename(file):
    '''
        Getting the name of the file without the extension. 
    '''
    return os.path.splitext(file)[0]

label_path = "./data/dataset_2/label"
image_path = "./data/dataset_2/image_2"

label_file_list = read_file_list(label_path)
image_file_list = read_file_list(image_path)

label_list = []
image_list = []

for label_name in label_file_list:
    label_list.append(filename(label_name))

for image_name in image_file_list:
    image_list.append(filename(image_name))

# set_A.difference(set_B) = set_A - set_B
delete_list = set(image_list).difference(set(label_list))

dirs = os.listdir(".")

for i in dirs:
    if os.path.splitext(i)[0] in delete_list:
        os.remove(i)
