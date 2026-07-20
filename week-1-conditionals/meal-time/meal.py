def main():
    x = input("What time is it? ");
    time = convert(x);
    if(7<=time<=7.5):
        print("breakfast time");
    elif(18<=time<=19):
        print("dinner time");


def convert(time):
    hour,min = time.split(":");
    hour, min = float(hour),float(min);
    actual_time=hour+(min/60);
    return actual_time


if __name__ == "__main__":
    main()