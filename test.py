import os
import sys
from run import generate_constraints, solve_game

USAGE = '\n\tpython3 test.py [draft|final]\n'
EXPECTED_VAR_MIN = 10
EXPECTED_CONS_MIN = 50

def test_theory():
    constraints = generate_constraints()
    solution = solve_game()

    assert len(constraints) > EXPECTED_VAR_MIN, "Only %d constraints -- your theory is likely not sophisticated enough for the course project." % len(constraints)
    assert solution, "No valid solution found -- check your constraints and game setup."
    assert any(solution[var] for var in solution), "All variables are False -- solution may not be meaningful."

def file_checks(stage):
    proofs_jp = os.path.isfile(os.path.join('.', 'documents', stage, 'proofs.jp'))
    modelling_report_docx = os.path.isfile(os.path.join('.', 'documents', stage, 'modelling_report.docx'))
    modelling_report_pptx = os.path.isfile(os.path.join('.', 'documents', stage, 'modelling_report.pptx'))
    report_txt = os.path.isfile(os.path.join('.', 'documents', stage, 'report.txt'))
    report_pdf = os.path.isfile(os.path.join('.', 'documents', stage, 'report.pdf'))

    assert proofs_jp, "Missing proofs.jp in your %s folder." % stage
    assert modelling_report_docx or modelling_report_pptx or (report_txt and report_pdf), \
        "Missing your report (Word, PowerPoint, or OverLeaf) in your %s folder" % stage

def test_draft_files():
    file_checks('draft')

def test_final_files():
    file_checks('final')

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['draft', 'final']:
        print(USAGE)
        exit(1)
    test_theory()
    file_checks(sys.argv[1])
