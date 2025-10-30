# Claude CV Factory

**From manual CV editing chaos to automated, error-free resume generation.**

## The Problem

**Manual CV editing is a minefield:**
- Formatting breaks with every change
- Typos and inconsistencies slip through unnoticed
- Multiple CV versions fall out of sync
- Exporting to different formats requires manual work
- No data validation — errors are discovered too late

## The Solution

**Claude CV Factory automates professional resume generation with built-in quality control:**

### Data Over Documents
- Store CVs in **structured YAML** format
- Single source of truth for all versions
- Git version control for change tracking

### Validation Over Errors
- **Automatic validation** before generation (`validate_render_cv.py`)
- Three validation modes: quick/detailed/full
- Early detection of issues (missing fields, invalid dates, incorrect types)

### Automation Over Manual Export
- **One-command rendering** of all CVs: `python render_cv.py`
- Generate **all formats** simultaneously: PDF, HTML, PNG, Markdown, Typst
- Professional themes (ModernCV, sb2nov, classic) out of the box

### Built on RenderCV

This project leverages [RenderCV](https://rendercv.com), a modern Typst-based framework for generating typographically perfect resumes.

## Benefits

**From chaos to system:**
- Data consistency
- Instant generation in any format
- Error protection
- Versioning and reproducibility
- Focus on content, not formatting

## Features

- **RenderCV YAML format**: Store CV information in RenderCV's structured YAML format
- **Professional PDF generation**: Generate high-quality PDFs using modern themes
- **Multiple output formats**: PDF, PNG, HTML, and Markdown
- **Professional themes**: ModernCV and other themes available
- **Automated rendering**: Simple build script to render all CVs

## Getting Started

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd claude-cv-factory
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Quick Build (Recommended)

To render all CVs in one command:

```bash
python3 render_cv.py
```

Or to render a specific CV:

```bash
python render_cv.py Yuri_Timerkhanov_CV.yaml
```

This will render all YAML files to PDF and other formats in `rendercv_output/cv/`

### CV Data Format

CVs are stored in RenderCV YAML format in the `cv-bank/` directory.

See [RenderCV documentation](https://docs.rendercv.com) for detailed format information.

## Output Formats

RenderCV generates multiple formats:
- **PDF**: High-quality print-ready resume
- **PNG**: Image versions (useful for previews)
- **HTML**: Web-friendly format (compatible with Grammarly)
- **Markdown**: Source format for further editing
- **Typst**: Source code for the PDF generation

## Customization

### Themes

The project uses the `moderncv` theme by default. You can change themes by modifying the conversion script or the generated YAML files.

Available themes include:
- `moderncv`
- `sb2nov`
- `classic`
- `engineeringresumes`

### Colors and Styling

Modify the `design` section in the YAML files or update the conversion script to change:
- Colors
- Fonts
- Page margins
- Layout options

## Dependencies

- `rendercv`: CV generation framework
- `pyyaml`: YAML processing