from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_pdf(report_text, name, email, github_info, output_path="skill_report.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    x = 50
    y = height - 50
    line_height = 16
    max_line_width = 90

    # Header
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.darkblue)
    c.drawString(x, y, "🔍 SkillMorph AI Report")
    y -= 30

    # User Info Section
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    c.drawString(x, y, f"👤 Name: {name}")
    y -= line_height
    c.drawString(x, y, f"📧 Email: {email}")
    y -= line_height
    c.drawString(x, y, f"📁 GitHub Repositories: {github_info['total_repos']}")
    y -= line_height
    c.drawString(x, y, f"💻 Languages Used: {', '.join(github_info['languages'])}")
    y -= 30

    # Report Section
    c.setFont("Helvetica", 10)
    for line in report_text.split('\n'):
        while len(line) > max_line_width:
            c.drawString(x, y, line[:max_line_width])
            line = line[max_line_width:]
            y -= line_height
            if y < 50:
                c.showPage()
                y = height - 50
        c.drawString(x, y, line)
        y -= line_height
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    return output_path
