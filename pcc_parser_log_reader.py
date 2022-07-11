
def get_parameter_avd(log_path):
    offsets = []
    lengths = []
    with open(log_path,'r') as f1:
        lines = f1.readlines()
        offset_counter = 0
        avd_length = 0
        for line in lines:
            segs = line.split()
            if len(segs) > 1 and segs[1].endswith("decode:"):
                break
            try:
                line_type = int(segs[6])
            except:
                continue
            print(line_type)
            if line_type < 4:
                offset_counter += int(segs[3])
            elif line_type == 4:
                offsets.append(offset_counter)
                offset_counter += int(segs[3])
                lengths.append(int(segs[3]))
        return (offsets,lengths)


if __name__=="__main__":
    log_path = "mid/pcc_parser_log.txt"
    offsets, lengths = get_parameter_avd(log_path)
    print(offsets,lengths)