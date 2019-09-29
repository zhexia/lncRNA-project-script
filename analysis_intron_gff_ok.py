def intron_statistics(inputfile_name,outfile_name):  #,outfile_name_2):
    inputfile_genome_gff = open(inputfile_name, "r")
    outfile_intron_length = open(outfile_name,"w")
#    outfile_exon_order = open(outfile_name_2,"w")
    import re
    from collections import defaultdict
    exon_id_start_end_dict = defaultdict(list)
    intron_length_dict = {}
    intron_length, num_intron, sumlength_intron = 0, 0, 0
    for line in inputfile_genome_gff:
        item = line.strip().split("\t")
        if ("#" not in line) and (line[0] != "\n"):
            if item[2] == "exon":
                exon_parent_id = re.findall("Parent=([^;]*)",item[8])[0]
                exon_id_start_end_dict[exon_parent_id].append([int(item[3]),int(item[4])])
                if int(item[3]) > int(item[4]):
                    print(exon_parent_id)
    print("The number of exon_parent_id are {}".format(len(exon_id_start_end_dict)))  

    for exon_id, exon_start_end in exon_id_start_end_dict.items():
        index = 0
        specific_num_intron = 0
     #   outfile_exon_order.write(exon_id + " " + str(sorted(exon_start_end)) + "\n")
        for i in sorted(exon_start_end):
    #        print(exon_id,sorted(exon_start_end))
            if len(exon_start_end) == 1:
                continue                                #############################################单外显子的基因
            else:
              
                if int(i[0]) > index:
                    if index == 0:
                        index = int(i[1])
                    else:
                        num_intron += 1
                        specific_num_intron += 1
                        intron_length = int(i[0]) - index + 1
                        sumlength_intron += intron_length
                        index = int(i[1])
                        intron_length_dict[exon_id + "_exon_" + str(specific_num_intron)] = intron_length
                     #   outline = exon_id + "_intron_" + str(specific_num_intron) + "," + str(intron_length) + "\n"
                     #   outfile_intron_length.write(outline)
                        outfile_intron_length.write(str(intron_length)+ "\n")
                else:
                    print(exon_id,int(i[0]),index)

    print("The total number of intron are {}".format(num_intron))    
    print("The average length of intron is {}".format(round(sumlength_intron/num_intron,2)))        
    inputfile_genome_gff.close()
    outfile_intron_length.close()
 #   outfile_exon_order.close()

inputfile_name = "ITAG3.2_gene_models.gff"
outfile_name = "ITAG3.2_gff_intron.csv"
#intron_statistics(inputfile_name,outfile_name)

inputfile_name2 = "../Pepper_1.55.gene_models.gff3"
outfile_name2 = "pepper_CM334_intron_gff.csv"
#intron_statistics(inputfile_name2,outfile_name2)

inputfile_name3 = "../Capsicum.annuum.L_Zunla-1_v2.0_genes.gff"
outfile_name3 = "pepper_zunla_intron_gff.csv"
#intron_statistics(inputfile_name3,outfile_name3)

inputfile_name4 = "../GCF_000715135.1_Ntab-TN90_genomic.gff"
outfile_name4 = "tobacco_TN90_intron_gff.csv"
#outfile_name4_2 = "tobacco_TN90_order_exon.csv"
intron_statistics(inputfile_name4, outfile_name4)#, outfile_name4_2)

inputfile_name5 = "../Nitab-v4.5_gene_models_Chr_Edwards2017.gff"
outfile_name5 = "tobacco_K236_intron_gff.csv"
#intron_statistics(inputfile_name5,outfile_name5)

def intron_statistics_easy(inputfile_name,outfile_name):
    inputfile_genome_gff = open(inputfile_name, "r")
    outfile_intron_length = open(outfile_name,"w")
    intron_length, sumlength_intron = 0, 0
    intron_start_end = []
    for line in inputfile_genome_gff:
        item = line.strip().split("\t")
        if ("#" not in line) and (item[2] == "intron"):
            intron_start_end.append([item[3],item[4]])

    print("The total number of introns are {}".format(len(intron_start_end)))

    for i in intron_start_end:
        intron_length = int(i[1]) - int(i[0]) + 1
        outfile_intron_length.write(str(intron_length) + "\n")
        sumlength_intron += intron_length

    print("The average length of intron is {}".format(round(sumlength_intron/len(intron_start_end),2)))
    inputfile_genome_gff.close()
    outfile_intron_length.close()
inputfile_potato = "../PGSC_DM_V403_genes.gff"
outfile_potato = "PSGC_gff_intron.csv"
intron_statistics_easy(inputfile_potato,outfile_potato)
