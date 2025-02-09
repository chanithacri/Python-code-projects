import os

class FileHandler:
    def __init__(self):
        self.folder_name = ''
        self.file_name = ''
        self.content = ''
        self.new_file_permition = False

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

    def make_file(self):
        if self.new_file_permition:
            self.file_name = input('Name the file(with file extention(.txt)> \n')
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
                content = input('What do you want to write file>')
                with open(self.file_name, 'w') as f:
                    f.write(content)
                    print(f'Content writen to {self.file_name}')
        else:
            pass

if __name__ == "__main__":
    try:
        file_hander = FileHandler()
        print('Welcome to file handler.')
        a = input('What do you wan\'t to do?(make folder, write file, read file)>')
        if a == 'make folder' or 'Make folder':
            file_hander.get_forder_name()
            if file_hander.new_file_permition:
                file_hander.make_file()
            else:
                pass
    except OSError:
        print(OSError.text())