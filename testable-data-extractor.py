# take output files from testable and extract relevant data to one file

# by Ethan Weed for Dyslexia Workshop 2016

# variables to extract:
# age, sex, studie, semester, mother language, reading problems,responses, RTs, correct

# import libraries for dealing with files
import os
import glob
import shutil

# make a new folder for the renamed files
newdir = 'PATH'
os.mkdir (newdir)

# copy all files to folder to be renamed
os.chdir('PATH') 
for file in glob.glob('*.csv'):
    shutil.copy(file, newdir)

# comforting message
print 'New folder created'


#move to the new folder to rename files
os.chdir(newdir)

# file renaming loop
filecounter = 1
for file in glob.glob('*.csv'): # go through the files in the directory 1 by 1
    filenum = str(filecounter)
    filecounter = filecounter + 1
    newfile = filenum + '.csv' # 
    os.rename(file, newfile) # take the old file name (*file*) and change it to the new one (*newfile*)
    # comforting message
    print 'Done with ' + filenum # sometimes it's nice to give yourself little progress messages
    
    
os.chdir(newdir) 

# make a new text file for the output
# make column headers
header = 'ID_num, age, sex, university, study, semester, mother_tongue, dyslexia, item, response, RT, correct \n'
output_file = 'PATH.csv'
with open(output_file, 'a+') as newfile:
    newfile.write(header)
newfile.close()

# this part is specific to the needs of this project. Change as needed.
for file in glob.glob('*.csv'):
    with open(file,'r') as f:

        text = f.read()
        print file

        #split input file into lines
        lines = text.split('\n')

        #get particpant ID from file name
        ID_filename = file[:-4]

        # find size of data file
        size = len(lines)

        info = lines[1].split(',')

        #print str(len(info))

        if len(info)==20:

            # make shorcuts for adding comma-seperators and line breaks to csv output file
            cs = ','
            nl = '\n'


            age = str(info[1])
            sex = str(info[2])
            uni = str(info[8])
            study = str(info[9])
            semester = str(info[10])
            mot_tongue = str(info[11])
            dyslexia = str(info[12])


            correct =[]

            # lines [4] = first line of data
            raw_data = lines[5:size-1]
            for s, val in enumerate(raw_data):
                #print s
                #print val
                data_i = val.split(',')
                #print data_i

                responses = data_i[36]
                RTs = data_i[37]
                correct = data_i[38]

                # add question number
                item = str(data_i [0])
                if item == '7':
                    item = '1'
                if item == '9':
                    item = '2'
                if item == '11':
                    item = '3'
                if item == '13':
                    item = '4'
                if item == '15':
                    item = '5'
                if item == '17':
                    item = '6'
                if item == '19':
                    item = '7'
                if item == '21':
                    item = '8'
                if item == '23':
                    item = '9'
                if item == '25':
                    item = '10'
                if item == '27':
                    item = '11'
                if item == '29':
                    item = '12'
                if item == '31':
                    item = '13'
                if item == '33':
                    item = '14'
                if item == '35':
                    item = '15'
                if item == '37':
                    item = '16'
                if item == '39':
                    item = '17'
                if item == '41':
                    item = '18'




                newline = (ID_filename + cs + age + cs + sex + cs + uni + cs + study + cs + semester + cs + mot_tongue + cs + dyslexia + cs + item + cs + responses + cs + RTs + cs + correct + nl)

                with open(output_file, 'a+') as newfile:
                    newfile.write(newline)
                newfile.close()
                
        elif len(info)<20:
            print ID_filename + ' did not complete test'

    f.close()
    
print 'All done!'


