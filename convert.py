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
			for i in range(0,len(data['shapes'])):
				clss = data['shapes'][i]['label']
				box_lt = data['shapes'][i]['points'][0]
				box_rb = data['shapes'][i]['points'][1]
				result = str(clss)+" 0.00 0 0.0 "+str(int(box_lt[0]))+" "+str(int(box_lt[1]))+" "+str(int(box_rb[0]))+" "+str(int(box_rb[1]))+" 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n"
				#result = str(clss)+" "+str(int(box_lt[0]))+" "+str(int(box_lt[1]))+" "+str(int(box_rb[0]))+" "+str(int(box_rb[1]))+"\n"
				print(result)
				new_file.write(result)
				#print(clss)
			#shape = data['shapes'][0]
			#print(len(data['shapes']), end="\n")