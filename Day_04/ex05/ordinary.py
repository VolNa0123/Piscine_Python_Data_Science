import sys
import psutil

def ordinary():
    with open(sys.argv[1]) as file:
        for line in file:
            return line

def main():
    for _ in ordinary():
        pass
    mem = psutil.Process().memory_info().vms/(10**9)
    cpu = psutil.Process().cpu_times()
    print(f'Peak Memory Usage = {mem} Gb')
    print(f'User Time + System Time = {cpu.user + cpu.system}s')

if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print("ERROR")

# psutil: https://pythobyte.com/psutil-module-c2868b8b/