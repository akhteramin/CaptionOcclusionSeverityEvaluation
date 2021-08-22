import glob
# files = glob.glob( '*.txt' )
files = ["result_n.txt","result_i.txt","result_e.txt","result_p.txt","result_w.txt","result_s.txt"]

with open('result.txt', 'w') as result:
    for file_ in sorted(files):
        print(file_)
        for line in open( file_, 'r' ):
            result.write( line )
        result.write("\n")