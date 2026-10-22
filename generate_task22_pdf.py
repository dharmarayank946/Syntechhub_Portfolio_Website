import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, HRFlowable

def generate_pdf():
    pdf_path = r'd:\Projects\Veda\Task22_Image_Carousel_Slider_Report.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # Brand Colors - Light Theme with Pastel Sage Green & Forest Accents
    c_primary = colors.HexColor('#1E2922')
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
        Paragraph('VEDA Technology Internship — Task 22 Report', title_style),
        Paragraph('Image Carousel &amp; Slider Documentation &amp; Verification (Scenic Landscapes Theme)', subtitle_style),
        HRFlowable(width='100%', thickness=1.5, color=c_green, spaceAfter=10),
        
        Paragraph('1. Project Overview', h2_style),
        Paragraph('This report documents the design, architecture, and verification of <b>Task 22 (Image Carousel / Slider)</b> for the VEDA Technology Web Development Internship. The project delivers an interactive, touch-friendly, and accessible image slider engineered strictly with <b>HTML5</b>, <b>CSS3</b>, and <b>Vanilla JavaScript (ES6+)</b>. Styled with an elegant <b>Light Pastel Green</b> palette (#F6FAF7 background, #FFFFFF surface cards, #2D6A4F primary forest green, #D8F3DC / #52B788 accents, and #E2EDE5 borders), the application showcases 6 high-definition nature landscape slides with smooth sliding transitions, infinite looping navigation, automated 4-second rotation with hover/focus pause-and-resume, touch swipe gesture support, keyboard arrows, direct dot indicators, and full WAI-ARIA compliance with zero external dependencies.', body_style),
        
        Paragraph('2. Technical Architecture &amp; Component Stack', h2_style),
        Table([
            [Paragraph('<b>Component</b>', body_style), Paragraph('<b>Implementation &amp; Technical Details</b>', body_style)],
            [Paragraph('Semantic HTML5 &amp; ARIA', body_style), Paragraph('Structured with <code>&lt;section role="region" aria-roledescription="carousel"&gt;</code>, <code>&lt;article role="group" aria-roledescription="slide"&gt;</code>, live regions, and <code>role="tablist"</code> indicators.', body_style)],
            [Paragraph('Responsive Flex &amp; Viewport', body_style), Paragraph('Hardware-accelerated horizontal track utilizing CSS <code>transform: translateX(-N * 100%)</code> with cubic-bezier timing (0.4, 0, 0.2, 1) for fluid 60fps sliding.', body_style)],
            [Paragraph('High-Definition Media', body_style), Paragraph('6 landscape slides (Yosemite, Black Forest, Kauai, Kluane, Redwood, Isle of Skye) with 16:9 ratio, responsive object-fit, and lazy loading.', body_style)],
            [Paragraph('Infinite Looping Logic', body_style), Paragraph('Seamless modular wrap-around navigation: clicking Next on slide 6 advances to slide 1, and clicking Previous on slide 1 wraps to slide 6.', body_style)],
            [Paragraph('Smart Autoplay Engine', body_style), Paragraph('Automated 4000ms rotation interval with automatic pause on mouse hover, focusin, or touch interaction, resuming gracefully on blur or mouseleave.', body_style)],
            [Paragraph('Touch Swipe Navigation', body_style), Paragraph('Pure touch event listeners (<code>touchstart</code>, <code>touchend</code>) computing horizontal delta X (threshold ≥ 50px) for smooth mobile swiping.', body_style)],
            [Paragraph('Interactive Indicators &amp; Counter', body_style), Paragraph('Clickable pagination dots with animated active width expansions, accessible aria-selected states, and live numeric fraction counters.', body_style)],
            [Paragraph('Keyboard &amp; Focus Accessibility', body_style), Paragraph('Full arrow key navigation (<kbd>&larr;</kbd> / <kbd>&rarr;</kbd>), visible high-contrast focus rings, and manual autoplay play/pause control button.', body_style)],
            [Paragraph('Zero Dependencies', body_style), Paragraph('100% vanilla code with no external JS libraries or UI frameworks; production-ready for GitHub Pages deployment.', body_style)]
        ], colWidths=[140, 390], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 2.8)
        ]),
        
        Paragraph('3. Functional Specifications Breakdown', h2_style),
        Table([
            [Paragraph('<b>Requirement</b>', body_style), Paragraph('<b>Logic &amp; Implementation Description</b>', body_style), Paragraph('<b>Status</b>', body_style)],
            [Paragraph('1. Multiple Image Slides', body_style), Paragraph('Features 6 nature photography slides with captions, tags, and descriptive alt text.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('2. Next &amp; Previous Controls', body_style), Paragraph('Previous and Next arrow buttons to navigate slides with modular index looping.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('3. Infinite Loop Navigation', body_style), Paragraph('Looping wrap-around navigation so users can continuously browse forward or backward.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('4. Smooth Slide Transitions', body_style), Paragraph('CSS transform translation with 0.5s cubic-bezier easing for smooth slide animation.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('5. Automatic Slide Rotation', body_style), Paragraph('Automatically transitions to the next slide every 4 seconds (4000ms).', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('6. Pause on Hover &amp; Focus', body_style), Paragraph('Halts the auto-rotation timer whenever the user hovers over or focuses inside the carousel.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('7. Resume on Mouse Leave', body_style), Paragraph('Automatically resumes rotation timer when pointer departs or focus moves out.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('8. Clickable Indicator Dots', body_style), Paragraph('Dot indicators dynamically highlight current slide and jump directly to clicked slide.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('9. Timer Reset on Interaction', body_style), Paragraph('Manual navigation resets the rotation countdown so slides do not switch prematurely.', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('10. Touch Swipe Gestures', body_style), Paragraph('Mobile touch gesture support allows left and right swiping to transition slides.', body_style), Paragraph('PASSED', pass_style)]
        ], colWidths=[140, 310, 80], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 2.5)
        ]),

        Paragraph('4. Verification &amp; Testing Matrix', h2_style),
        Table([
            [Paragraph('<b>Test Scenario</b>', body_style), Paragraph('<b>Input Action</b>', body_style), Paragraph('<b>Expected State</b>', body_style), Paragraph('<b>Actual State</b>', body_style), Paragraph('<b>Status</b>', body_style)],
            [Paragraph('Next Button Navigation', body_style), Paragraph('Click Next button on Slide 1', body_style), Paragraph('Slide 2 displayed, indicator 2 active, counter shows 2/6', body_style), Paragraph('Smooth transition to Slide 2; state updated', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Previous Button Navigation', body_style), Paragraph('Click Prev button on Slide 1', body_style), Paragraph('Loops to Slide 6, indicator 6 active, counter shows 6/6', body_style), Paragraph('Smooth wrap-around to Slide 6 confirmed', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Forward Infinite Loop', body_style), Paragraph('Click Next button on Slide 6', body_style), Paragraph('Loops to Slide 1, indicator 1 active, counter shows 1/6', body_style), Paragraph('Wrap-around to initial slide verified', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Direct Indicator Click', body_style), Paragraph('Click dot indicator 4', body_style), Paragraph('Direct jump to Slide 4, timer reset to 4000ms', body_style), Paragraph('Slide 4 instantly active; timer refreshed', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Autoplay Rotation', body_style), Paragraph('Observe idle carousel for 4s', body_style), Paragraph('Slide advances automatically to next slide', body_style), Paragraph('Slide rotated at exactly 4s intervals', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Hover Pause Verification', body_style), Paragraph('Hover mouse over slide media', body_style), Paragraph('Timer paused; active slide remains indefinitely', body_style), Paragraph('Autoplay halted during hover duration', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Mouse Leave Resume', body_style), Paragraph('Move mouse pointer outside', body_style), Paragraph('Timer restarts; advances after next full cycle', body_style), Paragraph('Autoplay restarted smoothly without skipping', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Keyboard Navigation', body_style), Paragraph('Press ArrowRight / ArrowLeft', body_style), Paragraph('Slides advance or retreat accordingly', body_style), Paragraph('Keyboard events handled accurately', body_style), Paragraph('PASSED', pass_style)],
            [Paragraph('Touch Swipe on Mobile', body_style), Paragraph('Horizontal swipe left (>50px)', body_style), Paragraph('Advances to next slide on mobile touch screen', body_style), Paragraph('Touch delta recognized; slide transitioned', body_style), Paragraph('PASSED', pass_style)]
        ], colWidths=[95, 110, 125, 130, 70], style=[
            ('BACKGROUND', (0,0), (-1,0), c_tbl_bg),
            ('GRID', (0,0), (-1,-1), 0.5, c_tbl_grid),
            ('PADDING', (0,0), (-1,-1), 2.2)
        ]),

        Paragraph('5. Deployment &amp; Repository Structure', h2_style),
        Paragraph('&bull; <b>Directory:</b> <code>Image-Carousel-Slider/</code>', body_style),
        Paragraph('&bull; <b>Files:</b> <code>index.html</code>, <code>style.css</code>, <code>script.js</code>, <code>README.md</code>, <code>images/ (6 slides)</code>', body_style),
        Paragraph('&bull; <b>GitHub Repository:</b> <code>https://github.com/dharmarayank946/Image-Carousel-Slider.git</code>', body_style),
        Paragraph('&bull; <b>GitHub Pages Live Demo:</b> <code>https://dharmarayank946.github.io/Image-Carousel-Slider/</code>', body_style),
        Paragraph('&bull; <b>Developer:</b> Nagalambika D Koralli &bull; VEDA Technology Internship', body_style)
    ]

    doc.build(story)
    shutil.copyfile(pdf_path, r'd:\Projects\Veda\Task22_Report.pdf')
    print('Task 22 PDF Reports generated successfully!')

if __name__ == '__main__':
    generate_pdf()
