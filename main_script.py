import subprocess

def main():
    ovs_count = input("Please enter the number of intermediatoy OVS switch...")
    if int(ovs_count) == 1:
        print("single ovs")
        subprocess.run(["python3", "automate_start1.py"])
    else:
        print("Two OVS")
        subprocess.run(["python3", "automate_start2.py"])

if __name__ == "__main__":
    main()
