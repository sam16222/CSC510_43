from main import the as mainConfigurations

"""This function helps to read the CSV file given as input"""
def readCSV():
    dict = {}

    with open(mainConfigurations['csvFilePath']) as file:
        content = [line[:-1] for line in file]
    header = (content[:1][0]).split(',')
    rows = content[1:]

    for index in range(len(header)):
        rowArray = []
        
        for row in rows:
            rowArray.append(row[index])
        dict[header[index]] = rowArray

    print(dict)

"""Function call to read the CSV file contents"""
readCSV()
