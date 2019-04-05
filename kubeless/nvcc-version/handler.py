from subprocess import Popen, PIPE, TimeoutExpired

def handler(event, context):
  proc = Popen(["nvcc", "--version"], stdout=PIPE, shell=True)
  try:
    output = proc.communicate(timeout=15)[0].decode("utf-8")
  except TimeoutExpired:
    proc.kill()
  return output