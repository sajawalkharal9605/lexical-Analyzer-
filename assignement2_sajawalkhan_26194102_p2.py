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
        print()
        with open(self.output_file,'r') as file:
            data=file.read()
            print("TASK 1 OUTPUT IS: \n"+ data)

        
input_file = "sajlexeme1.txt"
output_file ="sajlexeme2.txt" 

processor = Preprocessor(input_file, output_file)
processor.preprocess_file()
    
print()



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

        
        with open(self.output_file, 'r') as output_file:
            
            data = output_file.read()
            print("TASK 2 OUTPUT \n" + data) 


input_file2 = "sajlexeme2.txt"
output_file2 ="sajlexeme3.txt"

PROCESSOR=Processor(input_file2,output_file2)
PROCESSOR.BREAK_DATA_IN_CHARACTERS()

print()
print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK3<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    

import re

class LexicalAnalysis:
    #def __init__(self,input_file,output_file)

    #self.input_file=input_file
    #self.ouput_file=output_file

    def generator(self, input_file, output_file):
        
        with open(input_file, 'r') as file:
            content = file.read()

        
        keyword_pattern = r'\b(?:and|as|assert|break|class|continue|def|del|elif|else|except|False|finally|for|from|global|if|import|in|is|lambda|None|nonlocal|not|or|pass|raise|return|True|try|while|with|yield)\b'
        identifier_pattern = r'\b[a-zA-Z_]\w*\b'
        operator_pattern = r'\+|-|\*|\/|%|=|==|!=|<|>|<=|>=|and|or|not|in|is'
        punctuator_pattern = r'{|}|\[|\]|\(|\)|,|;|:|\.'
        literal_pattern = r'\b(?:\d+\.?\d*|".*?"|\'.*?\')\b'

        
        combined_pattern = re.compile(f'({keyword_pattern}|{identifier_pattern}|{operator_pattern}|{punctuator_pattern}|{literal_pattern})', re.DOTALL)

        
        lexemes = []
        for token in combined_pattern.findall(content):
            if token.strip():
                lexemes.append(token)


        self.write_lexemes_to_file(lexemes, output_file)

    def write_lexemes_to_file(self, lexemes, output_file):
        with open(output_file, 'w') as file:
            for lexeme in lexemes:
                file.write("Lexeme: " + lexeme + '\n')
                
        with open(output_file,'r') as file:
            data=file.read()
            print("task3 output is: \n"+ data)
        
input_file3 = "sajlexeme3.txt"
output_file3 = "sajlexeme4.txt"


analyzer = LexicalAnalysis()
analyzer.generator(input_file3, output_file3)
