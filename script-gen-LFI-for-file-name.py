def generate_paths_from_user_input_and_save_to_file(output_file_path):
    print("Enter file names (type 'DONE' when finished):")
    file_names = []
    while True:
        line = input()
        if line.strip().upper() == 'DONE':  # End input on 'DONE'
            break
        file_names.append(line.strip())

    with open(output_file_path, 'w') as file:  # Open file for writing
        for file_name in file_names:
            # Generate each line with increasing "../" prefixes
            for i in range(9):  # Including the original file and 8 more levels
                file.write(f"{'../' * i}{file_name}\n")  # Write to file

# Specify the output file path
output_file_path = 'output.txt'  # You can change this to your desired path

# Execute the function to get user input and save the paths to a file
generate_paths_from_user_input_and_save_to_file(output_file_path)
