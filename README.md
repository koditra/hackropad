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

## BOM (Bill of Materials)

| Item                                   | Quantity  | Notes                  |
| -------------------------------------- | --------- | ---------------------- |
| MODULE-SEEEDUINO-XIAO (Seeeduino XIAO) | 1         | main microcontroller   |
| SW_Push                                | 3         | input switches         |
| Keycaps (1U MX-style or compatible)    | 3         | for switches           |
| USB cable (USB-C)                      | 1         | power + programming    |
| M3 heat-set inserts                    | 4–6       | optional case mounting |
| M3 screws                              | 4–6       | case assembly          |
| 3D printed case parts                  | 1 set     | top + bottom shell     |
| Wire / solder                          | as needed | switch connections     |

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

## Notes

This project is designed to be simple to build and focused on improving coding speed with quick macros.
