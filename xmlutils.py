import xml.etree.cElementTree as ET
import folder as f
def parseXML(file_name):
   # Parse XML with ElementTree
   tree = ET.ElementTree(file=file_name)
   print(tree.getroot())
   root = tree.getroot()
   print(root.attrib.get('name'))
   print("tag=%s, attrib=%s" % (root.tag, root.attrib))

   # get the information via the children!
   print("-" * 25)
   print("Iterating using getchildren()")
   print("-" * 25)
   images = list(root)
   for image in images:
      image_children = list(image)
      for tag in image_children:
         print("%s=%s" % (tag.tag, tag.text))


def getFolderInfo(file_name):
    tree = ET.ElementTree(file=file_name)
    root = tree.getroot()
    return root.attrib

def getimageList(file_name):
   tree = ET.ElementTree(file=file_name)
   root = tree.getroot()
   images = list(root)
   imgList = []
   for image in images:
      desc=""
      name=""
      path=""
      date=""
      index=""
      port=False
      for tag in image:
         if tag.tag == 'name':
            name=tag.text
         if tag.tag== 'description':
            desc = tag.text
         if tag.tag== 'path':
            path = tag.text
         if tag.tag== 'date':
            date = tag.text
         if tag.tag== 'index':
            index = tag.text
         if tag.tag == "orientation":
            if tag.text == 'portrait' :
               port = True
      imgList.append(f.image(name,desc,date,index,path,port))
   imgList.sort(key=lambda x: (x.num))
   return imgList

