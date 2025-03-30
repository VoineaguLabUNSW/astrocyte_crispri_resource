import csv, json, sys

# Simple script to create byte-ranges for partial CSV downloading from JS
def makeIndex(input, header_lines=2):
    header, indices = [], {}
    with open(input, 'r') as fi:
        while header_lines > 0:
            header.append(fi.readline())
            header_lines -= 1

        # N.B tell() is the END of the last read line
        prevGroupStart, prevLineStart, prevGroup = fi.tell(), fi.tell(), None
        while line := fi.readline():
            currGroup = next(csv.reader([line]))[0]
            if currGroup != prevGroup:
                if prevGroup is not None: 
                    indices[prevGroup] = (prevGroupStart, prevLineStart)
                prevGroupStart, prevGroup = prevLineStart, currGroup
            prevLineStart = fi.tell()
        indices[prevGroup] = (prevGroupStart, fi.tell())      
    return {'indices': indices, 'header': header}

# Debugging
def printIndex(output):
    for k,v in output.items():
        with open(k, 'rb') as fi:
            for k2,v2 in v['indices'].items():
                print(k2 + ":")
                fi.seek(v2[0])
                data = fi.read(v2[1]-v2[0])
                print(data.decode("utf-8"), end="\n\n")

if __name__ == "__main__":
    # Combine all indices into a single file to minimize GitHub Pages throttling
    output = {"prefix": sys.argv[1], "files": {input: makeIndex(input) for input in ['Enh_annot_FullTable.csv', 'Gene_annot_FullTable.csv']}}
    with open('indexer_output.json', 'w') as fo:
        json.dump(output, fo)
