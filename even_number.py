import datetime
def even_number(numbers):
    for x in latest_numbers:
        if x % 2 == 0:
            print(x)

old_numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617,865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 32615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,894, 767, 553, 81, 379, 843,831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
new_numbers= list(old_numbers)[0]
int_new_numbers = new_numbers['sequence']

latest_numbers= [int(s) for s in int_new_numbers.split(',')]




def main():
    even_number(latest_numbers)


if __name__ == "__main__":
    now = datetime.datetime.now()
    print("Current Date and Time is :")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    main()
