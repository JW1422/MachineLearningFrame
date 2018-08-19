import csv

class importdata:
    @classmethod
    def getcsvdata (filename):
        with open('Test.csv', 'r') as csvfile:
            data = csv.reader(csvfile)
            line_counter = 0
            for row in data:
                if(line_counter == 0):
                    print(f'Column names are {", ".join(row)}')
                    line_count = line_counter + 1
                    #split the columns up from how many commans there are from the row + 1
                    #assign the label variables as lists - this might need to have a get header method                    
                else:
                    print(row)
                    #add to the lists 
    #have a method that gets called to collect and input the data into the classifier
    #this will then output the accuracy of what it believes it is
    
        
    

