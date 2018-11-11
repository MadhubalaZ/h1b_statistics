# -*- coding: utf-8 -*-
"""
Created on Fri Nov 09 09:10:42 2018

@author: madhu
"""
import sys

if len(sys.argv)!=4:
    print("Incorrect number of arguments")
    exit()
input_filename=sys.argv[1]
output_occupation_filename=sys.argv[2]
output_state_filename=sys.argv[3]

#define a fuction that will look for the required columns from the data and return their indexes
def get_index(f):
    line=f.readline()
    header=line.split(";")
    state_index=0
    status_index=0
    occupation_index=0
    for i in range(0,len(header)):
        if 'WORK' in header[i] and 'STATE' in header[i]:
            state_index=i
        if 'STATUS' in header[i]:
            status_index=i
        if 'SOC' in header[i] and 'NAME' in header[i]:
            occupation_index=i
    return state_index,status_index,occupation_index

#define a function that will sort a dictionary by its values in descending order
def sort(dict):
    sorted_dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_dict

#define a function that will calculate percentage for the input list
def percentage(List,total_certified):
    percentages=[]
    for value in range(0,len(List)):
        percent = round(List[value][1]/float(total_certified)*100,1)
        percentages.append(percent)
    return percentages

#define a function that will collect, count, sort and return data from the above collected indexes        
def get_top_10(f):
    
    total_certified=0
    state_count={}
    occupation_count={}
    
    lines=f.readlines()
    for line in lines:
        data=line.split(";")
        status = data[status_index].strip().upper()
        if status=="CERTIFIED":
            total_certified=total_certified+1
            state = data[state_index].strip().upper()
            occupation = data[occupation_index].strip().upper()
            occupation=occupation.replace("\"","")
            if state in state_count:
                state_count[state]=state_count[state]+1
            else:
                state_count[state]=1
            if occupation in occupation_count:
                occupation_count[occupation]=occupation_count[occupation]+1
            else:
                occupation_count[occupation]=1
    sorted_occupation = sort(occupation_count)[:10]
    sorted_state = sort(state_count)[:10]   
    return sorted_occupation,sorted_state,total_certified

#define a function that will write the output files , for the given lists
def write_to_files(List,percentage, fieldnames,output_filename):
    with open(output_filename, "w") as f:
        f.write(';'.join('%s' % name for name in fieldnames))
        f.write('\n')
        row=1
        for item in range(0,len(List)):
            f.write("%s;" % List[item][0])
            f.write("%s;" % List[item][1])
            f.write("%s" % percentage[item])
            f.write("%")
            f.write("\n")
            row+=1   

       
with open(input_filename,'r') as f:
    
    print "Running program to generate top 10 states and occupations for certified H1B"
    state_index, status_index, occupation_index = get_index(f)
    sorted_occupation,sorted_state,total_certified= get_top_10(f)
    
    percent_occupation=percentage(sorted_occupation,total_certified)
    percent_state=percentage(sorted_state,total_certified)
    
    fieldnames_occupation = ["TOP_OCCUPATIONS","NUMBER_CERTIFIED_APPLICATIONS","PERCENTAGE"]
    fieldnames_state = ["TOP_STATES","NUMBER_CERTIFIED_APPLICATIONS","PERCENTAGE"]
    
    write_to_files(sorted_occupation,percent_occupation,fieldnames_occupation,output_occupation_filename)
    write_to_files(sorted_state,percent_state,fieldnames_state,output_state_filename)
    
    print "Finished generating top 10 occupations and states."
    print "Check output folder to view output .txt files."
