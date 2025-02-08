import os

class FileHandler:
    def __init__(self):
        self.folder_name = ''
        self.file_name = ''
        self.content = ''
        self.new_file_permition = False

    def get_forder_name(self):
        self.folder_name = input('Name the folder>')
        while os.path.exists(f'{os.path}/{self.folder_name}'):
            print('Folder exists, do you wand to add file to existing folder. Yes or No >')
            print(os.listdir(f'{os.path}/{self.folder_name}'))
            answer = input('>\n')
            if answer == 'Yes' or 'yes':
                self.new_file_permition = True
                break
            else:
                self.file_name = input('New folder name> \n')
                continue

    def make_file(self):
        if self.new_file_permition:
            self.file_name = input('Name the file: \n')
            if os.path.exists(f'{os.path}/{self.file_name}'):
                answer = input('Do you want to rewrite')