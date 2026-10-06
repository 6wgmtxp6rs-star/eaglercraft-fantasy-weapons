# Fantasy Weapon Pack for Eaglercraft

A final fantasy-inspired weapon resource pack that matches each weapon to the best tool slot and role in Eaglercraft style gameplay.

## Final weapon list and tool fit

- Rune Sword → Sword
- Iron Fang Axe → Axe
- Frost Spear → Spear / Polearm
- Shadow Dagger → Dagger / Knife
- Elder Staff → Staff / Magic Focus
- Elven Bow → Bow
- Celestial Blade → Legendary Sword / Magic Blade
- Reaper Scythe → Scythe
- Thunder Mace → Hammer / Mace
- Orbit Chakram → Chakram / Throwing Weapon

## Grouping

### Melee core
- Rune Sword
- Iron Fang Axe
- Frost Spear
- Shadow Dagger
- Reaper Scythe
- Thunder Mace

### Ranged
- Elven Bow
- Orbit Chakram

### Magic/support
- Elder Staff
- Celestial Blade

## Files included

- `weapon_tool_mapping.json`
- `scripts/export_pngs.py`
- `dist/eaglercraft_fantasy_weapons/assets/minecraft/models/item/*.json`
- `dist/eaglercraft_fantasy_weapons/assets/minecraft/textures/items/*.svg`

## Setup

```bash
python -m pip install -r requirements.txt
python scripts/export_pngs.py
```

Then zip the `dist/eaglercraft_fantasy_weapons` folder as a resource pack and load it in Eaglercraft.
