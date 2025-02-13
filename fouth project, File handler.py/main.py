import os


class FileHandler:
    def __init__(self):
        self.folder_name = ''
        self.file_name = ''
        self.content = ''
        self.new_file_permition = False
    # Make folder
    def get_forder_name(self):
        self.folder_name = input('Name the folder>')
        while os.path.exists(self.folder_name) and os.path.isdir(self.folder_name):
            print('Folder exists, do you wand to add file to existing folder. Yes or No >')
            print(os.listdir(self.folder_name))
            answer = input('>')
            if answer == 'Yes' or 'yes':
                os.chdir(self.folder_name)
                self.new_file_permition = True
                break
            else:
                self.file_name = input('New folder name> \n')
                continue
        if not os.path.exists(self.folder_name) and os.path.isdir(self.folder_name):
            os.mkdir(self.folder_name)

    # Make file functionality
    def make_file(self):
        if self.new_file_permition:
            self.file_name = input('Name the file(with file extention(eg:- .py .txt)> \n')
            if os.path.exists(self.file_name):
                answer = input('Do you want to rewrite or add>')
                if 'rewrite' in answer:
                    content = input('What do you want to write file>')
                    with open(self.file_name, 'w') as f:
                        f.write(content)
                elif 'add' in answer:
                    content = input('What do you wan\'t to add to file>\n')
                    with open(self.file_name, 'a') as f:
                        f.write(f'\n{content}')

                print(f'Content writen to {self.file_name}')
            else:
                content = input('What do you want to write file>\n')
                with open(self.file_name, 'w') as f:
                    f.write(content)
                    print(f'Content writen to \n{self.file_name}')
        else:
            pass
    # Read file functionality
    def read_file(self):
        files = os.listdir()
        print(files)
        uer_input = input('Which one do you wan\'t to read>\n')
        if uer_input in files:
            content = []
            with open(uer_input, 'r') as f:
                content = f.readlines()
            for i in content:
                print(i, end='')
            print()

if __name__ == "__main__":
    file_hander = FileHandler()
    print('Welcome to file handler.')
    current_folder = os.path.dirname(__file__).split("/")
    print(f'Current directory \n{current_folder[-2]}')
    while True:
        try:
            a = input('What do you wan\'t to do?(make folder-Mf, write file-Wf, read file-Rf, change directory-Cd) eixt() to exit> \n')
            if a == 'exit()':
                print("Bye, have a nice day")
                break
            else:
                if a in ['Make folder', 'make folder', 'Mf', 'mf']:
                    file_hander.get_forder_name()
                    if file_hander.new_file_permition:
                        file_hander.make_file()
                        continue
                    else:
                        pass
                elif a in ['write file', 'Write file', 'Wr', 'wr']:
                    file_hander.new_file_permition = True
                    print(os.listdir())
                    file_hander.make_file()
                    continue
                elif a in ['Read file', 'read file', 'rf', 'Rf']:
                    file_hander.read_file()
                    continue
                else:
                    print("Command error")
        except OSError:
            print("Somting happend")
            print(str(OSError))