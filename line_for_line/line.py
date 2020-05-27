# This program prints every line of a given .txt file
import sys
import argparse # For adding optional arguments

def main():
  
    # Check if we got the right amount of CLI arguments
    if len(sys.argv) < 2:
        print("Incorrect number of command line arguments!")
        print("Usage: python line.py FILE.txt -optional arguments")
        sys.exit(1)
    
    # Check if given file is a .txt file
    if not sys.argv[1].endswith(".txt"):
        print("The given file is not a txt. file !")
        sys.exit(1)

    # Optional Arguments
    # TODO
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="Print text in all uppercase", action="store_true")
    args = parser.parse_args()

    # Open file
    file = open(sys.argv[1])

    # Print every line in the given file
    if args.upper:
        for lines in file:
            print(lines.upper())
    else:
        for lines in file:
            print(lines)
    # Close file
    file.close

if __name__ == "__main__":
    main()