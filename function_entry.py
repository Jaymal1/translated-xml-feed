# function_entry.py
import main

def run_script(request):
    main.run_script()  # or whatever function runs your script
    return "Script executed successfully", 200
