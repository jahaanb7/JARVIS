import re

class TextFormat:
  def clean_markdown(self, text):

    # Remove bold/italic markers
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', text)  # bold+italic
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)      # bold
    text = re.sub(r'\*(.+?)\*', r'\1', text)          # italic
    text = re.sub(r'__(.+?)__', r'\1', text)          # bold alt
    text = re.sub(r'_(.+?)_', r'\1', text)            # italic alt

    # Convert headers to emphasized text
    text = re.sub(r'^### (.+)$', r'\n\1:', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'\n\1:', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'\n\1:', text, flags=re.MULTILINE)

    # Convert numbered lists - add newlines before numbers
    text = re.sub(r'(\d+)\.\s+', r'\n\1. ', text)

    # Convert list items
    text = re.sub(r'^\* ', r'  • ', text, flags=re.MULTILINE)
    text = re.sub(r'^\- ', r'  • ', text, flags=re.MULTILINE)

    # Clean up horizontal rules
    text = re.sub(r'^---+$', r'', text, flags=re.MULTILINE)

    # Remove extra blank lines (more than 2 in a row)
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()