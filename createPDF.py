from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


def write_newspaper_to_pdf(label, content):
    filename = f"{label}.pdf"
    doc = canvas.Canvas(filename, pagesize=letter)
    textobject = doc.beginText()
    textobject.setTextOrigin(inch, letter[1] - inch)
    textobject.setFont("Helvetica-Bold", 14)

    # Split the label into multiple lines if needed
    label_lines = []
    words = label.split(' ')
    current_line = ''
    for word in words:
        if doc.stringWidth(current_line + word) < letter[0] - 2*inch:
            current_line += word + ' '
        else:
            label_lines.append(current_line.strip())
            current_line = word + ' '
    label_lines.append(current_line.strip())

    for line in label_lines:
        textobject.textLine(line)

    # Move the cursor down by half an inch to make space for the content
    textobject.moveCursor(0, -0.5 * inch)

    doc.drawText(textobject)
    textobject = doc.beginText()
    textobject.setTextOrigin(inch, letter[1] - 2 * inch)
    textobject.setFont("Helvetica", 12)

    lines = []
    for line in content:
        words = line.split(' ')
        current_line = ''
        for word in words:
            if doc.stringWidth(current_line + word) < letter[0] - 2*inch:
                current_line += word + ' '
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)
    for line in lines:
        if textobject.getY() <= 0.5*inch:
            doc.drawText(textobject)
            doc.showPage()
            textobject = doc.beginText()
            textobject.setTextOrigin(inch, letter[1] - 2 * inch)
            textobject.setFont("Helvetica", 12)
            textobject.moveCursor(doc.stringWidth(line), 0)
        textobject.textLine(line)

    doc.drawText(textobject)
    doc.save()


# # Example usage
# label = "In Deutschland gibt es viele schöne Städte. Berlin ist die Hauptstadt und hat eine reiche Geschichte."
# content = [
#     "Breaking news: Local cat saves owner from burning house",
#     "New study finds coffee may help prevent certain diseases",
#     "Sports: High school football team wins state championship",
#     "Opinion: Why we should invest in renewable energy",
#     "Arts and culture: Local artist debuts new exhibit at museum",
#     "In Deutschland gibt es viele schöne Städte. Berlin ist die Hauptstadt und hat eine reiche Geschichte. München ist bekannt für sein Oktoberfest und seine bayerische Kultur. Hamburg ist ein wichtiger Hafenstadt und hat viele Museen und Theater.",
# ]
# write_newspaper_to_pdf(label, content)
