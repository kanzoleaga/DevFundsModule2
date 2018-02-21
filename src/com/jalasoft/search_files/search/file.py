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
        self.has_content = False

    def get_extension(self):
        return self.extension

    def get_owner(self):
        return self.owner

    def set_owner(self):
        sec_info = win32security.GetFileSecurity(self.path, win32security.OWNER_SECURITY_INFORMATION)
        sid = sec_info.GetSecurityDescriptorOwner()
        self.owner = win32security.LookupAccountSid(None, sid)[0]

    def search_by_content(self, content):
        if self.is_binay_file():
            return self.has_content
        else:
            with open(self.path) as file_content:
                for line in file_content:
                    if content in line:
                        self.has_content = True
                        break
        return self.has_content

    def is_binay_file(self):
        textchars = bytearray([7, 8, 9, 10, 12, 13, 27]) + bytearray(range(0x20, 0x7f)) + bytearray(range(0x80, 0x100))
        is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

        if is_binary_string(open(self.path, 'rb').read(1024)):
            return True
        else:
            return False

    # Size was not set as part of the constructor because of efficiency, It will be called only
    # if the search criteria includes size
    def set_size(self):
        self.size = os.path.getsize(self.path)



