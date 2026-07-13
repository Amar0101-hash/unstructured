import os
from collections import defaultdict
from pathlib import Path

# Fully offline mode: never contact huggingface.co (must be set before docling imports)
os.environ["HF_HUB_OFFLINE"] = "1"

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

# Folder with pre-downloaded models (copy this folder to the corporate laptop)
artifacts_path = Path(r"")

pipeline_options = PdfPipelineOptions(artifacts_path=artifacts_path)
converter = DocumentConverter(
    format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
)

# Load and parse the PDF
result = converter.convert(r"")
doc = result.document

# Full document text (markdown)
print(doc.export_to_markdown())

# Group text items by page
pages = defaultdict(list)
for item, _ in doc.iterate_items():
    if hasattr(item, "text") and item.prov:
        pages[item.prov[0].page_no].append(item.text)

# Access a specific page (page numbers start at 1)
first_page_text = "\n".join(pages[1])
print(first_page_text)