##20ilmb03 _ Gokul _ Assignment 1 _ c atoms

output = str(input("Enter the output file name of your choice : "))
numb = int(input("Enter the number of atoms needed in the lattice : "))
x_co = float(input("Enter the x coordinate of your first atom : "))
y_co = float(input("Enter the y coordinate of your first atom : "))
z_co = float(input("Enter the z coordinate of your first atom : "))

print("Please wait...")

def lattice_maker(output_file_name, number, x_co, y_co, z_co):
  x = x_co
  with open(f"{output_file_name}.xyz", "w") as file:
    file.write(f"{number}\n\n")
    for i in range (0,number):
      file.write(f"C {x} {y_co} {z_co}\n")
      x+=3.0

lattice_maker(output,numb,x_co,y_co,z_co)



print(f"Your output file is saved in the current directory as {output}.xyz")

qu = input("Make sure you change the drawing method to CPK, inorder to see the atoms. Do you want me to open this file in VMD for u? (y/n)")
if qu == "y" or qu == "yes":
    print(f"\n\n\nTrying to open the file in VMD for you...please be patient...\n\n\n")

    import subprocess
    file_path = f"./{output}.xyz"
    try:
        subprocess.run(['vmd', file_path])
    except FileNotFoundError:
        print("VMD executable not found. Make sure VMD is installed and in your system's PATH.")
