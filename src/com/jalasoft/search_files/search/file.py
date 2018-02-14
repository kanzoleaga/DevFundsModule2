"""
File class inheritance from Asset
"""
import os

from src.com.jalasoft.search_files.search.asset import Asset

class File(Asset):
    def __init__(self, path, name):
        super().__init__(path, name)
        self.extension = os.path.splitext(name)[1]
        self.owner = ''

    def get_extension(self):
        return self.extension

    def set_size(self):
        self.size = os.path.getsize(self.path)

    def set_owner(self):
        # file_and_folder = win32security.GetFileSecurity(filename, win32security.OWNER_SECURITY_INFORMATION)
        # username = win32security.LookupAccountSid(None, file_and_folder.GetSecurityDescriptorOwner())
        self.owner = 'kanzoleaga'

file = File('C:/Users\Katerina Anzoleaga/Documents', 'hello')
file.set_owner()
print(file.owner)



