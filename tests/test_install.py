"""Tests for graphify install --platform routing."""
import json
import os
from pathlib import Path
import sys
from unittest.mock import patch
import pytest


PLATFORMS = {
    "claude": (".claude/skills/graphify/SKILL.md",),
    "codex": (".agents/skills/graphify/SKILL.md",),
    "opencode": (".config/opencode/skills/graphify/SKILL.md",),
    "claw": (".openclaw/skills/graphify/SKILL.md",),
    "droid": (".factory/skills/graphify/SKILL.md",),
    "trae": (".trae/skills/graphify/SKILL.md",),
    "trae-cn": (".trae-cn/skills/graphify/SKILL.md",),
    "windows": (".claude/skills/graphify/SKILL.md",),
}


def _install(tmp_path, platform):
    from graphify.__main__ import install
    old_cwd = Path.cwd()
    try:
        os.chdir(tmp_path)
        with patch("graphify.__main__.Path.home", return_value=tmp_path):
            install(platform=platform)
    finally:
        os.chdir(old_cwd)


def _run_main(tmp_path, argv):
    from graphify.__main__ import main
    old_cwd = Path.cwd()
    try:
        os.chdir(tmp_path)
        with patch("graphify.__main__.Path.home", return_value=tmp_path), patch.object(sys, "argv", argv):
            result = main()
    finally:
        os.chdir(old_cwd)
    assert result in (None, 0)


def test_install_default_claude(tmp_path):
    _install(tmp_path, "claude")
    assert (tmp_path / ".claude" / "skills" / "graphify" / "SKILL.md").exists()


def test_install_codex(tmp_path):
    _install(tmp_path, "codex")
    assert (tmp_path / ".agents" / "skills" / "graphify" / "SKILL.md").exists()


def test_install_opencode(tmp_path):
    _install(tmp_path, "opencode")
    assert (tmp_path / ".config" / "opencode" / "skills" / "graphify" / "SKILL.md").exists()


def test_install_positional_platform_opencode(tmp_path, monkeypatch):
    from graphify.__main__ import main
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["graphify", "install", "opencode"])
    with patch("graphify.__main__.Path.home", return_value=tmp_path):
        main()
    assert (tmp_path / ".config" / "opencode" / "skills" / "graphify" / "SKILL.md").exists()
    assert not (tmp_path / ".claude" / "skills" / "graphify" / "SKILL.md").exists()


def test_install_help_does_not_install_default(tmp_path, monkeypatch, capsys):
    from graphify.__main__ import main
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["graphify", "install", "opencode", "--help"])
    with patch("graphify.__main__.Path.home", return_value=tmp_path):
        main()
    out = capsys.readouterr().out
    assert "Usage: graphify install" in out
    assert "opencode" in out
    assert not (tmp_path / ".claude").exists()
    assert not (tmp_path / ".config").exists()


def test_install_claw(tmp_path):
    _install(tmp_path, "claw")
    assert (tmp_path / ".openclaw" / "skills" / "graphify" / "SKILL.md").exists()


def test_install_droid(tmp_path):
    _install(tmp_path, "droid")
    assert (tmp_path / ".factory" / "skills" / "graphify" / "SKILL.md").exists()


def test_install_trae(tmp_path):
    _install(tmp_path, "trae")
    assert (tmp_path / ".trae" / "skills" / "graphify" / "SKILL.md").exists()


def test_install_trae_cn(tmp_path):
    _install(tmp_path, "trae-cn")
    assert (tmp_path / ".trae-cn" / "skills" / "graphify" / "SKILL.md").exists()


def test_install_windows(tmp_path):
    _install(tmp_path, "windows")
    assert (tmp_path / ".claude" / "skills" / "graphify" / "SKILL.md").exists()


def test_install_unknown_platform_exits(tmp_path):
    with pytest.raises(SystemExit):
        _install(tmp_path, "unknown")


def test_legacy_install_parser_accepts_default_and_platform_forms():
    from graphify.__main__ import _parse_install_args

    assert _parse_install_args([]) == "claude"
    assert _parse_install_args(["codex"]) == "codex"
    assert _parse_install_args(["--platform", "codex"]) == "codex"
    assert _parse_install_args(["--platform=codex"]) == "codex"


def test_legacy_install_parser_uses_windows_default():
    from graphify.__main__ import _parse_install_args

    with patch("graphify.__main__.platform.system", return_value="Windows"):
        assert _parse_install_args([]) == "windows"


def test_named_command_parser_accepts_setup_and_remove_forms():
    from graphify.__main__ import _parse_named_command_args

    assert _parse_named_command_args([]) == (None, False)
    assert _parse_named_command_args(["codex"]) == ("codex", False)
    assert _parse_named_command_args(["install", "codex"]) == ("codex", False)
    assert _parse_named_command_args(["remove", "codex"]) == ("codex", True)
    assert _parse_named_command_args(["codex", "remove"]) == ("codex", True)


def test_cli_skill_codex_installs_user_skill_only(tmp_path):
    _run_main(tmp_path, ["graphify", "skill", "codex"])

    assert (tmp_path / ".agents" / "skills" / "graphify" / "SKILL.md").exists()
    assert not (tmp_path / "AGENTS.md").exists()
    assert not (tmp_path / ".codex" / "hooks.json").exists()


def test_cli_setup_codex_configures_project_only(tmp_path):
    _run_main(tmp_path, ["graphify", "setup", "codex"])

    assert (tmp_path / "AGENTS.md").exists()
    hooks_path = tmp_path / ".codex" / "hooks.json"
    assert hooks_path.exists()
    hooks = json.loads(hooks_path.read_text(encoding="utf-8"))["hooks"]
    assert hooks["SessionStart"] == [{
        "hooks": [{"type": "command", "command": "graphify hook-check"}],
    }]
    assert not (tmp_path / ".agents" / "skills" / "graphify" / "SKILL.md").exists()


def test_cli_install_positional_platform_is_deprecated_skill_alias(tmp_path, capsys):
    _run_main(tmp_path, ["graphify", "install", "codex"])

    captured = capsys.readouterr()
    assert "deprecated alias" in captured.err
    assert (tmp_path / ".agents" / "skills" / "graphify" / "SKILL.md").exists()
    assert not (tmp_path / "AGENTS.md").exists()


def test_cli_platform_install_is_deprecated_setup_alias(tmp_path, capsys):
    _run_main(tmp_path, ["graphify", "codex", "install"])

    captured = capsys.readouterr()
    assert "deprecated alias" in captured.err
    assert (tmp_path / "AGENTS.md").exists()
    assert not (tmp_path / ".agents" / "skills" / "graphify" / "SKILL.md").exists()


def test_cli_skill_and_setup_help_have_no_side_effects(tmp_path, capsys):
    _run_main(tmp_path, ["graphify", "skill", "codex", "--help"])
    _run_main(tmp_path, ["graphify", "setup", "codex", "--help"])

    captured = capsys.readouterr()
    assert "Usage: graphify skill" in captured.out
    assert "Usage: graphify setup" in captured.out
    assert not (tmp_path / ".agents").exists()
    assert not (tmp_path / "AGENTS.md").exists()


def test_install_platforms_copy_shared_skill_source(tmp_path):
    """All platform installers copy the shared skill source."""
    import graphify
    shared = (Path(graphify.__file__).parent / "skill.md").read_text()
    for platform, paths in PLATFORMS.items():
        root = tmp_path / platform
        root.mkdir()
        _install(root, platform)
        installed = root / paths[0]
        assert installed.read_text() == shared


def test_shared_skill_documents_platform_adapter_table():
    """Platform differences live in one shared skill as an adapter table."""
    import graphify
    skill = (Path(graphify.__file__).parent / "skill.md").read_text()
    assert "## Platform Adapter Table" in skill
    assert "| Agent | Instruction file | Runtime hook | Semantic extraction adapter |" in skill
    for name in ("Claude Code", "Codex", "OpenCode", "Cursor", "Gemini"):
        assert name in skill


def test_shared_skill_documents_kimi_fast_path():
    """The shared skill documents direct Kimi extraction before subagent fallback."""
    import graphify
    skill = (Path(graphify.__file__).parent / "skill.md").read_text()
    assert "MOONSHOT_API_KEY" in skill
    assert "Kimi fast path" in skill
    assert 'backend="kimi"' in skill
    assert "graphifyy[kimi]" in skill


def test_all_skill_files_exist_in_package():
    """Legacy platform skill files remain packaged for compatibility/reference."""
    import graphify
    pkg = Path(graphify.__file__).parent
    for name in ("skill.md", "skill-codex.md", "skill-opencode.md", "skill-claw.md", "skill-windows.md", "skill-droid.md", "skill-trae.md"):
        assert (pkg / name).exists(), f"Missing: {name}"


def test_project_instruction_templates_share_core():
    """Generated project instruction files use the same graphify rule core."""
    from graphify.__main__ import (
        _AGENTS_MD_SECTION,
        _ANTIGRAVITY_RULES,
        _CLAUDE_MD_SECTION,
        _CURSOR_RULE,
        _GEMINI_MD_SECTION,
        _GRAPHIFY_INSTRUCTION_BODY,
        _KIRO_STEERING,
        _VSCODE_INSTRUCTIONS_SECTION,
    )

    for section in (
        _CLAUDE_MD_SECTION,
        _AGENTS_MD_SECTION,
        _GEMINI_MD_SECTION,
        _VSCODE_INSTRUCTIONS_SECTION,
        _ANTIGRAVITY_RULES,
        _KIRO_STEERING,
        _CURSOR_RULE,
    ):
        assert _GRAPHIFY_INSTRUCTION_BODY in section


def test_claude_install_registers_claude_md(tmp_path):
    """Claude platform install writes CLAUDE.md; others do not."""
    _install(tmp_path, "claude")
    assert (tmp_path / ".claude" / "CLAUDE.md").exists()


def test_codex_install_does_not_write_claude_md(tmp_path):
    _install(tmp_path, "codex")
    assert not (tmp_path / ".claude" / "CLAUDE.md").exists()


# --- always-on AGENTS.md install/uninstall tests ---

def _agents_install(tmp_path, platform):
    from graphify.__main__ import _agents_install as _install_fn
    _install_fn(tmp_path, platform)


def _agents_uninstall(tmp_path, platform=""):
    from graphify.__main__ import _agents_uninstall as _uninstall_fn
    _uninstall_fn(tmp_path, platform=platform)


def test_codex_agents_install_writes_agents_md(tmp_path):
    _agents_install(tmp_path, "codex")
    agents_md = tmp_path / "AGENTS.md"
    assert agents_md.exists()
    assert "graphify" in agents_md.read_text()
    assert "GRAPH_REPORT.md" in agents_md.read_text()


def test_opencode_agents_install_writes_agents_md(tmp_path):
    _agents_install(tmp_path, "opencode")
    assert (tmp_path / "AGENTS.md").exists()


def test_claw_agents_install_writes_agents_md(tmp_path):
    _agents_install(tmp_path, "claw")
    assert (tmp_path / "AGENTS.md").exists()


def test_agents_install_idempotent(tmp_path):
    """Installing twice does not duplicate the section."""
    _agents_install(tmp_path, "codex")
    _agents_install(tmp_path, "codex")
    content = (tmp_path / "AGENTS.md").read_text()
    assert content.count("## graphify") == 1


def test_agents_install_appends_to_existing(tmp_path):
    """Installs into an existing AGENTS.md without overwriting other content."""
    agents_md = tmp_path / "AGENTS.md"
    agents_md.write_text("# Existing rules\n\nDo not break things.\n")
    _agents_install(tmp_path, "codex")
    content = agents_md.read_text()
    assert "Do not break things." in content
    assert "## graphify" in content


def test_agents_uninstall_removes_section(tmp_path):
    _agents_install(tmp_path, "codex")
    _agents_uninstall(tmp_path)
    agents_md = tmp_path / "AGENTS.md"
    # File deleted when it only contained graphify section
    assert not agents_md.exists()


def test_agents_uninstall_preserves_other_content(tmp_path):
    """Uninstall keeps pre-existing content."""
    agents_md = tmp_path / "AGENTS.md"
    agents_md.write_text("# Existing rules\n\nDo not break things.\n")
    _agents_install(tmp_path, "codex")
    _agents_uninstall(tmp_path)
    assert agents_md.exists()
    content = agents_md.read_text()
    assert "Do not break things." in content
    assert "## graphify" not in content


def test_agents_uninstall_no_op_when_not_installed(tmp_path, capsys):
    _agents_uninstall(tmp_path)
    out = capsys.readouterr().out
    assert "nothing to do" in out


# --- OpenCode plugin tests ---

def test_opencode_agents_install_writes_plugin(tmp_path):
    """opencode install writes .opencode/plugins/graphify.js."""
    _agents_install(tmp_path, "opencode")
    plugin = tmp_path / ".opencode" / "plugins" / "graphify.js"
    assert plugin.exists()
    assert "tool.execute.before" in plugin.read_text()


def test_opencode_agents_install_registers_plugin_in_config(tmp_path):
    """opencode install registers the plugin in .opencode/opencode.json."""
    _agents_install(tmp_path, "opencode")
    config_file = tmp_path / ".opencode" / "opencode.json"
    assert config_file.exists()
    import json as _json
    config = _json.loads(config_file.read_text())
    assert any("graphify.js" in p for p in config.get("plugin", []))


def test_opencode_agents_install_merges_existing_config(tmp_path):
    """opencode install preserves existing .opencode/opencode.json keys."""
    import json as _json
    config_file = tmp_path / ".opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(_json.dumps({"model": "claude-opus-4-5", "plugin": []}))
    _agents_install(tmp_path, "opencode")
    config = _json.loads(config_file.read_text())
    assert config["model"] == "claude-opus-4-5"
    assert any("graphify.js" in p for p in config["plugin"])


def test_opencode_agents_uninstall_removes_plugin(tmp_path):
    """opencode uninstall removes the plugin file and deregisters from opencode.json."""
    import json as _json
    _agents_install(tmp_path, "opencode")
    _agents_uninstall(tmp_path, platform="opencode")
    plugin = tmp_path / ".opencode" / "plugins" / "graphify.js"
    assert not plugin.exists()
    config_file = tmp_path / ".opencode" / "opencode.json"
    if config_file.exists():
        config = _json.loads(config_file.read_text())
        assert not any("graphify.js" in p for p in config.get("plugin", []))


# ── Cursor ────────────────────────────────────────────────────────────────────

def test_cursor_install_writes_rule(tmp_path):
    """cursor install writes .cursor/rules/graphify.mdc."""
    from graphify.__main__ import _cursor_install
    _cursor_install(tmp_path)
    rule = tmp_path / ".cursor" / "rules" / "graphify.mdc"
    assert rule.exists()
    content = rule.read_text()
    assert "alwaysApply: true" in content
    assert "graphify-out/GRAPH_REPORT.md" in content


def test_cursor_install_idempotent(tmp_path):
    """cursor install does not overwrite an existing rule file."""
    from graphify.__main__ import _cursor_install
    _cursor_install(tmp_path)
    rule = tmp_path / ".cursor" / "rules" / "graphify.mdc"
    original = rule.read_text()
    _cursor_install(tmp_path)
    assert rule.read_text() == original


def test_cursor_uninstall_removes_rule(tmp_path):
    """cursor uninstall removes the rule file."""
    from graphify.__main__ import _cursor_install, _cursor_uninstall
    _cursor_install(tmp_path)
    _cursor_uninstall(tmp_path)
    rule = tmp_path / ".cursor" / "rules" / "graphify.mdc"
    assert not rule.exists()


def test_cursor_uninstall_noop_if_not_installed(tmp_path):
    """cursor uninstall does nothing if rule was never written."""
    from graphify.__main__ import _cursor_uninstall
    _cursor_uninstall(tmp_path)  # should not raise


# ── Gemini CLI ────────────────────────────────────────────────────────────────

def test_gemini_install_writes_gemini_md(tmp_path):
    from graphify.__main__ import gemini_install
    gemini_install(tmp_path)
    md = tmp_path / "GEMINI.md"
    assert md.exists()
    assert "graphify-out/GRAPH_REPORT.md" in md.read_text()

def test_gemini_install_writes_hook(tmp_path):
    import json as _json
    from graphify.__main__ import gemini_install
    gemini_install(tmp_path)
    settings = _json.loads((tmp_path / ".gemini" / "settings.json").read_text())
    hooks = settings["hooks"]["BeforeTool"]
    assert any("graphify" in str(h) for h in hooks)

def test_gemini_install_idempotent(tmp_path):
    from graphify.__main__ import gemini_install
    gemini_install(tmp_path)
    gemini_install(tmp_path)
    md = tmp_path / "GEMINI.md"
    assert md.read_text().count("## graphify") == 1

def test_gemini_install_merges_existing_gemini_md(tmp_path):
    from graphify.__main__ import gemini_install
    (tmp_path / "GEMINI.md").write_text("# My project rules\n")
    gemini_install(tmp_path)
    content = (tmp_path / "GEMINI.md").read_text()
    assert "# My project rules" in content
    assert "graphify-out/GRAPH_REPORT.md" in content

def test_gemini_uninstall_removes_section(tmp_path):
    from graphify.__main__ import gemini_install, gemini_uninstall
    gemini_install(tmp_path)
    gemini_uninstall(tmp_path)
    md = tmp_path / "GEMINI.md"
    assert not md.exists()

def test_gemini_uninstall_removes_hook(tmp_path):
    import json as _json
    from graphify.__main__ import gemini_install, gemini_uninstall
    gemini_install(tmp_path)
    gemini_uninstall(tmp_path)
    settings_path = tmp_path / ".gemini" / "settings.json"
    if settings_path.exists():
        settings = _json.loads(settings_path.read_text())
        hooks = settings.get("hooks", {}).get("BeforeTool", [])
        assert not any("graphify" in str(h) for h in hooks)

def test_gemini_uninstall_noop_if_not_installed(tmp_path):
    from graphify.__main__ import gemini_uninstall
    gemini_uninstall(tmp_path)  # should not raise
