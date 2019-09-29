#参数1：.csv 参数2：.fasta2 输出：带有位置信息的fasta2
import sys

transcripts = dict()
with open(sys.argv[1], 'r') as csv:
        for line in csv:
            item = line.strip().split(',')
            if item[0] == "Species":
                continue
            transcript_id = item[3]
            chrome = item[5]
            start = item[6]
            end = item[7]
            strand = item[8]
            if transcript_id in transcripts:
                transcripts[transcript_id].append(chrome)
                transcripts[transcript_id].append(strand)
                transcripts[transcript_id].append(start)
                transcripts[transcript_id].append(end)
            else:
                transcripts[transcript_id] = list()
                transcripts[transcript_id].append(chrome)
                transcripts[transcript_id].append(strand)
                transcripts[transcript_id].append(start)
                transcripts[transcript_id].append(end)

gene_noposition = []

file_out2 = open('../plant_lncrna_position_fa/' + sys.argv[2], 'w')
with open(sys.argv[2], 'r') as fasta2:
    for line in fasta2:
        if line[0] == '>':
            genename = line[1:].strip()
            if genename in transcripts:  
                info = transcripts[genename] 
                line = '>'+ genename + ' ' + ' '.join(info) + ' ' + 'lncRNA' + '\n'
            else:
                gene_noposition.append(genename)
        file_out2.write(line)

file_out3 = open('../plant_lncrna_position_fa/' + sys.argv[3], 'w')
with open(sys.argv[3], 'r') as fasta3:
    for line in fasta3:
        if line[0] == '>':
            genename = line[1:].strip()  
            if genename in transcripts:  
                info = transcripts[genename] 
                line = '>'+ genename + ' ' + ' '.join(info) + ' ' + 'lncRNA' + '\n'
            else:
                gene_noposition.append(genename)
        file_out3.write(line)

file_out4 = open('../plant_lncrna_position_fa/' + sys.argv[4], 'w')
with open(sys.argv[4], 'r') as fasta4:
    for line in fasta4:
        if line[0] == '>':
            genename = line[1:].strip()  
            if genename in transcripts:  
                info = transcripts[genename] 
                line = '>'+ genename + ' ' + ' '.join(info) + ' ' + 'lncRNA' + '\n'
            else:
                gene_noposition.append(genename)
        file_out4.write(line)

file_out5 = open('../plant_lncrna_position_fa/' + sys.argv[5], 'w')
with open(sys.argv[5], 'r') as fasta5:
    for line in fasta5:
        if line[0] == '>':
            genename = line[1:].strip()  
            if genename in transcripts:  
                info = transcripts[genename] 
                line = '>'+ genename + ' ' + ' '.join(info) + ' ' + 'lncRNA' + '\n'
            else:
                gene_noposition.append(genename)
        file_out5.write(line)
print(gene_noposition)

csv.close()
fasta2.close()
fasta3.close()
fasta4.close()
fasta5.close()
file_out2.close()
file_out3.close()
file_out4.close()
file_out5.close()