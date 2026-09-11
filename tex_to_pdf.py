import subprocess

TEX_FILE = "cover_letter_template.tex"

def compile_tex(company_name):
    """Compile cover_letter_template.tex to PDF using pdflatex."""
    for _ in range(2):  # run twice to resolve references
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", TEX_FILE],
            capture_output=True,
            text=True,
        )

    if result.returncode != 0:
        print("Compilation failed. Log output:")
        print(result.stdout[-2000:])
        return None

    pdf_path = f"{company_name}_" + TEX_FILE.replace(".tex", ".pdf")
    print(f"Compiled: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    compile_tex("Test")