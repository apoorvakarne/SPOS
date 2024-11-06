# Read the MNT (Macro Name Table)
mnt = {}
with open('mnt_table.txt', 'r') as fp_mn:
    for line in fp_mn:
        elements = line.split()
        
        # Ensure the line has enough elements
        if len(elements) >= 5:
            mnt_index = int(elements[0])  # MNT index (integer)
            macro_name = elements[2]      # Macro name (string)
            mdt_index = int(elements[4])  # MDT index (integer)

            # Store macro details in MNT dictionary
            mnt[macro_name] = {
                'mnt_index': mnt_index,
                'mdt_index': mdt_index,
                'arguments': elements[3]  # Arguments part (e.g., '&X,&Y,&Z')
            }

# Read the MDT (Macro Definition Table)
mdt = {}
with open('mdt_table.txt', 'r') as fp_md:
    for line in fp_md:
        elements = line.split('\t')
        if len(elements) > 1:
            mdt_index = int(elements[0])  # MDT index (integer)
            mdt[mdt_index] = elements[1].strip()  # Store macro definition

# Read the ALA (Argument List Array)
ala = {}
with open('ala_table.txt', 'r') as fp_ala:
    for line in fp_ala:
        elements = line.split()
        if len(elements) > 1:
            index = int(elements[0])
            argument = elements[1]
            ala[index] = argument  # Store argument name to index mapping

# Macro Expansion: Process input file and replace macros with their definitions
input_file = 'input2.txt'
output_file = 'expanded_output.txt'

with open(input_file, 'r') as fp_in, open(output_file, 'w') as fp_out:
    for line in fp_in:
        # Skip empty lines to avoid IndexError
        if not line.strip():
            continue
        
        elements = line.split()

        # Check if the line has at least one element
        if len(elements) > 0 and elements[0] in mnt:
            macro_name = elements[0]
            mdt_index = mnt[macro_name]['mdt_index']

            # Expand the macro using the MDT and ALA
            macro_definition = mdt[mdt_index]
            arguments = elements[1:]  # Get arguments passed in the macro call

            # Split the arguments in the format '&X,&Y,&Z' or similar
            macro_arguments = mnt[macro_name]['arguments'].split(',')

            # Replace the arguments in the macro definition using ALA
            for idx, arg in enumerate(arguments):
                if idx < len(macro_arguments):
                    argument_name = macro_arguments[idx]
                    # Get the argument index from ALA (map argument name to index)
                    argument_index = list(ala.keys())[list(ala.values()).index(argument_name)]
                    macro_definition = macro_definition.replace(argument_name, str(argument_index))

            # Write the expanded macro to the output file
            fp_out.write(macro_definition + '\n')
        else:
            # Write non-macro lines as they are
            fp_out.write(line)

print("Macro expansion completed. Check 'expanded_output.txt' for output.")
