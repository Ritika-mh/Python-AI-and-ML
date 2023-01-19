import os
import hashlib
from sys import *
def hashfile(path,blocksize=1024):
    afile=open(path,"rb")
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    flag=os.path.isabs(path)
    if flag== False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)
    dups={}
    if exists:
        for Dirname,subdi,filelist in os.walk(path):
            for flen in filelist:
                path=os.path.join(Dirname,flen)
                file_hash=hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]

        return dups
    else:
        print("Invalid Path")
        exit()
def PrintDuplicate(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicate found:")

        print("The following files are identical.")

        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    print('\t\t%s'%subresult)

    else:
        print("No duplicate found")
def main():
    print("Directory Checksum cal  application")
    print("Application name:",argv[0])
    if(argv[1] == "-h")  or(argv[1]=="-H"):
        print("This script will travel the directory and display checksum of files")
        exit()

    if(argv[1] == "-u") or (argv[1]=="-U"):
        print("Usage : Application_name Direcory_Name ")
        exit()

    if (len(argv) != 2):
        print("Insufficient arguments")
        exit()
    try:
        arr={ }
        arr=FindDuplicate(argv[1])
        PrintDuplicate(arr)
    except ValueError:
        print("Error:Invalid datatype of input")
    except Exception as E:
        print("Error:Invalid input",E)

if(__name__ == "__main__"):
    main()