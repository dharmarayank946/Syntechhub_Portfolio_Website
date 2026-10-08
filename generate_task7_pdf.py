import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_pdf():
    pdf_path = r'd:\Projects\Veda\Task7_Basic_Calculator_Report.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # Brand Colors - Professional Slate & Blue
    c_primary = colors.HexColor('#1E293B')
    c_accent = colors.HexColor('#2563EB')
    c_subtitle = colors.HexColor('#64748B')
    c_tbl_bg = colors.HexColor('#EFF6FF')
    c_tbl_grid = colors.HexColor('#BFDBFE')

    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=c_primary, spaceAfter=4)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=13, textColor=c_subtitle, spaceAfter=12)
    h2_style = ParagraphStyle('SectionH2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=c_accent, spaceBefore=10, spaceAfter=4)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12, textColor=c_primary, spaceAfter=4)
    pass_style = ParagraphStyle('PassText', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=colors.HexColor('#16A34A'))

    story = [
        Paragraph('VEDA Technology Internship — Task 7 Report', title_style),
        Paragraph('Basic Calculator Application Documentation', subtitle_style),
        HRFlowable(width='100%', thickness=1.5, color=c_accent, spaceAfter=10),
        
        Paragraph('1. Project Overview', h2_style),
        Paragraph('This report documents the implementation and verification of <b>Task 7 (Basic Calculator)</b> for the VEDA Technology Web Development Internship. The application delivers a clean, light, and responsive web calculator built strictly with HTML5, CSS3, and Vanilla JavaScript without external frameworks, libraries, or dynamic <code>eval()</code> calls.', body_style),
        
        Paragraph('2. Technical Architecture & Component Stack', h2_style),
        Table([
            [Paragraph('<b>Component</b>', body_style), Paragraph('<b>Implementation &amp; Design Details</b>', body_style)],
            [Paragraph('HTML5', body_style), Paragraph('Semantic structure (<code>&lt;header&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;section&gt;</code>), accessible keypad buttons with <code>aria-label</code> tags.', body_style)],
            [Paragraph('CSS3 Grid', body_style), Paragraph('CSS Grid 4-column layout (<code>repeat(4, 1fr)</code>), light slate theme (<code>#f1f5f9</code> / <code>#ffffff</code>), subtle button active transform scaling, mobile responsive breakpoints.', body_style)],
            [Paragraph('Vanilla JS', body_style), Paragraph('Event delegation keypad listener, explicit state variables (<code>currentInput</code>, <code>previousInput</code>, <code>operator</code>), floating-point precision correction, zero <code>eval()</code> usage.', body_style)]
        ], colWidths=[100, 430], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 5)
        ]),
        
        Paragraph('3. Keypad Layout &amp; Operations Table', h2_style),
        Table([
            [Paragraph('<b>Operation</b>', body_style), Paragraph('<b>Symbol</b>', body_style), Paragraph('<b>Key Class / Column Span</b>', body_style), Paragraph('<b>Functionality Description</b>', body_style)],
            [Paragraph('Clear', body_style), Paragraph('C', body_style), Paragraph('<code>btn-clear</code> (Spans 2 cols)', body_style), Paragraph('Resets all calculator state, displays, and operands to 0.', body_style)],
            [Paragraph('Delete', body_style), Paragraph('⌫', body_style), Paragraph('<code>btn-delete</code> (1 col)', body_style), Paragraph('Removes the last entered character/digit.', body_style)],
            [Paragraph('Division', body_style), Paragraph('÷', body_style), Paragraph('<code>btn-operator</code> (1 col)', body_style), Paragraph('Divides previous number by current number.', body_style)],
            [Paragraph('Multiplication', body_style), Paragraph('×', body_style), Paragraph('<code>btn-operator</code> (1 col)', body_style), Paragraph('Multiplies previous number by current number.', body_style)],
            [Paragraph('Subtraction', body_style), Paragraph('-', body_style), Paragraph('<code>btn-operator</code> (1 col)', body_style), Paragraph('Subtracts current number from previous number.', body_style)],
            [Paragraph('Addition', body_style), Paragraph('+', body_style), Paragraph('<code>btn-operator</code> (1 col)', body_style), Paragraph('Adds current number to previous number.', body_style)],
            [Paragraph('Zero Digit', body_style), Paragraph('0', body_style), Paragraph('<code>btn-zero</code> (Spans 2 cols)', body_style), Paragraph('Appends digit 0 (handles leading zero rule).', body_style)],
            [Paragraph('Decimal Point', body_style), Paragraph('.', body_style), Paragraph('<code>btn-decimal</code> (1 col)', body_style), Paragraph('Appends decimal (prevents duplicate decimal entries).', body_style)],
            [Paragraph('Equals', body_style), Paragraph('=', body_style), Paragraph('<code>btn-equals</code> (1 col)', body_style), Paragraph('Computes and displays the final result.', body_style)],
        ], colWidths=[80, 50, 160, 240], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 4)
        ]),

        Paragraph('4. Input Validation &amp; Safety Rules', h2_style),
        Paragraph('&bull; <b>Zero <code>eval()</code> Policy:</b> All arithmetic operations are executed using explicit JS arithmetic operators (<code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>).', body_style),
        Paragraph('&bull; <b>Divide-by-Zero Safety:</b> Catch division by 0 prior to evaluation and output <i>"Cannot divide by zero"</i> without throwing runtime exceptions or crashing the UI state.', body_style),
        Paragraph('&bull; <b>Decimal Validation:</b> Strictly checks <code>!currentInput.includes(".")</code> before appending decimal point, preventing malformed values such as <code>2.5.3</code>.', body_style),
        Paragraph('&bull; <b>Floating-Point Precision:</b> Applies <code>Math.round(result * 1e10) / 1e10</code> to eliminate IEEE 754 precision artifacts (e.g. <code>2.5 + 3.5 = 6</code>).', body_style),

        Paragraph('5. Verification Matrix', h2_style),
        Table([
            [Paragraph('<b>Test Case</b>', body_style), Paragraph('<b>Input Sequence</b>', body_style), Paragraph('<b>Expected Output</b>', body_style), Paragraph('<b>Status</b>', body_style)],
            [Paragraph('Addition', body_style), Paragraph('<code>10 + 5 =</code>', body_style), Paragraph('<code>15</code>', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Subtraction', body_style), Paragraph('<code>10 - 5 =</code>', body_style), Paragraph('<code>5</code>', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Multiplication', body_style), Paragraph('<code>10 × 5 =</code>', body_style), Paragraph('<code>50</code>', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Division', body_style), Paragraph('<code>10 ÷ 5 =</code>', body_style), Paragraph('<code>2</code>', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Decimal Math', body_style), Paragraph('<code>2.5 + 3.5 =</code>', body_style), Paragraph('<code>6</code>', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Divide by Zero', body_style), Paragraph('<code>5 ÷ 0 =</code>', body_style), Paragraph('Cannot divide by zero', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Clear Reset', body_style), Paragraph('Press <code>C</code>', body_style), Paragraph('Resets display to <code>0</code>', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Multiple Decimals', body_style), Paragraph('<code>2 . 5 . 3</code>', body_style), Paragraph('<code>2.53</code>', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Chained Operations', body_style), Paragraph('<code>10 + 5 = + 5 =</code>', body_style), Paragraph('<code>20</code>', body_style), Paragraph('PASSED', pass_style)]
        ], colWidths=[100, 150, 180, 100], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 4)
        ]),

        Paragraph('6. Repository &amp; Deployment Information', h2_style),
        Paragraph('&bull; <b>GitHub Repository:</b> <code>https://github.com/dharmarayank946/Basic-Calculator.git</code>', body_style),
        Paragraph('&bull; <b>Local Host Server:</b> <code>http://localhost:8000</code>', body_style)
    ]

    doc.build(story)
    print('Task 7 PDF Report generated successfully!')

if __name__ == '__main__':
    generate_pdf()
