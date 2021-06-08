import re
file_obj = open("data.txt",'r')
outfile_obj = open("data_result.txt",'w')

h_max = 0
w_max = 0
h_min = 2
w_min = 200
total = 0
count = 0
for line in file_obj:
    line_strip = line.strip()
#    print(line_strip)
    height_to_find = r"\b\d\.\d\d"
    weight_to_find = r"\b\d\d\.\d\d"
    h_pattern = re.compile(height_to_find)
    w_pattern = re.compile(weight_to_find)
    h_results = h_pattern.findall(line_strip)
    for result in h_results:
        rs_float = float(result)
        if h_max < rs_float:
            h_max = rs_float
        if h_min > rs_float:
            h_min = rs_float
        total = total + rs_float
        count += 1
    outfile_obj.write(line)
print(total)
print(count)
print("Max height: ", h_max)
print("Min height: ", h_min)
print("Average: " , total/count)

outfile_obj.write('\n\n' + "Max height: " + str(h_max) + '\n')
outfile_obj.write("Min height: " + str(h_min) + '\n')
outfile_obj.write("Avg height: " + str(total/count) + '\n')

file_obj.close()
outfile_obj.close()


