import psutil             # psutil (python system and process utilities) is a cross-platform library for retrieving information on running processes and system utilization


def ProcessDisplay():
    listprocess=[];
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username']);
            pinfo['vms']=proc.memory_info().vms/(1024*1024)
            listprocess.append(pinfo);

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass;

    return listprocess;

def main():
    print("Process and Memory Monitor Basic");

    listprocess= ProcessDisplay();

    for element in listprocess:
        print(element);

if __name__=="__main__":
    main();