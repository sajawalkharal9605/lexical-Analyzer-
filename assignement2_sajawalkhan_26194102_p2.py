#task1


filename = "sajlexeme1.txt"

#user_input = input("Enter data to save in the file: ")

user_input="import maths\n\n def example_function():\n\n #this is a comment\n\n result=2+3\n\n return result"
                

def save_data_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
save_data_to_file(filename, user_input)



input_file = "sajlexeme1.txt"
output_file = "sajlexeme2.txt"


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK1<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



class Preprocessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def remove_blank_lines(self):
        with open(self.input_file, 'r') as file:
            lines = file.readlines()
            non_blank_lines = [line for line in lines if line.strip()]

        with open(self.output_file, 'w') as file:
            file.writelines(non_blank_lines)

    def remove_imports_annotations(self):
        with open(self.output_file, 'r') as file:
            lines = file.readlines()
            modified_lines = [line for line in lines if not line.strip().startswith(('import', '@'))]

        with open(self.output_file, 'w') as file:
            file.writelines(modified_lines) 


    def remove_comments_statements(self):
        with open(self.output_file, 'r') as file:
            lines = file.readlines()
            modified_lines = [line for line in lines if not line.strip().startswith(('#', '"""'))]

        with open(self.output_file, 'w') as file:
            file.writelines(modified_lines)


        
        

    def preprocess_file(self):
        self.remove_blank_lines()
        self.remove_comments_statements()
        self.remove_imports_annotations()
        
        print(f"Processed file saved to {self.output_file}")
        with open(self.output_file,'r') as file:
            data=file.read()
            print("Pre Processed File: \n"+ data)

        
input_file = "sajlexeme1.txt"
output_file ="sajlexeme2.txt" 

processor = Preprocessor(input_file, output_file)
processor.preprocess_file()
    




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK2<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



class Processor:
    def __init__(self,input_file,output_file):

        self.input_file=input_file2
        self.output_file=output_file2

    def BREAK_DATA_IN_CHARACTERS(self):
        
        with open(self.input_file, 'r') as input_file:
            
            buffer = []
            while True:
                char = input_file.read(1)
                
                if not char:
                    break
                
                if char != '\n':
                    buffer.append(char)

            
            buffer.append('$')

        
        with open(self.output_file, 'w') as output_file:
            output_file.write(''.join(buffer))

        
        #with open(self.output_file, 'r') as output_file:
            #data = output_file.read()
            #print("TASK 2 OUTPUT \n" + data) 


input_file2 = "sajlexeme2.txt"
output_file2 ="sajlexeme3.txt"

PROCESSOR=Processor(input_file2,output_file2)
PROCESSOR.BREAK_DATA_IN_CHARACTERS()



    


#class LexicalAnalyzer:


