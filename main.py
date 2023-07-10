import easyocr

def get_file_path():

    print('Enter the path to the file: ')
    file_path = input()

    return file_path



def get_text(file_path):
    """Open the file, read the text"""

    try:
        reader = easyocr.Reader(["en", "ru"])
        result = reader.readtext(file_path, detail=0)


        if len(result) > 0:
            print('The text was recognized successfully')
            print(result)
            
        else:
            print('The text was not detected')

        return result
    
    
    except FileNotFoundError:
        print('The file or directory does not exist')
        


path = get_file_path()
get_text(path)