from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_master_report(name, github_info, resume_feedback, gap_analysis, weekly_plan, output_path="Master_Career_Report.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    x = 50
    y = height - 50
    line_height = 16
    max_line_width = 90

    def write_block(title, content):
        nonlocal y
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, title)
        y -= 20
        c.setFont("Helvetica", 10)
        for line in content.split('\n'):
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
        y -= 20

    # Header
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, f"🔮 SkillMorph AI - Career Coaching Report")
    y -= 30
    c.setFont("Helvetica", 11)
    c.drawString(x, y, f"👤 Name: {name}")
    y -= line_height
    c.drawString(x, y, f"📁 GitHub Repos: {github_info['total_repos']}")
    y -= line_height
    c.drawString(x, y, f"💻 GitHub Languages: {', '.join(github_info['languages'])}")
    y -= 30

    # Sections
    write_block("📄 Resume Review", resume_feedback)
    write_block("📊 Skill Gap Analysis", gap_analysis)
    write_block("🗓️ Weekly Upskilling Plan", weekly_plan)

    c.save()
    return output_path
