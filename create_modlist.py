import os
import sys

def handle_error(message):
    print(message)
    input("\nPress Enter to exit...")
    sys.exit(1)

def generate_mod_list():
    base = os.path.dirname(os.path.abspath(__file__))
    p_dir, f_dir = os.path.join(base, "mod_previews"), os.path.join(base, "mod_files")
    
    if not (os.path.exists(p_dir) and os.path.exists(f_dir)):
        handle_error("Error: Directories missing.")
        
    p_files = []
    for f in os.listdir(p_dir):
        if os.path.isfile(os.path.join(p_dir, f)):
            name, ext = os.path.splitext(f)
            if ext.lower() != '.sww':
                handle_error(f"Error: Invalid extension '{ext}' for file '{f}' in mod_previews. Expected '.sww'.")
            p_files.append(f)
            
    f_files = {}
    for f in os.listdir(f_dir):
        if os.path.isfile(os.path.join(f_dir, f)):
            name, ext = os.path.splitext(f)
            if ext.lower() != '.mww':
                handle_error(f"Error: Invalid extension '{ext}' for file '{f}' in mod_files. Expected '.mww'.")
            f_files[name] = f
    
    out = []
    for pf in p_files:
        name, _ = os.path.splitext(pf)
        if name in f_files:
            out.append(pf)
        else:
            handle_error(f"Error: No match for '{pf}' in mod_files.")
            
    with open(os.path.join(base, "modlist.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    
    print("Success: modlist.txt generated successfully!")

if __name__ == "__main__":
    generate_mod_list()
