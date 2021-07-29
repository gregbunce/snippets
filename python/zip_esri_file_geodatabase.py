import os, zipfile

#: This function zips an esri file geodatabase using python 3 (note: full_path_to_fgdb must include the .gdb file extention).
def zip_fgdb(full_path_to_fgdb):
    outFile = full_path_to_fgdb[0:-4]+'_gdb.zip'
    gdbName = os.path.basename(full_path_to_fgdb)

    with zipfile.ZipFile(outFile,mode='w',compression=zipfile.ZIP_DEFLATED,allowZip64=True) as myzip:
        for f in os.listdir(full_path_to_fgdb):
            if f[-5:] != '.lock':
                myzip.write(os.path.join(full_path_to_fgdb,f),gdbName+'\\'+os.path.basename(f))
                
