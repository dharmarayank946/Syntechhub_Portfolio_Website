import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, HRFlowable

def generate_pdf():
    pdf_path = r'd:\Projects\Veda\Task21_Responsive_Navbar_Report.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # Brand Colors - Light Pastel Green & White Palette
    c_primary = colors.HexColor('#1C2B21')
    c_green = colors.HexColor('#2D6A4F')
    c_subtitle = colors.HexColor('#526659')
    c_tbl_bg = colors.HexColor('#F4F8F5')
    c_tbl_grid = colors.HexColor('#D0E7D7')

    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=c_primary, spaceAfter=4)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=13, textColor=c_subtitle, spaceAfter=12)
    h2_style = ParagraphStyle('SectionH2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=c_green, spaceBefore=10, spaceAfter=4)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=c_primary, spaceAfter=4)
    pass_style = ParagraphStyle('PassText', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11.5, textColor=colors.HexColor('#16A34A'))

    story = [
        Paragraph('VEDA Technology Internship — Task 21 Report', title_style),
        Paragraph('Responsive Navbar with Hamburger Menu Documentation &amp; Verification (Light Pastel Green &amp; White Theme)', subtitle_style),
        HRFlowable(width='100%', thickness=1.5, color=c_green, spaceAfter=10),
        
        Paragraph('1. Project Overview', h2_style),
        Paragraph('This report documents the design, architecture, and verification of <b>Task 21 (Responsive Navbar with Hamburger Menu)</b> for the VEDA Technology Web Development Internship. The project delivers a fully responsive, accessible, and high-performance navigation component engineered strictly with <b>HTML5</b>, <b>CSS3</b>, and <b>Vanilla JavaScript (ES6+)</b>. Styled with an elegant <b>Light Pastel Green and White</b> theme (#F4F8F5 background, #FFFFFF navbar/cards, #2D6A4F primary forest green, #EAF5EE badge accents, #D0E7D7 borders), it provides a desktop horizontal navigation bar and collapses into an animated 3-bar hamburger drawer on mobile screens (≤ 768px). The menu features smooth slide-in/out transitions, automatic closure on link selection or backdrop clicks, Escape key dismissal, and comprehensive WAI-ARIA states with zero external dependencies.', body_style),
        
        Paragraph('2. Technical Architecture &amp; Component Stack', h2_style),
        Table([
            [Paragraph('<b>Component</b>', body_style), Paragraph('<b>Implementation &amp; Technical Details</b>', body_style)],
            [Paragraph('HTML5 Semantic Structure', body_style), Paragraph('Structured with <code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;ul&gt;</code>, <code>&lt;li&gt;</code>, <code>&lt;a&gt;</code>, and <code>&lt;button&gt;</code> using proper accessibility landmarks and ARIA attributes.', body_style)],
            [Paragraph('Pastel Green &amp; White Theme', body_style), Paragraph('Light theme (#F4F8F5 / #FFFFFF) with sage green accents (#2D6A4F, #EAF5EE), high-contrast accessible text (#1C2B21), visible focus rings, and clean mobile-first layout.', body_style)],
            [Paragraph('Animated Hamburger Button', body_style), Paragraph('3 horizontal span lines smoothly morphing into an "X" via CSS transforms (rotate 45deg, scaleX 0, translateY) when <code>.is-active</code> is applied.', body_style)],
            [Paragraph('Hardware Slide Transitions', body_style), Paragraph('Off-canvas drawer utilizing CSS <code>transform: translateX(105%)</code> to <code>translateX(0)</code> with 0.28s cubic-bezier timing for 60fps sliding.', body_style)],
            [Paragraph('classList.toggle() Control', body_style), Paragraph('Menu state toggling strictly powered by vanilla JS <code>classList.toggle(\'is-active\')</code> and <code>classList.toggle(\'is-open\')</code>.', body_style)],
            [Paragraph('Auto-Close &amp; Escape Key', body_style), Paragraph('Drawer collapses automatically upon clicking any nav link, clicking the backdrop overlay, or pressing the <kbd>Esc</kbd> key.', body_style)],
            [Paragraph('WAI-ARIA &amp; Focus Recovery', body_style), Paragraph('Dynamic updates for <code>aria-expanded</code> and <code>aria-label</code>; focus automatically returns to the toggle button on Escape.', body_style)],
            [Paragraph('Zero Dependencies', body_style), Paragraph('100% pure vanilla HTML5, CSS3, and JavaScript; zero frameworks, zero external dependencies, ready for instant GitHub Pages hosting.', body_style)]
        ], colWidths=[140, 390], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 3)
        ]),
        
        Paragraph('3. Functional Specifications Breakdown', h2_style),
        Table([
            [Paragraph('<b>Requirement</b>', body_style), Paragraph('<b>Logic &amp; Implementation Description</b>', body_style), Paragraph('<b>Status</b>', body_style)],
            [Paragraph('1. Desktop Horizontal Bar', body_style), Paragraph('Displays brand and links in a clean horizontal row on screens > 768px with pill hover effects.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('2. Brand &amp; 5 Nav Links', body_style), Paragraph('Includes VEDATech brand with logo and links: Home, About, Services, Projects, Contact.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('3. Mobile Hamburger Menu', body_style), Paragraph('Collapses links into an off-canvas drawer on mobile screens (≤ 768px).', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('4. Hamburger Click Toggle', body_style), Paragraph('Clicking hamburger button opens and closes mobile menu using classList.toggle().', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('5. CSS Media Queries', body_style), Paragraph('Responsive layout switching at 768px and 480px breakpoints using pure CSS media queries.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('6. Slide Transitions', body_style), Paragraph('Smooth 0.28s cubic-bezier slide-in and slide-out transition without layout shift or jank.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('7. Auto-Close on Link Select', body_style), Paragraph('Clicking any navigation link closes mobile menu immediately and scrolls to section.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('8. Escape Key Support', body_style), Paragraph('Pressing Escape key closes drawer and returns focus to the toggle button.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('9. Animated Hamburger Icon', body_style), Paragraph('Updates hamburger icon: 3 lines morph into an "X" when open, reverting on close.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('10. Accessible ARIA &amp; Focus', body_style), Paragraph('aria-expanded, aria-label, aria-controls, and high-contrast visible keyboard focus rings.', body_style), Paragraph('PASSED', pass_style)]
        ], colWidths=[140, 310, 80], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 2.5)
        ]),

        Paragraph('4. Verification &amp; Testing Matrix', h2_style),
        Table([
            [Paragraph('<b>Test Scenario</b>', body_style), Paragraph('<b>Input Action</b>', body_style), Paragraph('<b>Expected State</b>', body_style), Paragraph('<b>Actual State</b>', body_style), Paragraph('<b>Status</b>', body_style)],
            [Paragraph('Desktop Viewport', body_style), Paragraph('Window width > 768px', body_style), Paragraph('Horizontal navbar visible, hamburger button hidden', body_style), Paragraph('Links displayed horizontally, toggle hidden', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Mobile Viewport', body_style), Paragraph('Window width ≤ 768px', body_style), Paragraph('Links collapsed into drawer, hamburger button visible', body_style), Paragraph('Drawer hidden off-screen, hamburger visible', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Open Hamburger', body_style), Paragraph('Click hamburger button', body_style), Paragraph('Drawer slides in, hamburger morphs to "X", overlay dims', body_style), Paragraph('Drawer visible, "X" icon active, overlay active', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Close Hamburger', body_style), Paragraph('Click "X" button', body_style), Paragraph('Drawer slides out, icon returns to 3 bars, overlay hidden', body_style), Paragraph('Drawer closed, 3 bars restored, overlay cleared', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Link Selection', body_style), Paragraph('Click "Services" link', body_style), Paragraph('Menu closes automatically, page scrolls to #services', body_style), Paragraph('Drawer closed, smoothly scrolled to section', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Escape Key Press', body_style), Paragraph('Press Escape key', body_style), Paragraph('Drawer closes instantly, focus returned to toggle', body_style), Paragraph('Menu closed, focus restored to button', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Backdrop Click', body_style), Paragraph('Click outside drawer', body_style), Paragraph('Drawer dismisses smoothly, overlay fades out', body_style), Paragraph('Menu closed, overlay dismissed cleanly', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Window Resize', body_style), Paragraph('Resize mobile to desktop', body_style), Paragraph('Open drawer classes cleared, desktop layout restored', body_style), Paragraph('Clean desktop reset without stuck classes', body_style), Paragraph('PASSED', pass_style)]
        ], colWidths=[95, 110, 125, 130, 70], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 2.2)
        ]),

        Paragraph('5. Deployment &amp; Repository Structure', h2_style),
        Paragraph('&bull; <b>Directory:</b> <code>Task21-Responsive-Navbar/</code>', body_style),
        Paragraph('&bull; <b>Files:</b> <code>index.html</code>, <code>style.css</code>, <code>script.js</code>, <code>README.md</code>', body_style),
        Paragraph('&bull; <b>GitHub Repository:</b> <code>https://github.com/dharmarayank946/Responsive-Navbar-with-Hamburger-Menu.git</code>', body_style),
        Paragraph('&bull; <b>GitHub Pages Live Demo:</b> <code>https://dharmarayank946.github.io/Responsive-Navbar-with-Hamburger-Menu/</code>', body_style),
        Paragraph('&bull; <b>Developer:</b> Nagalambika D Koralli &bull; VEDA Technology Internship', body_style)
    ]

    doc.build(story)
    shutil.copyfile(pdf_path, r'd:\Projects\Veda\Task21_Report.pdf')
    print('Task 21 PDF Reports generated successfully!')

if __name__ == '__main__':
    generate_pdf()
