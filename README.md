<p align="center">
  <a href="https://graphifylabs.ai"><img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/></a>
</p>

<p align="center">
  🇺🇸 <a href="README.md">English</a> | 🇨🇳 <a href="docs/translations/README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="docs/translations/README.ja-JP.md">日本語</a> | 🇰🇷 <a href="docs/translations/README.ko-KR.md">한국어</a> | 🇩🇪 <a href="docs/translations/README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="docs/translations/README.fr-FR.md">Français</a> | 🇪🇸 <a href="docs/translations/README.es-ES.md">Español</a> | 🇮🇳 <a href="docs/translations/README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="docs/translations/README.pt-BR.md">Português</a> | 🇷🇺 <a href="docs/translations/README.ru-RU.md">Русский</a> | 🇸🇦 <a href="docs/translations/README.ar-SA.md">العربية</a> | 🇮🇹 <a href="docs/translations/README.it-IT.md">Italiano</a> | 🇵🇱 <a href="docs/translations/README.pl-PL.md">Polski</a> | 🇳🇱 <a href="docs/translations/README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="docs/translations/README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="docs/translations/README.uk-UA.md">Українська</a> | 🇻🇳 <a href="docs/translations/README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="docs/translations/README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="docs/translations/README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="docs/translations/README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="docs/translations/README.ro-RO.md">Română</a> | 🇨🇿 <a href="docs/translations/README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="docs/translations/README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="docs/translations/README.da-DK.md">Dansk</a> | 🇳🇴 <a href="docs/translations/README.no-NO.md">Norsk</a> | 🇭🇺 <a href="docs/translations/README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="docs/translations/README.th-TH.md">ภาษาไทย</a> | 🇹🇼 <a href="docs/translations/README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://safishamsi.gumroad.com/l/qetvlo"><img src="https://img.shields.io/badge/Book-The%20Memory%20Layer-2ea44f?style=flat&logo=gitbook&logoColor=white" alt="The Memory Layer"/></a>
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v7" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
  <a href="https://www.linkedin.com/in/safi-shamsi"><img src="https://img.shields.io/badge/LinkedIn-Safi%20Shamsi-0077B5?logo=linkedin" alt="LinkedIn"/></a>
</p>

<p align="center">
  <a href="https://star-history.com/#safishamsi/graphify&Date">
    <img src="https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date" alt="Star History Chart" width="600"/>
  </a>
</p>

Type `/graphify` in your AI coding assistant and it maps your entire project — code, docs, PDFs, images, videos — into a knowledge graph you can query instead of grepping through files.

Works in Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro, Pi, and Google Antigravity.

```
/graphify .
```

That's it. You get three files:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

---

## Install

**Requires Python 3.10+**

```bash
uv tool install graphifyy
# or: pipx install graphifyy
# or: pip install graphifyy
```

> **Official package:** The PyPI package is `graphifyy` (double-y). Other `graphify*` packages on PyPI are not affiliated. The CLI command is still `graphify`.

> **`graphify: command not found`?** Use `uv tool install graphifyy` or `pipx install graphifyy` — both put the CLI on PATH automatically. With plain `pip`, add `~/.local/bin` (Linux) or `~/Library/Python/3.x/bin` (Mac) to your PATH, or run `python -m graphify`.

### Pick your platform

Install or refresh the user-level assistant skill:

| Platform | Install command |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify skill claude` |
| Claude Code (Windows) | `graphify skill windows` |
| Codex | `graphify skill codex` |
| OpenCode | `graphify skill opencode` |
| GitHub Copilot CLI | `graphify skill copilot` |
| VS Code Copilot Chat | `graphify skill vscode` |
| Aider | `graphify skill aider` |
| OpenClaw | `graphify skill claw` |
| Factory Droid | `graphify skill droid` |
| Trae | `graphify skill trae` |
| Trae CN | `graphify skill trae-cn` |
| Gemini CLI | `graphify skill gemini` |
| Hermes | `graphify skill hermes` |
| Kiro IDE/CLI | `graphify skill kiro` |
| Pi coding agent | `graphify skill pi` |
| Google Antigravity | `graphify skill antigravity` |

Deprecated aliases still work for compatibility: `graphify install`, `graphify install <platform>`, and `graphify install --platform <platform>`.

> Codex users: also add `multi_agent = true` under `[features]` in `~/.codex/config.toml`.
> Codex uses `$graphify` instead of `/graphify`.

---

## Make your assistant always use the graph

Run this once in your project after building a graph:

| Platform | Command |
|----------|---------|
| Claude Code | `graphify setup claude` |
| Codex | `graphify setup codex` |
| OpenCode | `graphify setup opencode` |
| GitHub Copilot CLI | `graphify setup copilot` |
| VS Code Copilot Chat | `graphify setup vscode` |
| Aider | `graphify setup aider` |
| OpenClaw | `graphify setup claw` |
| Factory Droid | `graphify setup droid` |
| Trae | `graphify setup trae` |
| Trae CN | `graphify setup trae-cn` |
| Cursor | `graphify setup cursor` |
| Gemini CLI | `graphify setup gemini` |
| Hermes | `graphify setup hermes` |
| Kiro IDE/CLI | `graphify setup kiro` |
| Pi coding agent | `graphify setup pi` |
| Google Antigravity | `graphify setup antigravity` |

Deprecated platform-first aliases still work for compatibility, for example `graphify codex install` and `graphify codex uninstall`.

This writes project-level assistant instructions that point to `GRAPH_REPORT.md` before raw file search. On platforms that support hooks, graphify also installs reminders or guards so the assistant sees the graph context before it starts grepping through files. Claude Code gets a `UserPromptSubmit` reminder and a `PreToolUse` guard that blocks raw search/read/list tools until the graph is used in the session.

Uninstall with the matching command (e.g. `graphify setup remove codex`).

---

## What's in the report

- **God nodes** — the most-connected concepts in your project. Everything flows through these.
- **Surprising connections** — links between things that live in different files or modules. Ranked by how unexpected they are.
- **The "why"** — inline comments (`# NOTE:`, `# WHY:`, `# HACK:`), docstrings, and design rationale from docs are extracted as separate nodes linked to the code they explain.
- **Suggested questions** — 4–5 questions the graph is uniquely positioned to answer.
- **Confidence tags** — every inferred relationship is marked `EXTRACTED`, `INFERRED`, or `AMBIGUOUS`. You always know what was found vs guessed.

---

## What files it handles

| Type | Extensions |
|------|-----------|
| Code (28 languages) | `.py .ts .js .jsx .tsx .go .rs .java .c .cpp .rb .cs .kt .scala .php .swift .lua .luau .zig .ps1 .ex .exs .m .jl .vue .svelte .groovy .gradle .sql .f .F .f90 .F90 .f95 .F95 .f03 .F03 .f08 .F08` |
| Docs | `.md .mdx .html .txt .rst .yaml .yml` |
| Office | `.docx .xlsx` (requires `pip install graphifyy[office]`) |
| PDFs | `.pdf` |
| Images | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` and more (requires `pip install graphifyy[video]`) |
| YouTube / URLs | any video URL (requires `pip install graphifyy[video]`) |

Code is extracted locally with no API calls (AST via tree-sitter). Everything else goes through your AI assistant's model API.

---

## Common commands

```bash
/graphify .                        # build graph for current folder
/graphify ./docs --update          # re-extract only changed files
/graphify . --cluster-only         # rerun clustering without re-extracting
/graphify . --no-viz               # skip the HTML, just the report + JSON
/graphify . --wiki                 # build a markdown wiki from the graph

/graphify query "what connects auth to the database?"
/graphify path "UserService" "DatabasePool"
/graphify explain "RateLimiter"

/graphify add https://arxiv.org/abs/1706.03762   # fetch a paper and add it
/graphify add <youtube-url>                       # transcribe and add a video

graphify hook install              # auto-rebuild on git commit
graphify merge-graphs a.json b.json              # combine two graphs
```

See the [full command reference](#full-command-reference) below.

---

## Ignoring files

Create a `.graphifyignore` in your project root — same syntax as `.gitignore`, including `!` negation:

```
# .graphifyignore
node_modules/
dist/
*.generated.py

# only index src/, ignore everything else
*
!src/
!src/**
```

---

## Team setup

`graphify-out/` is meant to be committed to git so everyone on the team starts with a map.

**Recommended `.gitignore` additions:**
```
graphify-out/manifest.json    # mtime-based, breaks after git clone
graphify-out/cost.json        # local only
# graphify-out/cache/         # optional: commit for speed, skip to keep repo small
```

**Workflow:**
1. One person runs `/graphify .` and commits `graphify-out/`.
2. Everyone pulls — their assistant reads the graph immediately.
3. Run `graphify hook install` to auto-rebuild after each commit (AST only, no API cost). This also sets up a git merge driver so `graph.json` is never left with conflict markers — two devs committing in parallel get their graphs union-merged automatically.
4. When docs or papers change, run `/graphify --update` to refresh those nodes.

---

## Using the graph directly

```bash
# query the graph from the terminal
graphify query "show the auth flow"
graphify query "what connects DigestAuth to Response?" --graph graphify-out/graph.json

# expose the graph as an MCP server (for repeated tool-call access)
python -m graphify.serve graphify-out/graph.json
```

The MCP server gives your assistant structured access: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`.

> **WSL / Linux note:** Ubuntu ships `python3`, not `python`. Use a venv to avoid conflicts:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "graphifyy[mcp]"
> ```

---

## Privacy

- **Code files** — processed locally via tree-sitter. Nothing leaves your machine.
- **Video / audio** — transcribed locally with faster-whisper. Nothing leaves your machine.
- **Docs, PDFs, images** — sent to your AI assistant for semantic extraction (via the `/graphify` skill, using whatever model your IDE session runs). Headless `graphify extract` requires `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), or a running Ollama instance (`OLLAMA_BASE_URL`). The `--dedup-llm` flag uses the same key.
- No telemetry, no usage tracking, no analytics.

---

## Full command reference

```
/graphify                          # run on current directory
/graphify ./raw                    # run on a specific folder
/graphify ./raw --mode deep        # more aggressive relationship extraction
/graphify ./raw --update           # re-extract only changed files
/graphify ./raw --directed         # preserve edge direction
/graphify ./raw --cluster-only     # rerun clustering on existing graph
/graphify ./raw --no-viz           # skip HTML visualization
/graphify ./raw --obsidian         # generate Obsidian vault
/graphify ./raw --wiki             # build agent-crawlable markdown wiki
/graphify ./raw --svg              # export graph.svg
/graphify ./raw --graphml          # export for Gephi / yEd
/graphify ./raw --neo4j            # generate cypher.txt for Neo4j
/graphify ./raw --neo4j-push bolt://localhost:7687
/graphify ./raw --watch            # auto-sync as files change
/graphify ./raw --mcp              # start MCP stdio server

# user-level assistant skills
graphify skill claude                  # ~/.claude/skills/graphify/SKILL.md
graphify skill codex                   # ~/.agents/skills/graphify/SKILL.md
graphify skill opencode                # ~/.config/opencode/skills/graphify/SKILL.md
graphify skill vscode                  # ~/.copilot/skills/graphify/SKILL.md
graphify skill remove codex

# current-project assistant setup
graphify setup claude                  # CLAUDE.md + UserPromptSubmit reminder + PreToolUse guard
graphify setup codex                   # AGENTS.md + .codex/hooks.json
graphify setup opencode                # AGENTS.md + tool.execute.before plugin
graphify setup cursor                  # .cursor/rules/graphify.mdc
graphify setup gemini                  # GEMINI.md + BeforeTool hook
graphify setup vscode                  # .github/copilot-instructions.md + VS Code skill
graphify setup remove codex

# deprecated aliases kept for compatibility
graphify install codex                 # deprecated alias for: graphify skill codex
graphify install --platform codex      # deprecated alias for: graphify skill codex
graphify codex install                 # deprecated alias for: graphify setup codex
graphify codex uninstall               # deprecated alias for: graphify setup remove codex

# git hooks - platform-agnostic, rebuild graph on commit and branch switch
graphify hook install
graphify hook uninstall
graphify hook status

graphify claude install / uninstall
graphify codex install / uninstall
graphify opencode install
graphify cursor install / uninstall
graphify gemini install / uninstall
graphify copilot install / uninstall
graphify aider install / uninstall
graphify claw install / uninstall
graphify droid install / uninstall
graphify trae install / uninstall
graphify trae-cn install / uninstall
graphify hermes install / uninstall
graphify kiro install / uninstall
graphify antigravity install / uninstall

# query and navigate the graph directly from the terminal (no AI assistant needed)
graphify query "what connects attention to the optimizer?"
graphify query "show the auth flow" --dfs
graphify query "what is CfgNode?" --budget 500
graphify query "..." --graph path/to/graph.json
graphify path "DigestAuth" "Response"       # shortest path between two nodes
graphify explain "SwinTransformer"          # plain-language explanation of a node

# add content and update the graph from the terminal
graphify add https://arxiv.org/abs/1706.03762          # fetch paper, save to ./raw, update graph
graphify add <video-url>
graphify add https://... --author "Name" --contributor "Name"

# headless extraction for CI/scripts
graphify extract ./docs                        # headless LLM extraction for CI (no IDE needed)
graphify extract ./docs --backend gemini       # explicit backend: gemini, kimi, claude, openai, or ollama
graphify extract ./docs --backend gemini --model gemini-3.1-pro-preview
graphify extract ./docs --backend ollama       # local Ollama (set OLLAMA_BASE_URL / OLLAMA_MODEL)
graphify extract ./docs --no-cluster           # raw extraction only, skip clustering
graphify extract ./docs --dedup-llm            # LLM tiebreaker for ambiguous entity pairs (uses same API key)
graphify extract ./docs --global --as myrepo   # extract and register into the cross-project global graph
GRAPHIFY_MAX_OUTPUT_TOKENS=32768 graphify extract ./docs --backend claude  # raise output cap for dense corpora

# clone any GitHub repo and run the full pipeline on it
graphify clone https://github.com/karpathy/nanoGPT
graphify clone https://github.com/org/repo --branch dev --out ./my-clone

# cross-repo/global graphs
graphify merge-graphs repo1/graphify-out/graph.json repo2/graphify-out/graph.json
graphify merge-graphs g1.json g2.json g3.json --out cross-repo.json
graphify global add graphify-out/graph.json myrepo   # register a project graph into ~/.graphify/global.json
graphify global remove myrepo                         # remove a project from the global graph
graphify global list                                  # show all registered repos + node/edge counts
graphify global path                                  # print path to the global graph file

# incremental update and maintenance
graphify watch ./src
graphify check-update ./src
graphify update ./src
graphify cluster-only ./my-project
graphify cluster-only ./my-project --graph path/to/graph.json
```

Works with any mix of file types:

| Type | Extensions | Extraction |
|------|-----------|------------|
| Code | `.py .ts .js .jsx .tsx .mjs .go .rs .java .c .cpp .rb .cs .kt .scala .php .swift .lua .zig .ps1 .ex .exs .m .mm .jl .vue .svelte` | AST via tree-sitter + call-graph (cross-file for all languages) + Java extends/implements + docstring/comment rationale |
| Docs | `.md .mdx .html .txt .rst .yaml .yml` | Concepts + relationships + design rationale via Claude |
| Office | `.docx .xlsx` | Converted to markdown then extracted via Claude (requires `pip install graphifyy[office]`) |
| Papers | `.pdf` | Citation mining + concept extraction |
| Images | `.png .jpg .webp .gif` | Claude vision - screenshots, diagrams, any language |
| Video / Audio | `.mp4 .mov .mkv .webm .avi .m4v .mp3 .wav .m4a .ogg` | Transcribed locally with faster-whisper, transcript fed into Claude extraction (requires `pip install graphifyy[video]`) |
| YouTube / URLs | any video URL | Audio downloaded via yt-dlp, then same Whisper pipeline (requires `pip install graphifyy[video]`) |

## Video and audio corpus

Drop video or audio files into your corpus folder alongside your code and docs - graphify picks them up automatically:

```bash
pip install 'graphifyy[video]'   # one-time setup
/graphify ./my-corpus            # transcribes any video/audio files it finds
```

Add a YouTube video (or any public video URL) directly:

```bash
graphify add <video-url>
graphify add https://... --author "Name" --contributor "Name"
```

---

## Learn more

- [How it works](docs/how-it-works.md) — the extraction pipeline, community detection, confidence scoring, benchmarks
- [ARCHITECTURE.md](ARCHITECTURE.md) — module breakdown, how to add a language
- [Optional integrations](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite

---

## Built on graphify — Penpax

[**Penpax**](https://graphifylabs.ai) is the always-on layer built on top of graphify — it applies the same graph approach to your entire working life: meetings, browser history, emails, files, and code, updating continuously in the background.

Built for people whose work lives across hundreds of conversations and documents they can never fully reconstruct. No cloud, fully on-device.

**Free trial launching soon.** [Join the waitlist →](https://graphifylabs.ai)

---

<details>
<summary>Contributing</summary>

**Worked examples** are the most useful contribution. Run `/graphify` on a real corpus, save the output to `worked/{slug}/`, write an honest `review.md` covering what the graph got right and wrong, and open a PR.

**Extraction bugs** — open an issue with the input file, the cache entry (`graphify-out/cache/`), and what was missed or wrong.

See [ARCHITECTURE.md](ARCHITECTURE.md) for module responsibilities and how to add a language.

</details>
