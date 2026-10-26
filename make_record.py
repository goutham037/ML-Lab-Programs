# Build a combined Word lab record: Aim + Program + Output (+ plot) per task.
import os, glob
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "outputs")
FONT = "Times New Roman"

AIMS = {
    "task01": "To write a Python program to import and export data using Pandas library functions.",
    "task02": "To demonstrate various data preprocessing techniques for a given dataset.",
    "task03": "To implement dimensionality reduction using Principal Component Analysis (PCA).",
    "task04": "To write a Python program to demonstrate various data visualization techniques.",
    "task05": "To implement Simple and Multiple Linear Regression models.",
    "task06": "To develop a Logistic Regression model for a given dataset.",
    "task07": "To develop a Decision Tree classification model and classify a new sample.",
    "task08": "To implement Naive Bayes classification in Python for a given dataset.",
    "task09": "To build a KNN classification model in Python for a given dataset.",
    "task10": "To implement a Back Propagation model in Python for a given dataset.",
    "task11": "To implement Random Forest classification and a Boosting ensemble method.",
    "task12a": "To write a Python program to implement the K-Means clustering algorithm.",
    "task12b": "To write a Python program to implement the BIRCH clustering algorithm.",
}

doc = Document()
s = doc.styles["Normal"]
s.font.name = FONT
s.font.size = Pt(12)
rpr = s.element.get_or_add_rPr()
rf = OxmlElement("w:rFonts")
for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
    rf.set(qn(a), FONT)
rpr.insert(0, rf)
for h, sz in (("Heading 1", 15), ("Heading 2", 13)):
    st = doc.styles[h]; st.font.name = FONT; st.font.size = Pt(sz)
    st.font.color.rgb = RGBColor(0x1F, 0x33, 0x5B)


def P(t="", align=None, bold=False, size=None):
    p = doc.add_paragraph(); r = p.add_run(t)
    r.font.name = FONT; r.bold = bold
    if size: r.font.size = Pt(size)
    if align == "c": p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p


def code(text):
    for ln in text.rstrip().split("\n"):
        p = doc.add_paragraph(); r = p.add_run(ln if ln else " ")
        r.font.name = "Consolas"; r.font.size = Pt(9.5)
        p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0


# ---- Title page ----
P("MACHINE LEARNING LABORATORY", align="c", bold=True, size=20)
P("RECORD OF PROGRAMS", align="c", bold=True, size=16)
P("")
P("Department of Computer Science and Engineering", align="c", size=13)
P("Gokaraju Rangaraju Institute of Engineering and Technology", align="c", size=12)
P("")
P("Reference: Python Machine Learning — Sebastian Raschka, O'Reilly", align="c", size=11)
doc.add_page_break()

files = sorted(glob.glob(os.path.join(HERE, "task*.py")))
for i, path in enumerate(files, 1):
    base = os.path.basename(path)
    key = base.split("_")[0]
    if key not in AIMS:  # task12a/task12b
        key = base[:7]
    doc.add_heading(f"Experiment {i}", level=1)
    doc.add_heading("Aim", level=2)
    P(AIMS.get(key, ""))
    doc.add_heading("Program", level=2)
    code(open(path, encoding="utf-8").read())
    doc.add_heading("Output", level=2)
    txt = os.path.join(OUT, base.replace(".py", "_output.txt"))
    if os.path.exists(txt):
        out = open(txt, encoding="utf-8").read().strip()
        code(out if out else "(program produced plots only)")
    # embed plots if any
    plots = sorted(glob.glob(os.path.join(OUT, base.replace(".py", "") + "_fig*.png")))
    for pl in plots:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(pl, width=Inches(4.5))
    doc.add_page_break()

dst = os.path.join(HERE, "ML_Lab_Record.docx")
doc.save(dst)
print("saved", dst, "| experiments:", len(files))
