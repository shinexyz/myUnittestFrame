import os
#获取当前目录
def get_path():
    path=os.path.split(os.path.realpath(__file__))[0]
    return path
#获取根目录
def get_rootPath():
    project_path = os.path.abspath(os.path.dirname(__file__))
    root_path = project_path[:project_path.find("{}\\".format("UnittestAndRequests")) + len("{}\\".format("UnittestAndRequests"))]
    return root_path
if __name__ == '__main__':
    print(get_rootPath())

