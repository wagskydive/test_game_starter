import os, sys
sys.path.insert(0, os.path.abspath('src'))

from llm_integration import generate_dialogue


def test_generate_dialogue_enabled():
    text = generate_dialogue('hello')
    assert text.startswith('[LLM]')


def test_generate_dialogue_disabled(monkeypatch):
    monkeypatch.setenv('DISABLE_LLM', '1')
    assert generate_dialogue('hi') is None
