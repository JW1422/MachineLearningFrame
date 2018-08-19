import csvkit as csv

class importdata:
    @classmethod
    def getcsvdata (filename):
        with open("Test.csv", "rb") as csvfile:
            data = csvfile.reader("Test.csv", '')
            for row in data:
                print(row)
    
        
    

