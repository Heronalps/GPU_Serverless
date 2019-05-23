import math
import pandas as pd

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def q_99_boundary(data):
    sample_size = len(data)
    total = 0
    data = sorted(data)
    result = []
    for i in range(sample_size + 1):
        total += nCr(sample_size, sample_size - i)*(0.99**(sample_size - i))*((1-0.99)**i)
        if total >= 0.025:
            print ("total : {0}".format(total))
            print ("U : {0}".format(i))
            print ("Uth largest number : {0}".format(data[i]))
            result.append(data[i])
        if total >= 0.975:
            print ("total : {0}".format(total))
            print ("L : {0}".format(i))
            print ("Lth largest number : {0}".format(data[i]))
            result.append(data[i])
            break

    return result

if __name__ == "__main__":
    wait_df = pd.read_csv('./wait_time_seconds.csv')
    
    # non-zero sample in GPU 8 time series
    data = wait_df[wait_df['8']!=0]['8']
    q_99_boundary(data)