# Pass 1 - Creating MNT, MDT, and ALA

input_file = 'input2.txt'

# Open and read the input file
fp = open(input_file, 'r')
data = fp.readline()

line_no = 1  # Counter for line number in input file
mntc = 1  # Counter for MNT index
mdtc = 1  # Counter for MDT index

# Open/create other files
fp_mn = open('mnt_table.txt', 'w')  # Macro Name Table
fp_md = open('mdt_table.txt', 'w')  # Macro Definition Table
fp_ala = open('ala_table.txt', 'w')  # Argument List Array
fp_out = open('output_file1.txt', 'w')  # Output file for non-macro code

while data != '':  # Loop through each line of the input file
    elements = data.split()

    # If the line contains a macro definition
    if len(elements) > 1 and elements[1] == 'MACRO':
        data = fp.readline()  # Read next line for the macro definition
        line_no += 1

        # Store macro arguments
        macro_arguments = data[data.find('&'):].rstrip().split(',')
        argument_indexes = {arg.strip(): i + 1 for i, arg in enumerate(macro_arguments)}

        # Write to MNT (Macro Name Table)
        fp_mn.write('%d\t%s\t%d\n' % (mntc, data[data.find('-'):].rstrip(), mdtc))

        # Write to MDT and ALA
        fp_md.write('%d\t%s\t\n' % (mdtc, data[data.find('-'):].rstrip()))  # Write macro name in MDT
        for arg in argument_indexes:
            fp_ala.write('%d\t%s\n' % (argument_indexes[arg], arg))  # Write argument index to ALA

        mntc += 1
        mdtc += 1

        # Read next line from input before executing while loop
        data = fp.readline()
        line_no += 1

        # Process each line of the macro definition
        while elements[1] != 'MEND':  # While it is inside the MACRO block
            start = data.find('-')
            end = data.find(',')

            string_to_write = '%d\t%s' % (mdtc, data[start:end + 1].rstrip())

            if '&' in data[end:]:
                arg_name = data[end + 1:].strip()
                arg_index = argument_indexes.get(arg_name, 0)  # Default to 0 if not found
                string_to_write += '#%d\n' % arg_index
            else:
                string_to_write += data[end + 1:].split('&')[-1]

            fp_md.write(string_to_write)  # Write to MDT
            mdtc += 1

            # Read next line in input
            data = fp.readline()
            line_no += 1
            elements = data.split()

        if 'MEND' in data:  # Macro END detected
            fp_md.write('%d\t%s' % (mdtc, data))  # Write MEND to MDT
            mdtc += 1
            data = fp.readline()  # Read next line in input
            line_no += 1
    else:
        fp_out.write(data)  # Write non-macro lines to the output file
        data = fp.readline()
        line_no += 1

# Close all files after processing
fp.close()
fp_mn.close()
fp_md.close()
fp_ala.close()
fp_out.close()
