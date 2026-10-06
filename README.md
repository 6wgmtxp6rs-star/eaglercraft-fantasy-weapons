# Epic Fantasy Weapons Pack for Eaglercraft

A refined fantasy weapons resource pack for Eaglercraft with stronger silhouette detail, rune-inspired metals, and magical accents. This version focuses on a darker, more premium fantasy look while staying lightweight and easy to customize.

## Included weapon styles

- Rune Sword
- Iron Fang Axe
- Frost Spear
- Shadow Dagger
- Elder Staff
- Elven Bow
- Celestial Blade (bonus variant)

## Pack layout

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
│                       ├── fantasy_elven_bow.svg
│                       └── fantasy_celestial_blade.svg
```

## Installation

1. Open the generated `dist/eaglercraft_fantasy_weapons` directory.
2. Zip it as a resource pack archive.
3. Load the zip in Eaglercraft or extract it into your Eaglercraft resource-pack folder.
4. If your client requires PNG textures, run the export script:

```bash
python -m pip install -r requirements.txt
python scripts/export_pngs.py
```

## Export workflow

The script converts all SVG weapon textures in the pack into PNG files that are easier to load in various Eaglercraft setups.

## Notes

This is a stylized, Eaglercraft-friendly fantasy weapon pack intended for easy visual tweaking. The pack is designed to be lightweight, so it can be adjusted quickly for different fantasy themes like arcane, undead, rune, or dragon-hunter aesthetics.

## License

Creative use only. Feel free to adapt the pack for personal or community Minecraft content.
