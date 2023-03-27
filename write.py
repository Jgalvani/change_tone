import os

def create_dirs(output):
    directory = os.path.dirname(output)
    
    if directory and not os.path.isdir(directory):
        os.makedirs(directory)
        print(f'{directory} created')
        
    elif not os.path.isdir(output):
        os.makedirs(output)
        print(f'{output} created')
    else:
        print(f'could not create {output}')
        
		
def create_file(output, txt):
    create_dirs(output)
 
    with open(output, 'w', newline='\n', encoding='utf-8') as file:
        file.write(txt)
        
    print(f'{output} was created')