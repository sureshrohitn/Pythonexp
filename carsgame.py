import datetime

command = ""
started = False
starttime = 0

endtime = 0

score = 0
while command.upper() != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            starttime = datetime.datetime.now()
            print("Car Already Started,wake up!!!")
        else:
            started = True
            print("Car Started.......")

    elif command == "stop":
        if not started:
            endtime = datetime.datetime.now()
            print("Car Already stoped, Now what are you doing here!!!!!")
        else:
            started = False
            print("Car stoped........")
    elif command == "help":
        print("start ->  to start the Car")
        print("Stop ->  to stop the Car")
        print("quit ->  to quit the Car")
    elif command == "quit":
        score = (endtime - starttime) * 0.01
        print(score)
        break
    else:
        print("enter valid command, for more click help")
