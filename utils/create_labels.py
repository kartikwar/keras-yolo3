import os
import numpy as np
import  json

def create_file(folder_path, type_file='train'):
	text_lines = []
	all_folders = os.listdir(folder_path)
	folders_to_keep = []
	val_folders = []
	save_path = ''
	all_jsons = []
	if type_file == 'train':
		folders_to_keep = [folder for folder in all_folders if folder not in val_folders]
		save_path = '../train.txt'
	else:
		folders_to_keep = val_folders
		save_path = '../val.txt'

	json_matrix = [[os.path.join(folder_path, l_folder, l_file) for l_file in os.listdir(os.path.join(folder_path, l_folder)) if '.json' in l_file] for l_folder in folders_to_keep]
	json_list = np.array(json_matrix).flatten().tolist()

	for json_f in json_list:
		root_path = json_f.replace(json_f.split("/")[-1], "")
		im_path= ''

		with open (json_f) as jf:
			labels = json.load(jf)

			for file_name, label in labels.items():

				textline = ''
				boxes = []
				regions = label.get("regions")
				im_path = os.path.join(root_path, label.get('filename'))

				for i, region in enumerate(regions):
					coordinates = region.get("shape_attributes")
					x, y, width, height = coordinates['x'], coordinates['y'], coordinates['width'], coordinates[
						'height']
					boxes.extend([str(x) + ',' + str(y) + ',' + str(x + width) + ',' + str(y + height) + ',' + str(0)])

				if len(boxes):
					# textline += im_path + " " + str(boxes).replace("[", "").replace("]", "").strip()
					textline += im_path + " " + " ".join(boxes).strip()
					text_lines.append(textline)
					temp = 0



	f = open(save_path, 'w')
	for ele in text_lines:
		f.write(ele + '\n')
	f.close()

def create_file(folder_path, type_file='train'):
	text_lines = []
	all_folders = os.listdir(folder_path)
	folders_to_keep = []
	val_folders = []
	save_path = ''
	all_jsons = []
	if type_file == 'train':
		folders_to_keep = [folder for folder in all_folders if folder not in val_folders]
		save_path = '../train.txt'
	else:
		folders_to_keep = val_folders
		save_path = '../val.txt'

	json_matrix = [[os.path.join(folder_path, l_folder, l_file) for l_file in os.listdir(os.path.join(folder_path, l_folder)) if '.json' in l_file] for l_folder in folders_to_keep]
	json_list = np.array(json_matrix).flatten().tolist()

	for json_f in json_list:
		root_path = json_f.replace(json_f.split("/")[-1], "")
		im_path= ''

		with open (json_f) as jf:
			labels = json.load(jf)

			for file_name, label in labels.items():

				textline = ''
				boxes = []
				regions = label.get("regions")
				im_path = os.path.join(root_path, label.get('filename'))

				for i, region in enumerate(regions):
					coordinates = region.get("shape_attributes")
					x, y, width, height = coordinates['x'], coordinates['y'], coordinates['width'], coordinates[
						'height']
					boxes.extend([str(x) + ',' + str(y) + ',' + str(x + width) + ',' + str(y + height) + ',' + str(0)])

				if len(boxes):
					# textline += im_path + " " + str(boxes).replace("[", "").replace("]", "").strip()
					textline += im_path + " " + " ".join(boxes).strip()
					text_lines.append(textline)
					temp = 0



	f = open(save_path, 'w')
	for ele in text_lines:
		f.write(ele + '\n')
	f.close()
	temp = 0

	temp = 0
# labels_json = [l_file for l_file in os.listdir(l_folder) for l_folder in all_folders]



if __name__ == '__main__':
	# all_folders = os.listdir("/home/kartik/Downloads/Data-20200416T060849Z-001/Data/completed")
	create_file(folder_path="/home/siddhant/aramco/completed")
	#create_file(folder_path="/home/kartik/Downloads/Data-20200416T060849Z-001/Data/completed", type_file='val')
	pass
