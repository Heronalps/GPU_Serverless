import os, shlex
from subprocess import Popen, PIPE

# traverse UECFOOD100

root_dir = './UECFOOD100'

# run python3 filter.py <src> ./UECFOOD100_filter/<dest>

for dir_name, _subdir_list, file_list in os.walk(root_dir):
    for file_name in file_list:
        src_file_path = "{0}/{1}".format(dir_name, file_name)
        dest_file_path = src_file_path.replace("UECFOOD100", "UECFOOD100_blur")
        command_line = "python3 filter.py {0} {1} -bf".format(src_file_path, dest_file_path)
        proc = Popen(shlex.split(command_line), stdout=PIPE)
        output, _err = proc.communicate()
        print ("=====")
        print (output)
