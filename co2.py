##20ilmb03 _ Gokul _ Assignment 1 _ CO2 lattice

print("Hi! Welcome to the CO2 cubical lattice generator.\n Make sure the number of molecules in the lattice is a perfect cube. For example: 125, 1000 etc..\n Have fun!\n")
output = str(input("Enter the output file name of your choice : "))
numb = int(input("Enter the number of molecules needed in the lattice : "))
x_co = float(input("Enter the x coordinate of the carbon atom of your first molecule : "))
y_co = float(input("Enter the y coordinate of the carbon atom of your first molecule : "))
z_co = float(input("Enter the z coordinate of the carbon atom of your first molecule : "))

print("Please wait while your lattice is getting cooked...")


'''------The function------'''
def lattice_maker(output_file_name, number_of_molecules, x_coordinate, y_coordinate, z_coordinate):
    ic_x_c=float(x_coordinate)
    ic_y_c=float(y_coordinate)
    ic_z_c=float(z_coordinate)
    c_x_c=ic_x_c
    c_y_c=ic_y_c
    c_z_c=ic_z_c
    
    number_of_atoms = 3*number_of_molecules
    number = int(number_of_molecules**(1/3))
    with open(f"{output_file_name}.xyz", "w") as file:
        file.write(f"{number_of_atoms}\n\n")
        for i in range (0,number+1):
            c_y_c=ic_y_c
            
            for j in range (0,number+1):
                c_z_c=ic_z_c
                
                for k in range (0,number+1):
                    o1_x_c=c_x_c+1.6
                    o1_y_c=c_y_c
                    o1_z_c=c_z_c
                    o2_x_c=c_x_c-1.6
                    o2_y_c=c_y_c
                    o2_z_c=c_z_c
                    file.write(f"C {c_x_c} {c_y_c} {c_z_c}\n")
                    file.write(f"O {o1_x_c} {o1_y_c} {o1_z_c}\n")
                    file.write(f"O {o2_x_c} {o2_y_c} {o2_z_c}\n")
                    c_z_c+=4.0
                c_y_c+=4.0
            c_x_c+=6.0

'''--------Function Ends Here--------'''


lattice_maker(output,numb,x_co,y_co,z_co)


print(f"Your output file is saved in the current directory as {output}.xyz")

qu = input("Do you want to open this file in VMD?? (y/n)")
if qu == "y" or qu == "yes":
    print(f"\n\n\nTrying to open the file in VMD for you...please be patient...\n\n\n")

    import subprocess
    file_path = f"./{output}.xyz"
    try:
        subprocess.run(['vmd', file_path])
    except FileNotFoundError:
        print("VMD executable not found. Make sure VMD is installed and in your system's PATH.")

