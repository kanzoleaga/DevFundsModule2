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

    def get_owner(self):
        return self.owner

    def set_owner(self):
        sec_info = win32security.GetFileSecurity(self.path, win32security.OWNER_SECURITY_INFORMATION)
        sid = sec_info.GetSecurityDescriptorOwner()
        self.owner = win32security.LookupAccountSid(None, sid)[0]




    # Size was not set as part of the constructor because of efficiency, It will be called only
    # if the search criteria includes size
    def set_size(self):
        self.size = os.path.getsize(self.path)



