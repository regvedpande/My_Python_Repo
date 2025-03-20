def process_file(input_filename, output_filename):
    """
    Reads lines from an input file, processes them (e.g., converts to uppercase),
    and writes the processed lines to an output file.

    Args:
        input_filename: The name of the input file.
        output_filename: The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                processed_line = line.upper()  # Example: convert to uppercase
                outfile.write(processed_line)
        print(f"File processing completed. Output written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file = "input.txt"
output_file = "output.txt"

# Create a sample input file (if it doesn't exist)
with open(input_file, 'w') as f:
    f.write("This is a sample line.\n")
    f.write("Another line for processing.\n")
    f.write("and a third line.\n")

process_file(input_file, output_file)

#demonstrate reading the new file.
try:
    with open(output_file, 'r') as f:
        print("\nContents of output file:")
        print(f.read())
except FileNotFoundError:
    print(f"Error: output file '{output_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
