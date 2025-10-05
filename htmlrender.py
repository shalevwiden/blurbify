

# import imgkit


# def render_html():
#     with open("htmlfiles/bodyhtml.html", "r", encoding="utf-8") as bodyfile:
#         body_html = bodyfile.read()
#     imgkit.from_string(body_html, "imagetemplates/from_string.png")

# render_html()
import weasyprint
import pypdfium2 as pdfium
from PIL import Image

def render_html_to_png(html_file, png_file):
    # Step 1: Read HTML
    with open(html_file, "r", encoding="utf-8") as f:
        body_html = f.read()

    # Step 2: Render HTML → PDF (WeasyPrint)
    pdf_path = png_file.replace(".png", ".pdf")
    weasyprint.HTML(string=body_html).write_pdf(pdf_path)

    # Step 3: Open PDF with pypdfium2
    pdf = pdfium.PdfDocument(pdf_path)
    page = pdf[0]  # take first page
    pil_image = page.render(scale=2).to_pil()  # scale=2 for higher resolution

    # Step 4: Save as PNG
    pil_image.save(png_file)

    return pil_image

# Example usage:

htmlsource="web_stuff/templates/bodyhtml.html"
saveimage="image_templates/bodytext.png"
img = render_html_to_png(htmlsource, saveimage)
img.show()
