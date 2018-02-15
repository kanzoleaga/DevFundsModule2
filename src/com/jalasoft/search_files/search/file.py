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
        # Get file owner
        file_and_folder = win32security.GetFileSecurity(self.path, win32security.OWNER_SECURITY_INFORMATION)
        file_owner = win32security.LookupAccountSid(None, file_and_folder.GetSecurityDescriptorOwner())
        self.owner = file_owner[0]

    def get_extension(self):
        return self.extension

    def get_owner(self):
        return self.owner

    # Size was not set as part of the constructor because of efficiency, It will be called only
    # if the search criteria includes size
    def set_size(self):
        self.size = os.path.getsize(self.path)
