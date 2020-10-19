"""Format converter for label_jl

"""
import json
import os
dirs = os.listdir(".")
#print(dir)
for i in dirs:
    if os.path.splitext(i)[1] == ".json":
        with open(i,'r',encoding='utf8') as f:
            #line = f.readline()
            data = json.load(f)
            print(i)
            new_file = open("label_new/"+str(os.path.splitext(i)[0])+'.txt', 'w+')
            for i in range(0,len(data['outputs']['object'])):
                prefix = data['outputs']['object'][i]
                clss = prefix['name']
                box_lt = [prefix['bndbox']['xmin'], prefix['bndbox']['ymin']]
                box_rb = [prefix['bndbox']['xmax'], prefix['bndbox']['ymax']]
                result = str(clss)+" 0.00 0 0.0 "+str(int(box_lt[0]))+" "+str(int(box_lt[1]))+" "+str(int(box_rb[0]))+" "+str(int(box_rb[1]))+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n"
                print(result)
                new_file.write(result)