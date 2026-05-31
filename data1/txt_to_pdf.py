from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

txt_folder = r"C:\Users\ARTH\Desktop\Projects\College_RAG_Chatbot\data"

styles = getSampleStyleSheet()

for txt_file in Path(txt_folder).glob("*.txt"):
    pdf_file = txt_file.with_suffix(".pdf")

    with open(txt_file, "r", encoding="utf-8") as f:
        content = f.read()

    doc = SimpleDocTemplate(str(pdf_file))
    story = []

    for line in content.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["BodyText"]))
            story.append(Spacer(1, 4))

    doc.build(story)

    print(f"Created: {pdf_file.name}")

print("All PDF files generated successfully!")