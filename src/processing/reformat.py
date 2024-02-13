
# Purpose: To be able to convert an input file of a given format to a specified output file with new formatting

#Generates an outfile based on an infile with specified features array
def reformat(infile_name, outfile_name, wanted_features, lines_per_entry, new_delim):

    infile = open(infile_name, "r") #the file to read from
    outfile = open(outfile_name, "a+") #file to append to (create if does not exist)

    line_count = 0
    new_line = "" #line to append

    #stat printing values
    old_line_count = 0
    new_line_count = 0
    old_features = 0

    for line in infile: #iterate over every line
        old_line_count = old_line_count + 1
        
        line_count = line_count + 1
        new_line = new_line + " " + line #append several lines to 1 line

        if line_count == lines_per_entry: #time to append line to outfile

            new_line = new_line.split()
            if old_features == 0: #stat printing
                old_features = len(new_line)
            copy_line = []

            for key, val in enumerate(new_line):
                if key in wanted_features: #take only the features we want
                    copy_line.append(val)

            copy_line = new_delim.join(copy_line)
            copy_line = copy_line + "\n"
            outfile.write(copy_line) #append line

            #reset for next set
            new_line = ""
            line_count = 0
            
            new_line_count = new_line_count + 1 #stat printing
    print("Converted {} lines from {} -> {} lines in {}".format(old_line_count, infile_name, new_line_count, outfile_name))
    print("Previous feature count: {}, new feature count {}".format(old_features, len(wanted_features)))

features = [3, 4, 9, 10, 12, 16, 19, 32, 38, 40, 41, 44, 51, 58]
for key, val in enumerate(features):
    features[key] = val - 1 #subtract 1 from each because most people use 1-indexing instead of 0

reformat("cleveland.data", "newoutput.data", features, 10, ',')