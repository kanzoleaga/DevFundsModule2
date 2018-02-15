"""
File class inheritance from Asset
"""
import os
import win32security

from src.com.jalasoft.search_files.search.asset import Asset

class File(Asset):
    def __init__(self, path, name):
        super().__init__(path, name)
        self.extension = os.path.splitext(name)[1]
        self.owner = ''

    def get_extension(self):
        return self.extension

    # Size was not set as part of the constructor because of efficiency, It will be called only
    # if the search criteria includes size
    def set_size(self):
        self.size = os.path.getsize(self.path)

    # Owner was not set as part of the constructor because efficiency, It will be called only
    # if the search criteria includes owner
    def set_owner(self):
        file_and_folder = win32security.GetFileSecurity(self.path, win32security.OWNER_SECURITY_INFORMATION)
        username = win32security.LookupAccountSid(None, file_and_folder.GetSecurityDescriptorOwner())
        return username[0]





