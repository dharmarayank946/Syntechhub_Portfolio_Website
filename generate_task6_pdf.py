import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_pdf():
    pdf_path = r'd:\Projects\Veda\Task6_BMI_Calculator_Report.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.HexColor('#29463B'), spaceAfter=4)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=13, textColor=colors.HexColor('#6B7D76'), spaceAfter=12)
    h2_style = ParagraphStyle('SectionH2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=15, textColor=colors.HexColor('#5FAF92'), spaceBefore=10, spaceAfter=4)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#29463B'), spaceAfter=4)

    story = [
        Paragraph('VEDA Technology Internship — Task 6 Report', title_style),
        Paragraph('BMI Calculator Application Documentation', subtitle_style),
        HRFlowable(width='100%', thickness=1.5, color=colors.HexColor('#5FAF92'), spaceAfter=10),
        
        Paragraph('1. Project Overview', h2_style),
        Paragraph('This report details <b>Task 6 (BMI Calculator)</b> for the VEDA Technology Web Development Internship. The web application allows users to enter height (in cm) and weight (in kg), calculate their Body Mass Index (BMI), and categorize their result into Underweight, Normal Weight, Overweight, or Obese.', body_style),
        
        Paragraph('2. Technical Stack', h2_style),
        Table([
            [Paragraph('<b>Component</b>', body_style), Paragraph('<b>Technology Details</b>', body_style)],
            [Paragraph('HTML5', body_style), Paragraph('Semantic structure (&lt;header&gt;, &lt;main&gt;, &lt;section&gt;, &lt;form&gt;, &lt;label&gt;, &lt;input&gt;, &lt;button&gt;, &lt;footer&gt;)', body_style)],
            [Paragraph('CSS3', body_style), Paragraph('Custom Soft Mint &amp; White theme (--bg: #F3FAF7, --primary: #5FAF92, --light-accent: #DDF1E8, --border: #D5E8DF)', body_style)],
            [Paragraph('Vanilla JS', body_style), Paragraph('DOM selection, form submission, input validation rules, BMI formula, if/else categorization', body_style)]
        ], colWidths=[100, 430], style=[
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#DDF1E8')),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#A8D8C5')),
            ('PADDING', (0,0), (-1,-1), 5)
        ]),
        
        Paragraph('3. BMI Formula &amp; Categories', h2_style),
        Table([
            [Paragraph('<b>Formula</b>', body_style), Paragraph('<b>Range / Boundary</b>', body_style), Paragraph('<b>Category Output</b>', body_style)],
            [Paragraph('BMI = weight (kg) / height (m)&sup2;', body_style), Paragraph('Below 18.5', body_style), Paragraph('Underweight', body_style)],
            [Paragraph('Convert height from cm to meters', body_style), Paragraph('18.5 &ndash; 24.9', body_style), Paragraph('Normal Weight', body_style)],
            [Paragraph('Round output to 1 decimal place', body_style), Paragraph('25.0 &ndash; 29.9', body_style), Paragraph('Overweight', body_style)],
            [Paragraph('E.g. 70 kg &amp; 175 cm &rarr; 22.9', body_style), Paragraph('30.0 or above', body_style), Paragraph('Obese', body_style)],
        ], colWidths=[180, 150, 200], style=[
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#DDF1E8')),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#A8D8C5')),
            ('PADDING', (0,0), (-1,-1), 4)
        ]),

        Paragraph('4. Input Validation Rules', h2_style),
        Paragraph('&bull; <b>Empty Input Validation:</b> Displays <i>"Please enter your height and weight."</i>', body_style),
        Paragraph('&bull; <b>Non-Numeric Validation:</b> Displays <i>"Please enter valid numeric values."</i>', body_style),
        Paragraph('&bull; <b>Height Boundary (&le; 0):</b> Displays <i>"Height must be greater than 0."</i>', body_style),
        Paragraph('&bull; <b>Weight Boundary (&le; 0):</b> Displays <i>"Weight must be greater than 0."</i>', body_style),

        Paragraph('5. Verification &amp; Compliance Checklist', h2_style),
        Paragraph('&bull; Verified normal BMI (e.g., 70kg, 175cm &rarr; 22.9, Normal Weight)', body_style),
        Paragraph('&bull; Verified underweight (e.g., 50kg, 175cm &rarr; 16.3, Underweight)', body_style),
        Paragraph('&bull; Verified overweight (e.g., 85kg, 175cm &rarr; 27.8, Overweight)', body_style),
        Paragraph('&bull; Verified obese (e.g., 100kg, 175cm &rarr; 32.7, Obese)', body_style),
        Paragraph('&bull; Verified empty, zero, negative, and decimal inputs &amp; Reset functionality', body_style)
    ]

    doc.build(story)
    print('PDF generated successfully!')

if __name__ == '__main__':
    generate_pdf()
