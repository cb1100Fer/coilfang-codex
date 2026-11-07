# Dwarf Paladin keybind research — WoW Forever

Phase 1 research for the keybind planner and practice tool. It covers every Paladin ability (all ranks), all 51 talents, Dwarf racials, common Holy and Protection macros, and a first-pass layout that works for all three specs.

The machine-readable versions live in [`data/`](data/). The planner app will read those files.

## Sources and how current the data is

| Source | What it gave us | Freshness |
|---|---|---|
| [wowforevertalents.com](https://wowforevertalents.com/paladin/): [talents](https://wowforevertalents.com/paladin/), [abilities](https://wowforevertalents.com/abilities/paladin/), [racials](https://wowforevertalents.com/racials/) | Spell ranks, costs, cooldowns, learn levels, talent positions and text, Dwarf racials | Read from the Forever client, build 1.60.1.70862, plus the server hotfixes of **7 Nov 2026** |
| [Blizzard — Forever Class Deep Dive: Paladin](https://news.blizzard.com/en-us/article/24302099/world-of-warcraft-forever-class-deep-dives-paladin) | Design intent and mechanics (Seal of Fury taunt, Judgement no longer consumes the Seal, etc.) | Written during the beta. Some details were superseded by the 2 Nov changes. |
| [wowforevertools.com](https://wowforevertools.com/abilities/paladin) | Cross-check of trainer levels (Blessing of Kings lvl 20, Salvation/Revoke) | Older beta data |
| Guide search results (Mobalytics, Method, Icy Veins, Warcraft Tavern, Conquest Capped) | Cross-checks and conflicts | Mixed dates |

Where sources disagree, these files follow the **client data**.

## Forever changes that matter for keybinds

- **Holy Strike** (new, lvl 6, 8 ranks, 10s CD) is the shared melee button for all specs. Shieldsworn cuts its CD to 6s.
- **Judgement no longer consumes your Seal.** It becomes a press-on-cooldown button, and you rarely need to recast a Seal.
- **Seal of Fury** (new, lvl 10) is the tank Seal. Its **Judgement is the taunt**, with 10 yd range. The talent **Swift Judgement** is a second Judgement on its own 1 min CD, used as a backup taunt.
- **Consecration** is baseline at lvl 20, full damage only to the first 4 targets. **Hammer of the Righteous** (new, lvl 40, 4 targets, 6s CD) is in the client data but not in Blizzard's post, so verify it in-game.
- **Voice of Truth** is now a lvl 20 trainer spell: 6s immunity to silence and interrupt, 3 min CD. It was an 11-point Holy talent in the beta.
- **Holy Shock** sits at 20 points in Holy with a 10s CD. **Light's Vigil** is the new 31-point Holy capstone, a cast on an ally that makes your next Holy Shock on them free of cooldown and heals their whole party.
- **Retribution's capstone is Unsealed Wrath** (passive seal storage). Twist of Light and Instrument of Law from the beta post were removed on 2 Nov.
- **Protection** gains **Templar's Bulwark** (5 min absorb, shares Forbearance) and **Holy Shield** at 20 points.
- **Lay on Hands** has a 20 min CD. Blessings last 1 hour.
- **Removed:** Blessing of Salvation, Blessing of Sanctuary, Blessing of Light, Sense Undead, and the class mounts (Warhorse/Charger) as trainer spells.

## Unknowns to check in-game

1. **Salvation / Mass Salvation / Revoke.** Blizzard announced them, but the current client lists no trainer for any of them. Treat them as absent.
2. **Blessing of Kings (single target).** Blizzard and guides say it is baseline at lvl 20, but it is missing from the client trainer dump (only Greater Blessing of Kings at 60 appears).
3. **Hammer of the Righteous** is in the client data, but no Blizzard note mentions it.
4. **Divine Favor and the GCD.** Whether the "Divine Favor + heal" one-press macro works depends on this.
5. **Dwarf racials.** Some guides still list "Mace Specialization". The client lists **Artisan's Precision** (+1% hit), **Big Game Hunter**, **Stoneform** and **Find Treasure**.
6. **Naga V2 Pro wheel tilt** is unconfirmed, so it is modelled as optional.

## All Paladin abilities

Usage key: **core** = rotation · freq = most pulls · sit = situational · CD = planned cooldown · flex = only if that talent is taken · panic = emergency · util = helping others · buff = set at pull · ooc = out of combat · low = replaced later on the same key · — = not used.

Full rank-by-rank text, costs and cooldowns are in `data/paladin-spells.json`.

| Ability | Category | Learn lvl | Ranks | Source | Forever | Holy | Prot | Ret |
|---|---|---|---|---|---|---|---|---|
| Holy Light | heal | 1 | 9 | trainer | ◆ changed | **core** | sit | sit |
| Flash of Light | heal | 20 | 6 | trainer | ◆ changed | **core** | sit | sit |
| Holy Shock | heal | 30 | 4 | talent (Holy, 20 pts) | ◆ changed | **core** | — | flex |
| Light's Vigil | heal | 40 | 3 | talent (Holy, 30 pts) | ★ new | freq | — | — |
| Purify | dispel | 8 | 1 | trainer |  | low | low | low |
| Cleanse | dispel | 42 | 1 | trainer |  | freq | sit | sit |
| Holy Strike | strike | 6 | 8 | trainer | ★ new | sit | **core** | **core** |
| Hammer of the Righteous | strike | 40 | 1 | trainer | ★ new | — | **core** | freq |
| Judgement | judgement | 4 | 1 | trainer | ◆ changed | sit | **core** | **core** |
| Swift Judgement | judgement | 25 | 1 | talent (Protection, 15 pts) | ★ new | — | CD | — |
| Seal of Righteousness | seal | 1 | 8 | trainer | ◆ changed | sit | sit | freq |
| Seal of the Crusader | seal | 6 | 6 | trainer | ◆ changed | sit | sit | freq |
| Seal of Fury | seal | 10 | 7 | trainer | ★ new | — | **core** | — |
| Seal of Command | seal | 20 | 5 | talent (Retribution, 10 pts) | ◆ changed | — | — | **core** |
| Seal of Justice | seal | 22 | 1 | trainer |  | sit | sit | sit |
| Seal of Light | seal | 30 | 4 | trainer | ◆ changed | sit | sit | sit |
| Seal of Wisdom | seal | 38 | 3 | trainer | ◆ changed | freq | freq | sit |
| Consecration | aoe | 20 | 5 | trainer | ◆ changed | sit | **core** | freq |
| Holy Wrath | aoe | 50 | 2 | trainer | ◆ changed | sit | sit | sit |
| Exorcism | damage | 20 | 6 | trainer | ◆ changed | sit | sit | freq |
| Hammer of Wrath | damage | 44 | 3 | trainer | ◆ changed | sit | sit | freq |
| Hammer of Justice | control | 8 | 4 | trainer |  | util | util | util |
| Turn Undead | control | 24 | 3 | trainer |  | sit | sit | sit |
| Repentance | control | 30 | 1 | talent (Retribution, 20 pts) |  | — | — | flex |
| Divine Protection | defensive | 6 | 2 | trainer | ◆ changed | panic | panic | panic |
| Voice of Truth | defensive | 20 | 1 | trainer | ★ new | CD | sit | sit |
| Templar's Bulwark | defensive | 20 | 1 | talent (Protection, 10 pts) | ★ new | — | CD | — |
| Holy Shield | defensive | 30 | 4 | talent (Protection, 20 pts) | ◆ changed | — | **core** | — |
| Divine Shield | defensive | 34 | 2 | trainer | ◆ changed | panic | panic | panic |
| Blessing of Protection | emergency | 10 | 3 | trainer | ◆ changed | util | util | util |
| Lay on Hands | emergency | 10 | 3 | trainer | ◆ changed | panic | panic | panic |
| Divine Intervention | emergency | 30 | 1 | trainer |  | util | util | util |
| Blessing of Freedom | utility | 18 | 1 | trainer |  | util | util | util |
| Blessing of Sacrifice | utility | 46 | 2 | trainer |  | util | sit | util |
| Righteous Fury | buff | 10 | 1 | trainer | ◆ changed | — | buff | sit |
| Oath of Light | buff | 25 | 1 | talent (Holy, 15 pts) | ★ new | buff | — | — |
| Devotion Aura | aura | 1 | 7 | trainer |  | buff | buff | buff |
| Retribution Aura | aura | 16 | 5 | trainer |  | buff | buff | buff |
| Concentration Aura | aura | 22 | 1 | trainer |  | buff | buff | buff |
| Shadow Resistance Aura | aura | 28 | 3 | trainer | ◆ changed | buff | buff | buff |
| Frost Resistance Aura | aura | 32 | 3 | trainer | ◆ changed | buff | buff | buff |
| Fire Resistance Aura | aura | 36 | 3 | trainer | ◆ changed | buff | buff | buff |
| Blessing of Might | blessing | 4 | 7 | trainer | ◆ changed | ooc | ooc | ooc |
| Blessing of Wisdom | blessing | 14 | 6 | trainer | ◆ changed | ooc | ooc | ooc |
| Blessing of Kings | blessing | 20 | 1 | trainer | ◆ changed | ooc | ooc | ooc |
| Greater Blessing of Might | blessing | 52 | 2 | trainer | ◆ changed | ooc | ooc | ooc |
| Greater Blessing of Wisdom | blessing | 54 | 2 | trainer | ◆ changed | ooc | ooc | ooc |
| Greater Blessing of Kings | blessing | 60 | 1 | trainer | ◆ changed | ooc | ooc | ooc |
| Divine Favor | cooldown | 20 | 1 | talent (Holy, 10 pts) |  | CD | — | — |
| Redemption | ooc | 12 | 5 | trainer |  | ooc | ooc | ooc |

## Talents (51)

Talents start at lvl 10. Gold medals sit at 11, 16, 21 and 31 points. Dual Spec unlocks at lvl 40. Only the **ACTIVE** talents need a key.


**Holy**

- Row 1: Spiritual Focus (5 ranks)
- Row 1: Divine Strength (5 ranks)
- Row 2: Healing Light (3 ranks)
- Row 2: Reverence (2 ranks) ★
- Row 2: Improved Seals (5 ranks)
- Row 2: Purifying Power (2 ranks) ★
- Row 3: Divine Favor (1 rank) — **ACTIVE**: 4% of base mana · Instant · 2 min cooldown
- Row 3: Illumination (5 ranks) — requires Reverence
- Row 3: Holy Conduit (2 ranks) ★
- Row 4: Divine Precision (2 ranks) ★
- Row 4: Infusion of Light (2 ranks) ★
- Row 4: Oath of Light (1 rank) — **ACTIVE**: 8% of base mana · 40 yd range · Instant ★
- Row 5: Consecrated Ground (2 ranks) ★
- Row 5: Holy Shock (1 rank) — **ACTIVE**: 160 Mana · 20 yd range · Instant · 10 sec cooldown
- Row 5: Boundless Light (2 ranks) ★
- Row 6: Holy Power (5 ranks)
- Row 7: Light's Vigil (1 rank) — **ACTIVE**: 730 Mana · 40 yd range · 1.5 sec cast · 6 sec cooldown ★ — requires Holy Shock

**Protection**

- Row 1: Divine Intellect (5 ranks)
- Row 1: Redoubt (5 ranks)
- Row 2: Precision (3 ranks)
- Row 2: Guardian's Favor (2 ranks)
- Row 2: Sacred Duty (2 ranks) ★
- Row 3: Templar's Bulwark (1 rank) — **ACTIVE**: 110 Mana · Instant · 5 min cooldown ★
- Row 3: Improved Hammer of Justice (3 ranks)
- Row 3: Shield Specialization (2 ranks)
- Row 3: Toughness (5 ranks)
- Row 4: Swift Judgement (1 rank) — **ACTIVE**: 10 yd range · Instant · 1 min cooldown ★
- Row 4: Improved Righteous Fury (3 ranks)
- Row 4: Anticipation (5 ranks)
- Row 5: Stoicism (2 ranks) ★
- Row 5: Holy Shield (1 rank) — **ACTIVE**: 100 Mana · Instant · 10 sec cooldown — requires Templar's Bulwark
- Row 5: Reckoning (5 ranks)
- Row 6: Iron Creed (3 ranks) ★
- Row 7: Shieldsworn (1 rank) ★ — requires Holy Shield

**Retribution**

- Row 1: Deflection (5 ranks)
- Row 1: Benediction (5 ranks)
- Row 2: Improved Judgement (2 ranks)
- Row 2: Conviction (3 ranks)
- Row 2: Sanctified Judgement (3 ranks) ★
- Row 3: Vindication (3 ranks)
- Row 3: Unyielding Faith (2 ranks)
- Row 3: Seal of Command (1 rank) — **ACTIVE**: 65 Mana · Instant
- Row 3: Pursuit of Justice (2 ranks)
- Row 4: Eye for an Eye (2 ranks)
- Row 4: Sacred Arbiter (1 rank) ★
- Row 4: Two-Handed Weapon Specialization (3 ranks)
- Row 5: Turn Evil (2 ranks) ★
- Row 5: Repentance (1 rank) — **ACTIVE**: 60 Mana · 20 yd range · Instant · 1 min cooldown
- Row 5: Vengeance (3 ranks) — requires Sanctified Judgement
- Row 6: Champion of the Light (5 ranks) ★
- Row 7: Unsealed Wrath (1 rank) ★ — requires Repentance

**Talent actives per spec** (the only buttons that change between specs):

| Spec | Talent buttons |
|---|---|
| Holy | Holy Shock, Light's Vigil, Divine Favor, Oath of Light |
| Protection | Holy Shield, Swift Judgement, Templar's Bulwark |
| Retribution | Seal of Command, Repentance (Holy Shock if built as Shockadin) |

## Dwarf racials

| Racial | Type | Bind? |
|---|---|---|
| Stoneform: removes and grants immunity to bleed, poison and disease, −10% physical damage for 8s, 3 min CD | Active | **Yes.** Defensive cluster, all specs. |
| Find Treasure: treasure tracking | Toggle | Out-of-combat key only |
| Artisan's Precision: +1% hit with spells and attacks | Passive | — |
| Big Game Hunter: +5% damage vs Beasts | Passive | — |

## Macros

The full text of 28 macros is in `data/macros.json`. Highlights:

**Healer (Holy):** mouseover Flash of Light and Holy Light (Shift = downrank) · smart Holy Shock (heals a friend or hits an enemy under the cursor) · mouseover Light's Vigil · Oath of Light on the tank via `@targettarget` · Divine Favor + Holy Light · mouseover Cleanse, BoP, Freedom, Sacrifice, Lay on Hands, Redemption · `/stopcasting` snipe heal · Judgement with Shift to reseal Wisdom.

**Tank (Protection):** Holy Strike + `/startattack` · mouseover Judgement taunt (Seal of Fury) · mouseover Swift Judgement backup taunt · Hammer of the Righteous + `/startattack` · defensive stack (Bulwark / Divine Shield on one key, since they share Forbearance) · mouseover Hammer of Justice (paladins have no interrupt) · cancel Salvation (only if Salvation exists live).

**Shared / Ret:** Ret seal swap for Unsealed Wrath (Command ↔ Righteousness on one key) · healthstone with Shift for potion · trinkets · smart Blessing (Shift = Greater).

## Spec-agnostic layout (draft v0)

The rule: **every baseline spell has one key in every spec.** Only four **FLEX** slots change with talents.

| Flex slot | Key | Holy | Protection | Retribution |
|---|---|---|---|---|
| FLEX-A: signature talent button | Q | Holy Shock | Holy Shield | Seal of Command |
| FLEX-B: second talent button | E | Light's Vigil | Swift Judgement | Repentance |
| FLEX-C: talent cooldown | 5 | Divine Favor | Templar's Bulwark | *(free, e.g. Holy Shock for Shockadin)* |
| FLEX-D: pre-pull talent buff | T | Oath of Light | — | — |

**Keyboard** (Shift variant after the slash):
`1` Holy Strike / Hammer of Wrath · `2` Judgement (taunt) / Exorcism · `3` Consecration / Holy Wrath · `4` Hammer of the Righteous / Turn Undead · `Q` FLEX-A / Seal of Righteousness · `E` FLEX-B / Seal of the Crusader · `R` Seal of Fury / Seal of Wisdom (Ctrl: Seal of Light) · `F` Hammer of Justice / Seal of Justice · `T` FLEX-D / Righteous Fury · `G` Stoneform / Voice of Truth · `Z` Divine Protection / Divine Shield · `X` Lay on Hands · `C` Healthstone / Mana potion · `V` Trinkets · `Ctrl-1…6` auras · `Alt-1…3, Alt-Q/E/R` blessings and greater blessings.

**Naga V2 Pro, 6-button plate:**
S1 Flash of Light · S2 Holy Light (Shift = downrank) · S3 Blessing of Freedom · S4 Cleanse · S5 Blessing of Protection (Shift = Sacrifice) · S6 Stopcast-snipe heal · wheel click Assist · wheel up Smart Blessing · wheel down Redemption · top buttons Divine Intervention and Hearthstone.

Why it is laid out this way:
- **Heals live on the mouse.** You heal by hovering over raid frames, so the mouse hand also triggers the cast. All specs get emergency off-heals in the same spot.
- **Melee lives on 1–4 / Q / E / R near WASD.** Protection and Retribution share the same rotation keys. Holy's hot keys (Q/E/5) are the FLEX slots, so the same finger presses "my talent button" in every spec.
- **Shift is always a related variant** of the base key (damage ↔ execute, seal ↔ seal), which keeps the mental model small.
- **Defensives that share Forbearance sit on one key with modifiers**, so you can't waste one by accident.

The exact binding list is in `data/layout-draft.json`. It is a starting point to refine in the planner and simulator.

## Data files

| File | Contents |
|---|---|
| `data/paladin-spells.json` | 50 bindable class abilities: every rank (text, cost, cast, CD, learn level), category, and per-spec usage tier |
| `data/paladin-talents.json` | All 51 talents with tree, row/column, ranks, points required, active/passive, prerequisites; plus removed spells and unknowns |
| `data/dwarf-racials.json` | Dwarf racials, Forever vs Classic text |
| `data/general-actions.json` | Non-class binds (targeting, mount, consumables, trinkets…) |
| `data/macros.json` | 28 macros with bodies, roles, the spell each replaces, and verification flags |
| `data/hardware.json` | Naga V2 Pro (6-button plate) buttons and keyboard reach tiers |
| `data/layout-draft.json` | Draft v0 binding set and flex-slot definitions |

## Next phases

1. **Planner app:** a keyboard and Naga visual with drag-and-drop abilities and macros, spec toggle (Holy/Prot/Ret) showing flex slots, coverage warnings for unbound core spells, and export.
2. **Practice simulator:** prompts like "Tank: taunt the loose add", "Heal: tank at 40%" or a rotation metronome, timed against your binds, to measure reaction time and misses per key.

## Community layouts (researched 7 Nov 2026)

WoW Forever launched on 4 Nov 2026, and no complete paladin bind list had been published by then. The forums, guide sites and videos instead describe a handful of recurring **approaches**. Each one is a preset in `data/presets.json`, adapted to Forever spells and this planner's flex keys. You can load them from the planner's **Community presets** dropdown.

| Preset | Approach | Sources |
|---|---|---|
| Naga thumb grid | Rotation and talent buttons on the six side buttons, with Shift + side button as a heal and protection layer. Synapse sends F13–F18 or Ctrl+Numpad so modifiers still work. | [MMO-Champion: Naga 12-button binds](https://www.mmo-champion.com/threads/1497947-What-do-you-keybind-to-a-Naga-12-button-mouse/page2) · [MMO-Champion: Naga Shift binds](https://www.mmo-champion.com/threads/858293-Help-Razor-Naga-Shift-bind-ability) · [WoW Insider: mouseovers + Naga](https://www.engadget.com/2010-06-10-the-magical-alchemy-of-mouseovers-plus-a-razer-naga.html) |
| Wheel & click healer | Click-casting (Clique) style: mouseover heals on the wheel and wheel click, Shift for BoP, Lay on Hands and Freedom, melee kept on 1–4 | [Blizzard: Holy Paladin Key and Click Configuration Guide](https://us.forums.blizzard.com/en/wow/t/holy-paladin-key-and-click-configuration-guide/842317) · [Blizzard EU: Holy Paladin Keybinds](https://eu.forums.blizzard.com/en/wow/t/holy-paladin-keybinds-what/261991) · [Zockify: Forever paladin macros](https://www.zockify.com/forever/paladin/macros/) |
| Keyboard-first WASD | Everything on 1–6 and the letters around WASD, with Shift as the second layer and interrupt-type buttons within easy reach. Works with any mouse. | [WoW Insider: key-binding your ret paladin](https://www.engadget.com/2013-03-06-how-to-key-bind-your-retribution-paladin.html) · [Blizzard EU: holy/ret keybinds](https://eu.forums.blizzard.com/en/wow/t/keybinds-problem-holy-ret/112893) · [YouTube: Best WoW Keybinds for Tanks, Healers & DPS](https://www.youtube.com/watch?v=1aIrYKBBZ5w) · [WarcraftMaps: Forever keybinds](https://warcraftmaps.com/guides/keybinds) |
| Compact modifier macros | Forever macro-site one-button macros: Judgement + Holy Strike together, Consecration (Shift = Righteous Fury), Flash of Light (Shift = Holy Light), BoP (Alt = Divine Protection) | [Classic WoW Forever: paladin macros](https://classicwowforever.com/macros/paladin/) · [RankedBoost](https://rankedboost.com/world-of-warcraft/forever/macros/paladin/) · [WOWF.IO](https://wowf.io/en/macros/paladin) · [Zockify](https://www.zockify.com/forever/paladin/macros/) |

Notes:
- Most Naga and click-healing threads are years old, and their spell names predate Forever. The approaches carry over, but the exact spells don't.
- The Judgement + Holy Strike macro relies on Judgement being off the global cooldown, as it is in Classic-era clients. Check this in Forever before relying on it.
- Reddit and YouTube pages couldn't be read directly from this environment. Their content was gathered through web search.
