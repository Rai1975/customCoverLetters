import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

TEX_FILE = "cover_letter_template.tex"
OUTPUT_DIR = os.path.join(os.getcwd(), "pdf_out")


def generate_cover_letter(
        company_name,
        title,
        body,
        address=None,
        phone_number=None,
        email=None,
        first_name=None,
        last_name=None,
    ):

    address = os.getenv('ADDRESS') if address is None else address
    phone_number = os.getenv('PHONE_NUMBER') if phone_number is None else phone_number
    email = os.getenv('EMAIL') if email is None else email
    first_name = os.getenv('FIRST_NAME') if first_name is None else first_name
    last_name = os.getenv('LAST_NAME') if last_name is None else last_name

    with open(os.path.join(os.getcwd(), TEX_FILE), "r") as f:
        filestring = f.read()

    filestring = filestring.replace("FIRSTNAME", first_name)
    filestring = filestring.replace("LASTNAME", last_name)
    filestring = filestring.replace("ADDRESS", address)
    filestring = filestring.replace("PHONENUMBER", phone_number)
    filestring = filestring.replace("EMAIL", email)
    filestring = filestring.replace("TITLE", title)
    filestring = filestring.replace("COMPANYNAME", company_name)
    filestring = filestring.replace("CONTENTBODY", body)

    return filestring


def compile_tex(filestring, company_name):
    """Write the filled-in tex string to its own file, compile it, then
    clean up everything except the final PDF."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    base_name = f"{company_name}_cover_letter"
    output_tex = os.path.join(OUTPUT_DIR, f"{base_name}.tex")

    with open(output_tex, "w") as f:
        f.write(filestring)

    for _ in range(2):  # run twice to resolve references
        result = subprocess.run(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-output-directory", OUTPUT_DIR,
                output_tex,
            ],
            capture_output=True,
            text=True,
        )

    if result.returncode != 0:
        print("Compilation failed. Log output:")
        print(result.stdout[-2000:])
        return None

    pdf_path = os.path.join(OUTPUT_DIR, f"{base_name}.pdf")

    # Clean up everything except the PDF
    for ext in (".tex", ".aux", ".log", ".out"):
        stray_file = os.path.join(OUTPUT_DIR, f"{base_name}{ext}")
        if os.path.exists(stray_file):
            os.remove(stray_file)

    print(f"Compiled: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    filled = generate_cover_letter(
        company_name="Test",
        title="Software Engineer",
        body="Example paragraph content here.",
    )
    compile_tex(filled, "Test")