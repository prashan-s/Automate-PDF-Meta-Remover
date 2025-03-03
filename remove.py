import fitz  # PyMuPDF

# Load the PDF
input_file = "input.pdf"
output_file = "output_no_metadata.pdf"

doc = fitz.open(input_file)

# Clear metadata
doc.set_metadata({})

# Save the new file without metadata
doc.save(output_file)

print(f"Metadata removed and saved to {output_file}")