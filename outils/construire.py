"""Assemble des fichiers Markdown en un PDF (Markdown vers HTML, puis Chrome sans interface).
Usage : python outils/construire.py "Titre" sortie.pdf fichier1.md [fichier2.md ...]
Dépendance : le paquet Python `markdown` (voir requirements.txt) et Google Chrome."""
import subprocess, sys, tempfile, pathlib, markdown

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CSS = """
@page { size: A4; margin: 18mm 17mm 18mm 17mm; }
body { font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif; font-size: 10.6pt; line-height: 1.45; color: #1c1c1c; }
h1 { font-size: 20pt; margin: 0 0 6pt; } h2 { font-size: 13.5pt; margin: 12pt 0 4pt; border-bottom: 1px solid #999; padding-bottom: 2pt; }
h3 { font-size: 11pt; margin: 8pt 0 2pt; } p { margin: 3pt 0 5pt; } li { margin: 1pt 0; }
table { border-collapse: collapse; width: 100%; margin: 5pt 0 7pt; font-size: 9pt; page-break-inside: auto; }
tr { page-break-inside: avoid; } th, td { border: 1px solid #aaa; padding: 2.5pt 4pt; vertical-align: top; text-align: left; }
th { background: #eee; } blockquote { border-left: 3px solid #b33; margin: 6pt 0; padding: 3pt 8pt; background: #fbf1f1; }
code { font-size: 8.4pt; } section.s { page-break-before: always; } section.first { page-break-before: auto; }
"""

def main():
    titre, out, *files = sys.argv[1:]
    parts = []
    for i, f in enumerate(files):
        html = markdown.markdown(pathlib.Path(f).read_text(encoding="utf-8").split("---\n", 2)[-1] if pathlib.Path(f).read_text(encoding="utf-8").startswith("---\n") else pathlib.Path(f).read_text(encoding="utf-8"), extensions=["tables"])
        parts.append(f'<section class="{"first" if i == 0 else "c"}">{html}</section>')
    doc = f'<!doctype html><html lang="fr"><meta charset="utf-8"><title>{titre}</title><style>{CSS}</style><body>{"".join(parts)}</body></html>'
    with tempfile.TemporaryDirectory() as d:
        h = pathlib.Path(d) / "d.html"; h.write_text(doc, encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pathlib.Path(out).resolve()}", h.as_uri()],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)

if __name__ == "__main__":
    main()
