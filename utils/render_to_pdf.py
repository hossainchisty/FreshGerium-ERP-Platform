from io import BytesIO

from xhtml2pdf import pisa

from django.http import HttpResponse
from django.template.loader import get_template

__author__ = "Hossain Chisty"

def generate_pdf(template_src, context_dict={}):
    '''
    Generates a PDF file from a template and context dictionary.
    '''
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return None
