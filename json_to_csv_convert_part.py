''' Created by Jeremy Reynolds for UALR COSMOS Team
	Converts part of all json files in the INPUT_DIR directory to
	csv files following the parameters on row 33.
	Will use the same filename for the .csv as from the .json
	
	This file must be in a directory along with a folder
	named "json" which contains the json files.
	The output directory "csv" will be created at launch.
	
	WARNING: Data will be appended to the .csv file if re-ran.
'''

import csv, glob, gzip, json, os

INPUT_DIR = './json/'
OUTPUT_DIR = './csv/'

count = 0

if not os.path.exists(OUTPUT_DIR):
	os.makedirs(OUTPUT_DIR)

# for file in glob.glob(INPUT_DIR + '/*.json'):		# Use this block if uncompressed .json
	# with open(file, encoding='utf-8-sig') as f:
		# data = json.loads(f.read())
		
for file in glob.glob(INPUT_DIR + '/*.json.gz'):	# Use this block if compressed .json.gz
	with gzip.open(file, 'rb') as f:
		data = json.loads(f.read())
		
	# Removes directory names from filepath (./json\filename123.json = filename123)
	filename = file.split("\\")[1].split(".json")[0]
	count += 1
	
	with open(OUTPUT_DIR + filename + '.csv', 'a', encoding='utf-8-sig', newline='') as f:
		writer = csv.writer(f)
		writer.writerow([data['text'],data['entities']['urls']])	# Items you want saved to csv.
	print(count, filename, '\tid:', data['id'])