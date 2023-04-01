# I had to create some complexe object so I defined them here.
# That can be usefull as sometimes it's hard to only compute with letter or number variables 

class folder:
    def __init__(self,name="",description="",date="",fimage="",foldernum=0):
        self.name =name
        self.description = description
        self.date = date
        self.cover = fimage
        self.foldernum = foldernum

class image:
        def __init__(self,name="",description="",date="",num=0,path="",port=False):
            self.name =name
            self.description = description
            self.date = date
            self.num = num
            self.path=path
            self.portrait = port