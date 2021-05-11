import sys
import adsmh.impute.missforest_impute as missingforest_impute


def run():
    """
    Helper scripts for notebooks.
    """
    args = sys.argv
    if not len(args) == 4:
        print("\nPlease specify task, method and argument:\
            #    \n>  adsmh [task] [method] [arg]")
        return
    task, method, arg = args[1], args[2], int(args[3])
    if task == "impute":
        if method == "missforest":
            missingforest_impute.impute(arg)
        else:
            print("Unrecognised method: valid methods are [missforest].")
    else:
        print("Unrecognised task: valid tasks are [impute].")