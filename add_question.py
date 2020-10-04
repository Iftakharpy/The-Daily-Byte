
import os
import sys
import logging

log_format = "%(asctime)s | %(levelname)s | %(message)s"

logging.basicConfig(filemode = "a",
                    filename = "add_question_logs.log",
                    format = log_format
                    )


def get_last_serial_num() -> int:
    INVALID_MSG = "Invalid format of directory name"
    
    max_serial_num = 0
    #getting the max serial number
    for dir_name in os.listdir(os.getcwd()):
        # checking serial nums of the dir_name
        if os.path.isdir(dir_name) and "." in dir_name:
            try:
                num = int(dir_name.split('.',1)[0])
            except IndentationError:
                logging.warning(f"{INVALID_MSG} \"{dir_name}\"")
                continue
            except ValueError:
                logging.warning(f"{INVALID_MSG} \"{dir_name}\"")
                continue

            # seting greater number as max_serial_num
            max_serial_num = max(max_serial_num, num)

    return max_serial_num


def create_files(question_name: str) -> None:
    name = question_name.lower().replace(" ", "_")

    question_file_name = f"{name}_question.md"
    test_file_name = f"{name}_test.py"
    solution_file_name = f"{name}.py"

    with open(question_file_name,"w") as f:
        f.write(f"# {question_name}\n\n")
        pass
    with open(solution_file_name,"w") as f:
        pass
    with open(test_file_name,"w") as f:
        pass


def make_question_dir(directory_name: str) -> None:
    # getting the largest serial number
    serial = get_last_serial_num() + 1
    # formatting the number to 3 digit 
    serial = f"{serial}".rjust(3,"0")

    #preparing the directory_name with serial number
    dir_name = f"{serial}. {directory_name}"

    path = os.path.join(os.getcwd(),dir_name)
    os.makedirs(path)
    os.chdir(path)
    return path






HELP_TEXT = """
format: python3 script_name.py [option] [vlaue]

options:
    -q or --question ["question name"]
        1. Create directory with the question name.
        2. Create files for the question and exit.
    
    -h or --help
        show this text and exit
"""

def main(string: str):
    make_question_dir(string)
    create_files(string)

def run():
    if __name__=="__main__" and len(sys.argv)==1:
        inpt = input("Enter question title: ")
        main(inpt)
    else:
        args = sys.argv[1:]
        lookup = set(args)
        if "-h" in lookup or "--help" in lookup:
            print(HELP_TEXT)
            exit(0)
        
        question = ""
        for index,arg in enumerate(args):
            if arg == "-q" or arg == "--question":
                try:
                    question = args[index+1]
                except IndexError:
                    print(f"provide value for {arg}")
                break
        else:
            print("You have passed invalid argument")
            print(HELP_TEXT)
            exit(0)
        
        if question.strip() == "":
            print("Invalid question name")
            exit(0)
        else:
            main(question)


run()