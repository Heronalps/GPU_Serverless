import os, shlex, time, sys, json
from subprocess import Popen, PIPE

# traverse UECFOOD100

root_dir = './UECFOOD100'
TOTAL = 10

# run python3 filter.py <src> ./UECFOOD100_filter/<dest>
start = time.time()
count = 1
for dir_name, _subdir_list, file_list in os.walk(root_dir):
    for file_name in file_list:
        if file_name.endswith('.jpg'):
            src_file_path = "{0}/{1}".format(dir_name, file_name)
            dest_file_path = src_file_path.replace("UECFOOD100", "UECFOOD100_filter")
            command_line = "python3 filter.py {0} {1} -bf".format(src_file_path, dest_file_path)
            proc = Popen(shlex.split(command_line), stdout=PIPE)
            output, _err = proc.communicate()
            print ("=====")
            print ("Add filter to No.{} photo".format(count))
            print (output.decode('utf-8'))
            count = count + 1
        if count > TOTAL:
            break

print ("The UECFOOD100 processing time is {} seconds".format(time.time() - start))