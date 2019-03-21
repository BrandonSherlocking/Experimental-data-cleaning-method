
import csv, os

os.chdir('press_data')
 

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue	# skip non-csv files
 
	print('Removing header from ' + csvFilename + '...')
 
	# Read the CSV file in (skipping first row).
	csvRows = []
	csvFileObj = open(csvFilename, encoding='utf-8')
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue	# skip first row
		row = row[0].split(';')
		csvRows.append(row)
	csvFileObj.close()

	# Process the rows and columns, take the first six rows of the source data,
	# and delete the first 12 columns of the second row to the last row.
	csvRows = csvRows[:6]
	for i in range(len(csvRows)):
		if i == 0:
			continue
		del csvRows[i][:12]

	# Reassign a new header to each row
	csvRows[0].insert(0, 'Time')
	csvRows[1].insert(0, 'Pressure1')
	csvRows[2].insert(0, 'Pressure1')
	csvRows[3].insert(0, 'Pressure1')
	csvRows[4].insert(0, 'temperature1')
	csvRows[5].insert(0, 'temperature2')

	# Transpose data
	csvRows = [[row[i] for row in csvRows] for i in range(len(csvRows[0]))]

	# def transpose(self, matrix):
 #        new_matrix = []
 #        for i in range(len(matrix[0])):
 #            matrix1 = []
 #            for j in range(len(matrix)):
 #                matrix1.append(matrix[j][i])
 #            new_matrix.append(matrix1)
 #        return new_matrix

 
	# Write out the CSV file.
	os.makedirs('specification_data', exist_ok=True)
	csvFileObj_new  = open(os.path.join('specification_data', csvFilename), 'w', 
					newline='')
	csvWriter = csv.writer(csvFileObj_new)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()
