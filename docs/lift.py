from liftover import get_lifter
import csv

converter = get_lifter('hg19', 'hg38')
with open('Website_ResultsMX.csv', newline='') as f, open('Website_ResultsMX_lift.csv', 'w', newline='') as g:
    reader = csv.reader(f, delimiter=',')
    writer = csv.writer(g, delimiter=',')
    heading = next(reader)
    heading.append('EnhancerCoordinatesHg19')
    coord_col = heading.index('EnhancerCoordinates')
    heading[coord_col] = 'EnhancerCoordinatesHg38'
    writer.writerow(heading)
    for row in reader:
        chrom, range = row[coord_col].split(':')
        chrom = chrom[3:]
        start, end = range.split('-')
        new_start = converter[chrom][int(start)]
        new_end = converter[chrom][int(end)]
        row.append(f'{new_start[0][0]}:{new_start[0][1]}-{new_end[0][1]}')
        writer.writerow(row)
