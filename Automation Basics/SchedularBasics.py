import schedule
import time
import datetime

def fun_Minute():
    print("current time is ");
    print(datetime.datetime.now());
    print("scheduler executed after Minute");

def fun_Hour():
    print("current time is ");
    print(datetime.datetime.now());
    print("scheduler executed after Hour");

def fun_Day():
    print("current time is ");
    print(datetime.datetime.now());
    print("scheduler executed after Day");

def fun_Afternoon():
    print("current time is ");
    print(datetime.datetime.now());
    print("scheduler executed after ");

def main():
    print("Python automation: Scheduler");

    print(datetime.datetime.now());

    schedule.every(1).minutes.do(fun_Minute);

    schedule.every().hour.do(fun_Hour);

    schedule.every().day.at("00:00").do(fun_Afternoon);

    schedule.every().sunday.do(fun_Day);

    schedule.every().saturday.at("18:30").do(fun_Day);

    while True:
        schedule.run_pending();
        time.sleep(1);

if __name__=="__main__":
    main();