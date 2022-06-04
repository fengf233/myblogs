from importlib.resources import path
import os

src_dir = r'docs'      
 
def list_docs_dir(src_dir):
    _dir = {}

    list_dir = os.listdir(src_dir)
    
    for i in range(0,len(list_dir)):

        path = os.path.join(src_dir,list_dir[i])
        
        if os.path.isdir(path):
            _dir[list_dir[i]] =list_md_file(path)

    return _dir

def list_md_file(file_dir):
    _md = []
    list_file = os.listdir(file_dir)
    
    for i in range(0,len(list_file)):

        path = os.path.join(file_dir,list_file[i])

        if path.endswith(".md"):
            _md.append(path)

    return _md

if __name__ == '__main__':

    files = list_docs_dir(src_dir)

    with open("README.md","w") as f:
        f.write("\n")
        for dir,mds in files.items() :
            f.write("## "+dir+"\n")
            for md in mds:
                f.write("- [{}]({})\n".format(
                    str(os.path.basename(md)).rstrip(".md"),
                    md
                ))
            f.write("\n")
