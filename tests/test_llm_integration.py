import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.llm_integration import generate_dialogue, load_offline_model


def test_generate_dialogue_enabled():
    text = generate_dialogue('hello')
    assert text.startswith('[LLM]')


def test_generate_dialogue_disabled(monkeypatch):
    monkeypatch.setenv('DISABLE_LLM', '1')
    assert generate_dialogue('hi') is None


def test_generate_dialogue_offline(tmp_path):
    model = tmp_path / "model.bin"
    model.write_text("dummy")
    assert load_offline_model(str(model))
    text = generate_dialogue('quest')
    assert text.startswith('[OFFLINE_LLM]')
