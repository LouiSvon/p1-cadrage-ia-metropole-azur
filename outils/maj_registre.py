"""Réécrit le bloc des valeurs calculées (D) de registre.md à partir de calcul/business_case.py."""
import pathlib, re, subprocess, sys
racine = pathlib.Path(__file__).resolve().parent.parent
bloc = subprocess.run([sys.executable, str(racine / "calcul" / "business_case.py"), "--registre"], check=True, capture_output=True, text=True).stdout.strip()
p = racine / "registre.md"
txt = p.read_text(encoding="utf-8")
nouveau = re.sub(r"(<!-- D:debut -->\n).*?(\n<!-- D:fin -->)", lambda m: m.group(1) + bloc + m.group(2), txt, flags=re.S)
assert nouveau != txt or bloc in txt, "marqueurs D absents"
p.write_text(nouveau, encoding="utf-8")
