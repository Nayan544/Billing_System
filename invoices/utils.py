from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict):
    try:
        template = get_template(template_src)
        html = template.render(context_dict)

        if not html:
            html = "<p>No content to render.</p>"  # fallback for NoneType

        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result)

        if not pdf.err:
            return result.getvalue()
        else:
            print("PDF generation error:", pdf.err)
            return None

    except Exception as e:
        print("PDF render exception in VS Code console:", e)
        return None