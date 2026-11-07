#!/usr/bin/env python3
"""Build keybinds/planner/index.html from the template and the data/ JSON files.

Usage: python3 keybinds/tools/build_planner.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TEMPLATE = ROOT / "planner" / "planner.template.html"
OUT = ROOT / "planner" / "index.html"


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def compact_spells():
    out = []
    for s in load("paladin-spells.json")["spells"]:
        top = s["ranks"][-1] if s["ranks"] else {"text": "", "cost": ""}
        out.append({
            "id": s["id"], "name": s["name"], "kind": "spell",
            "category": s["category"], "usage": s["usage"],
            "level": s["learnLevel"], "ranks": len(s["ranks"]),
            "source": s["source"],
            "talent": s["talent"], "status": s["status"],
            "text": top["text"], "cost": top["cost"], "notes": s.get("notes", ""),
            "confidence": s.get("confidence", "high"),
            "rk": [[r["level"], r["text"], r["cost"]] for r in s["ranks"]],
        })
    return out


def main():
    racials = [r for r in load("dwarf-racials.json")["racials"] if r["type"] != "passive"]
    data = {
        "spells": compact_spells(),
        "racials": [{
            "id": r["id"], "name": r["name"], "kind": "racial", "category": r["category"],
            "usage": r["usage"], "level": 1, "text": r["text"],
            "cost": r.get("cooldown", ""), "notes": r.get("notes", ""),
        } for r in racials],
        "general": [{
            "id": a["id"], "name": a["name"], "kind": "general", "category": a["category"],
            "usage": a["usage"], "level": 1, "text": "", "cost": "", "notes": a.get("notes", ""),
        } for a in load("general-actions.json")["actions"]],
        "macros": load("macros.json")["macros"],
        "layout": load("layout-draft.json"),
        "presets": load("presets.json")["presets"],
        "hardware": load("hardware.json"),
    }
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/null", blob)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({len(html)//1024} KB)")


if __name__ == "__main__":
    main()
