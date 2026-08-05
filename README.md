# Metadata EXIF Analyzer

A Python tool for extracting and analyzing EXIF metadata from digital images.

This repository contains both the beginner-friendly version used in my educational Instagram videos and a more structured implementation for developers.

---

## Features

- 📷 Extract camera manufacturer
- 📱 Detect device model
- 📅 Read capture date and time
- 📍 Extract GPS coordinates (if available)
- 🗺️ Generate Google Maps location link
- 🎓 Beginner-friendly educational example
- 🧑‍💻 Structured implementation for developers

---

## Project Structure

```text
metadata-exif-analyzer/
├── examples/
│   └── exif_analyzer.py     # Educational version used in Instagram tutorials
│
├── src/
│   └── exif_analyzer.py     # Structured implementation
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ahmetgulerpy/metadata-exif-analyzer.git
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

---

## Usage

Educational version:

```bash
python examples/exif_analyzer.py
```

Structured version:

```bash
python src/exif_analyzer.py image.jpg
```

---

## Repository Purpose

This repository was created to help beginners understand how EXIF metadata can be extracted and analyzed using Python.

The `examples` directory contains the simplified version demonstrated in my educational content, while the `src` directory provides a cleaner and more structured implementation of the same concept.

---

## Disclaimer

This project is intended for educational, research and authorized security awareness purposes only.

Always ensure you have permission before analyzing files that do not belong to you.

---

## License

This project is licensed under the MIT License.
