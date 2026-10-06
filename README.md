# Fantasy Weapons Pack for Eaglercraft

A stylized fantasy 3D weapons resource pack built for Eaglercraft-style resource pack loading. This repo includes:

- A resource pack layout compatible with Eaglercraft-style packs
- Fantasy sword, axe, spear, dagger, staff, and bow texture sources in SVG
- JSON model overrides for common vanilla weapons
- A quick import guide and optional export workflow

## Included weapon sets

- Rune Sword
- Iron Fang Axe
- Frost Spear
- Shadow Dagger
- Elder Staff
- Elven Bow

## Structure

```text
.
├── README.md
├── requirements.txt
├── scripts/
│   └── export_pngs.py
├── dist/
│   └── eaglercraft_fantasy_weapons/
│       ├── pack.mcmeta
│       └── assets/
│           └── minecraft/
│               ├── lang/
│               │   └── en_us.lang
│               ├── models/
│               │   └── item/
│               │       ├── diamond_sword.json
│               │       ├── iron_sword.json
│               │       ├── golden_sword.json
│               │       ├── diamond_axe.json
│               │       ├── iron_axe.json
│               │       ├── bow.json
│               │       └── ...
│               └── textures/
│                   └── items/
│                       ├── fantasy_iron_sword.svg
│                       ├── fantasy_iron_axe.svg
│                       ├── fantasy_iron_spear.svg
│                       ├── fantasy_iron_dagger.svg
│                       ├── fantasy_wooden_staff.svg
│                       └── fantasy_elven_bow.svg
```

## Installation

1. Open the generated `dist/eaglercraft_fantasy_weapons` folder.
2. Zip it as a resource pack archive.
3. Load the zip in Eaglercraft or extract it into your Eaglercraft resource pack folder.
4. If your client requires PNG textures, run the export script to convert the SVG texture sources to PNG.

## Export PNGs

```bash
pip install -r requirements.txt
python scripts/export_pngs.py
```

This script converts the SVG weapon sources into PNGs inside the generated resource pack.

## Notes

This is a fantasy-style weapon pack intended to feel like a lightweight custom 3D item set. Eaglercraft support varies by browser/client version, so the pack is designed to be easy to tweak if you want to adjust blade silhouettes, gem accents, or color themes.

## License

This project is shared as a creative resource pack template for personal and modded game use.
