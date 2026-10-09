import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_pdf():
    pdf_path = r'd:\Projects\Veda\Task9_Image_Gallery_Report.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # Brand Colors - Professional Slate & Accent Palette
    c_primary = colors.HexColor('#263248')
    c_accent = colors.HexColor('#5577D9')
    c_subtitle = colors.HexColor('#718096')
    c_tbl_bg = colors.HexColor('#F7F9FC')
    c_tbl_grid = colors.HexColor('#E2E8F0')

    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=c_primary, spaceAfter=4)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=13, textColor=c_subtitle, spaceAfter=12)
    h2_style = ParagraphStyle('SectionH2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=c_accent, spaceBefore=10, spaceAfter=4)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12, textColor=c_primary, spaceAfter=4)
    pass_style = ParagraphStyle('PassText', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=colors.HexColor('#16A34A'))

    story = [
        Paragraph('VEDA Technology Internship — Task 9 Report', title_style),
        Paragraph('Image Gallery Application Documentation', subtitle_style),
        HRFlowable(width='100%', thickness=1.5, color=c_accent, spaceAfter=10),
        
        Paragraph('1. Project Overview', h2_style),
        Paragraph('This report documents the design, implementation, and empirical verification of <b>Task 9 (Image Gallery)</b> for the VEDA Technology Web Development Internship. The application delivers an interactive, modern, and accessible image gallery built strictly using HTML5, CSS3 (CSS Grid), and Vanilla JavaScript without relying on external frameworks or third-party libraries.', body_style),
        
        Paragraph('2. Technical Architecture & Component Stack', h2_style),
        Table([
            [Paragraph('<b>Component</b>', body_style), Paragraph('<b>Implementation &amp; Technical Details</b>', body_style)],
            [Paragraph('HTML5 Structure', body_style), Paragraph('Semantic HTML5 elements (<code>&lt;header&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;article&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;footer&gt;</code>) with accessibility attributes (<code>aria-hidden</code>, <code>aria-label</code>, <code>tabindex</code>).', body_style)],
            [Paragraph('CSS3 Grid &amp; Layout', body_style), Paragraph('Clean light theme palette (<code>#F7F9FC</code> background, <code>#5577D9</code> accent, <code>#263248</code> text). Responsive CSS Grid with breakpoints for 4-col desktop, 3-col laptop, 2-col tablet, and 1-col mobile layout.', body_style)],
            [Paragraph('Vanilla JS (ES6+)', body_style), Paragraph('State-driven lightbox preview modal, image counter, category filtering, escape key modal closing, left/right arrow keyboard navigation, and focus restoration.', body_style)]
        ], colWidths=[110, 420], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 5)
        ]),
        
        Paragraph('3. Key Features &amp; Technical Capabilities', h2_style),
        Table([
            [Paragraph('<b>Feature Name</b>', body_style), Paragraph('<b>Technical Specification</b>', body_style), Paragraph('<b>User Experience Impact</b>', body_style)],
            [Paragraph('9 Curated Images', body_style), Paragraph('High-res photography via reliable Unsplash CDN URLs with alt text.', body_style), Paragraph('Ensures non-broken, visually compelling nature gallery content.', body_style)],
            [Paragraph('CSS Grid Layout', body_style), Paragraph('Fluid grid using <code>grid-template-columns</code> &amp; media queries.', body_style), Paragraph('Adapts seamlessly from 4 columns on desktop down to 1 col on mobile.', body_style)],
            [Paragraph('Lightbox Modal', body_style), Paragraph('Full-screen backdrop with blurred overlay &amp; smooth scale transform.', body_style), Paragraph('Delivers focus on enlarged image previews with captions.', body_style)],
            [Paragraph('Keyboard Nav', body_style), Paragraph('Handles <code>Escape</code> to close, <code>ArrowLeft</code> / <code>ArrowRight</code> to navigate.', body_style), Paragraph('Enables effortless accessible browsing without touching a mouse.', body_style)],
            [Paragraph('Category Filter', body_style), Paragraph('Dynamic JS filtering by category tags (Mountains, Forest, Water).', body_style), Paragraph('Allows instant sorting and grouping of gallery items.', body_style)]
        ], colWidths=[110, 210, 210], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 5)
        ]),

        Paragraph('4. Aspect Ratio &amp; Accessibility Safety Compliance', h2_style),
        Paragraph('&bull; <b>Aspect Ratio Maintenance:</b> Gallery cards enforce <code>aspect-ratio: 4 / 3</code> with <code>object-fit: cover</code>; lightbox previews enforce <code>object-fit: contain</code> with <code>max-height: 75vh</code> ensuring 0 image distortion.', body_style),
        Paragraph('&bull; <b>Zero Framework Dependency:</b> 100% written in native HTML5, CSS3, and ES6 JavaScript.', body_style),
        Paragraph('&bull; <b>Keyboard &amp; ARIA Accessibility:</b> All cards are key-focusable (<code>tabindex="0"</code>); modal uses <code>role="dialog"</code> and <code>aria-modal="true"</code> with automatic focus lock and return.', body_style),
        Paragraph('&bull; <b>Scroll Lock Prevention:</b> Lightbox modal dynamically locks body scroll (<code>overflow: hidden</code>) while active and restores scroll on close.', body_style),

        Paragraph('5. Verification Test Suite Matrix', h2_style),
        Table([
            [Paragraph('<b>Test Case</b>', body_style), Paragraph('<b>Execution Path</b>', body_style), Paragraph('<b>Expected Outcome</b>', body_style), Paragraph('<b>Status</b>', body_style)],
            [Paragraph('Gallery Load', body_style), Paragraph('Page DOMContentLoaded', body_style), Paragraph('9 high-res images render with alt text', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Card Click Preview', body_style), Paragraph('Click any gallery item', body_style), Paragraph('Lightbox opens correct full image &amp; title', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Close Button', body_style), Paragraph('Click <code>#lightbox-close</code>', body_style), Paragraph('Lightbox closes, scroll restored', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Escape Key Close', body_style), Paragraph('Press Escape key', body_style), Paragraph('Active lightbox modal closes immediately', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Arrow Key Nav', body_style), Paragraph('Press Left / Right arrows', body_style), Paragraph('Cycles smoothly to prev/next image', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Console Audit', body_style), Paragraph('Browser DevTools check', body_style), Paragraph('0 JavaScript console errors', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Mobile Layout', body_style), Paragraph('Viewport width &lt; 540px', body_style), Paragraph('Responsive 1-col layout, zero overflow', body_style), Paragraph('PASSED', pass_style)]
        ], colWidths=[100, 160, 170, 100], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 4)
        ]),

        Paragraph('6. Repository &amp; Local Verification Information', h2_style),
        Paragraph('&bull; <b>GitHub Repository:</b> <code>https://github.com/dharmarayank946/Image-Gallery.git</code>', body_style),
        Paragraph('&bull; <b>Target Folder:</b> <code>Task9-Image-Gallery/</code>', body_style),
        Paragraph('&bull; <b>Local Web Server:</b> <code>http://localhost:8009</code>', body_style)
    ]

    doc.build(story)
    # Also create Task9_Report.pdf copy for standard naming
    shutil.copyfile(pdf_path, r'd:\Projects\Veda\Task9_Report.pdf')
    print('Task 9 PDF Reports generated successfully!')

if __name__ == '__main__':
    generate_pdf()
