from subprocess import Popen, PIPE, TimeoutExpired

# def handler(event, context):
#   gpu_info = subprocess.run(['nvidia-smi'])
#   return gpu_info

proc = Popen(['nvidia-smi'], stdout=PIPE)
try:
  output = proc.communicate(timeout=15)
except TimeoutExpired:
  proc.kill()
print (output)
