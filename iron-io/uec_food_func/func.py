import os, shlex, time, sys, json
from subprocess import Popen, PIPE

def handler():
    root_dir = './UECFOOD100'
    TOTAL = 10
    count = 1
    # traverse UECFOOD100
    for dir_name, _subdir_list, file_list in os.walk(root_dir):
        for file_name in file_list:
            if file_name.endswith('.jpg'):
                src_file_path = "{0}/{1}".format(dir_name, file_name)
                dest_file_path = src_file_path.replace("UECFOOD100", "UECFOOD100_filter")
                command_line = "python3 filter.py {0} {1} -bf".format(src_file_path, dest_file_path)
                proc = Popen(shlex.split(command_line), stdout=PIPE)
                
                # run python3 filter.py <src> ./UECFOOD100_filter/<dest>
                output, _err = proc.communicate()
                print ("=====")
                print ("Add filter to No.{0} {1} photo".format(count, src_file_path))
                print (output.decode('utf-8'))
                count = count + 1
            if count > TOTAL:
                # Break nested loop
                return

if __name__ == "__main__":
    start = time.time()
    handler()
    print ("The UECFOOD100 processing time is {} seconds".format(time.time() - start))