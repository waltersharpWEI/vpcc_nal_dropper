
def pull_file_part(inpath, outpath, start_offset, length):
    with open(inpath,'rb') as f1:
        f1.seek(start_offset)
        with open(outpath,'wb') as f2:
            buf = f1.read(length)
            f2.write(buf)
    return 0

if __name__=="__main__":
    inpath = "C:\\Users\\water\\Downloads\\s3_loot_120\\s2.bin"
    outpath = "C:\\Users\\water\\Downloads\\s3_long\\s3_32\\avcc.s2.bin"
    header_size = 20
    pull_file_part(inpath,outpath,148653+header_size,15767)