# Hackropad

A small 3-key macropad called a hackropad that will help me code faster by typing common Java snippets like if-else statements, for loops, and debug prints with a single key press.

---

## Design Overview

### 3D Render

<img width="717" height="418" alt="Screenshot 2026-06-14 at 12 57 26 PM" src="https://github.com/user-attachments/assets/0501acc7-506e-4f74-b038-f4ab9c39883e" />

### Schematic

<img width="770" height="559" alt="Screenshot 2026-06-14 at 11 34 00 AM" src="https://github.com/user-attachments/assets/e24e3319-3014-4a10-abb0-3c0b2dcadbd1" />

### PCB Layout

<img width="507" height="689" alt="Screenshot 2026-06-14 at 12 59 28 PM" src="https://github.com/user-attachments/assets/e3eebd51-1dad-4521-afbd-5467ae5c5086" />

### Case (3D View)

<img width="1512" height="974" alt="Screenshot 2026-06-14 at 11 32 01 AM" src="https://github.com/user-attachments/assets/88361f31-130f-4ec8-a0bd-e2c839941955" />

---

## Firmware

KMK firmware (CircuitPython)

Main file:

```text id="f1"
Firmware/main.py
```

---

## Files

* `CAD/` → case STEP files
* `PCB/` → KiCad project
* `production/` → gerbers + manufacturing files
* `Firmware/` → firmware source

---

## Pre-Submission Checklist

* PCB is 100mm × 100mm or smaller (2-layer)
* Case fits within 200mm × 200mm × 100mm
* Case is fully 3D printable (no laser-cut or CNC parts)
* Only kit parts used (or self-sourced extras)
* Gerbers exported and zipped
* Case exported as `.STEP`
* Firmware compiles and included in repo
* Heatset insert holes are 4.7mm diameter
* Screw holes have 3.4mm clearance
* 0.2mm tolerance on mating surfaces
* USB-C cutout included in case
* README includes all screenshots + BOM

---

## Notes

This project is designed to be simple to build and focused on improving coding speed with quick macros.
