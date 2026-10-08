import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_pdf():
    pdf_path = r'd:\Projects\Veda\Project_Report.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.HexColor('#49352F'), spaceAfter=4)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=13, textColor=colors.HexColor('#806B63'), spaceAfter=12)
    h2_style = ParagraphStyle('SectionH2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=15, textColor=colors.HexColor('#E88B6B'), spaceBefore=10, spaceAfter=4)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#49352F'), spaceAfter=4)

    story = [
        Paragraph('VEDA Technology Internship — Task 5 Report', title_style),
        Paragraph('Temperature Converter Application Documentation', subtitle_style),
        HRFlowable(width='100%', thickness=1.5, color=colors.HexColor('#E88B6B'), spaceAfter=10),
        
        Paragraph('1. Project Overview', h2_style),
        Paragraph('This report details <b>Task 5 (Temperature Converter)</b> for the VEDA Technology Web Development Internship. The web app enables real-time conversion between Celsius (&deg;C), Fahrenheit (&deg;F), and Kelvin (K).', body_style),
        
        Paragraph('2. Technical Architecture', h2_style),
        Table([
            [Paragraph('<b>Component</b>', body_style), Paragraph('<b>Technology Details</b>', body_style)],
            [Paragraph('HTML5', body_style), Paragraph('Semantic structure (&lt;header&gt;, &lt;main&gt;, &lt;section&gt;, &lt;form&gt;, &lt;select&gt;, &lt;footer&gt;)', body_style)],
            [Paragraph('CSS3', body_style), Paragraph('Custom Soft Peach theme (--bg-main: #FFF9F5, --primary: #E88B6B, --light: #F6D6C9)', body_style)],
            [Paragraph('Vanilla JS', body_style), Paragraph('Native DOM selection, input event listeners, 6 unit functions, input validation', body_style)]
        ], colWidths=[100, 430], style=[
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F6D6C9')),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E8D5CE')),
            ('PADDING', (0,0), (-1,-1), 5)
        ]),
        
        Paragraph('3. Conversion Formulas &amp; JavaScript Functions', h2_style),
        Table([
            [Paragraph('<b>Conversion Pair</b>', body_style), Paragraph('<b>Function Name</b>', body_style), Paragraph('<b>Formula</b>', body_style)],
            [Paragraph('Celsius &rarr; Fahrenheit', body_style), Paragraph('celsiusToFahrenheit(c)', body_style), Paragraph('(C &times; 9/5) + 32', body_style)],
            [Paragraph('Celsius &rarr; Kelvin', body_style), Paragraph('celsiusToKelvin(c)', body_style), Paragraph('C + 273.15', body_style)],
            [Paragraph('Fahrenheit &rarr; Celsius', body_style), Paragraph('fahrenheitToCelsius(f)', body_style), Paragraph('(F - 32) &times; 5/9', body_style)],
            [Paragraph('Fahrenheit &rarr; Kelvin', body_style), Paragraph('fahrenheitToKelvin(f)', body_style), Paragraph('(F - 32) &times; 5/9 + 273.15', body_style)],
            [Paragraph('Kelvin &rarr; Celsius', body_style), Paragraph('kelvinToCelsius(k)', body_style), Paragraph('K - 273.15', body_style)],
            [Paragraph('Kelvin &rarr; Fahrenheit', body_style), Paragraph('kelvinToFahrenheit(k)', body_style), Paragraph('(K - 273.15) &times; 9/5 + 32', body_style)],
        ], colWidths=[140, 160, 230], style=[
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F6D6C9')),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E8D5CE')),
            ('PADDING', (0,0), (-1,-1), 4)
        ]),

        Paragraph('4. Features &amp; Validation Rules', h2_style),
        Paragraph('&bull; <b>Live Conversion:</b> Real-time updates via JavaScript <code>input</code> and <code>change</code> event listeners.', body_style),
        Paragraph('&bull; <b>Empty Input Validation:</b> Displays <i>"Enter a temperature to convert."</i>', body_style),
        Paragraph('&bull; <b>Invalid Number Validation:</b> Displays <i>"Please enter a valid temperature."</i>', body_style),
        Paragraph('&bull; <b>Absolute Zero Boundary (0 K):</b> Prevents temperatures below 0 K and displays <i>"Kelvin temperature cannot be below 0 K."</i>', body_style),
        Paragraph('&bull; <b>Number Formatting:</b> Displays up to 2 decimal places without trailing zeroes (e.g. 25 &deg;C = 77 &deg;F).', body_style),

        Paragraph('5. GitHub Repository Information', h2_style),
        Paragraph('&bull; <b>Repository URL:</b> https://github.com/dharmarayank946/Temperature-Converter.git', body_style),
        Paragraph('&bull; <b>Local Path:</b> D:\\Projects\\Veda\\Task5-Temperature-Converter\\', body_style)
    ]

    doc.build(story)
    print('PDF generated successfully!')

if __name__ == '__main__':
    generate_pdf()
