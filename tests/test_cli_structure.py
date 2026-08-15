import ast
from pathlib import Path

def test_cli_is_import_safe_and_has_main_function():
    tree=ast.parse((Path(__file__).parents[1]/"main.py").read_text())
    assert any(isinstance(n,ast.FunctionDef) and n.name=="main" for n in tree.body)
    assert any(isinstance(n,ast.If) for n in tree.body)
