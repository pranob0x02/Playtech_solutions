import sys
import psutil as psu

input = sys.argv[1]  # Takes input from command line


def cpu_metrics(cpu):  # function to get cpu metrics
    for name in cpu._fields:
        value = getattr(cpu, name)
        print(name.capitalize(), value)


def memory_metrics(vm):  # function to get memory metrics
    print("---------------------------------------")
    for name in vm._fields:
        value = getattr(vm, name)
        print(name.capitalize(), value)


if input == "cpu":
    print(f"cores:  {psu.cpu_count()}")
    print(f"load average: {psu.getloadavg()}")

    print("\n")
    print("CPU times:")
    cpu_metrics(psu.cpu_times())

    print("\n")
    print("CPU frequency:")
    cpu_metrics(psu.cpu_freq())

    print("\n")
    print("CPU statistics:")
    cpu_metrics(psu.cpu_stats())

elif input == "mem":
    print("virtual memory")
    memory_metrics(psu.virtual_memory())
    print("\n")

    print("swap memory")
    memory_metrics(psu.swap_memory())


else:
    print("No such option")
