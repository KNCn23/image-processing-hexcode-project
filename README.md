# Image Processing — Hex Code Analyzer

A Python tool that processes image files and extracts dominant color data as hex codes using pixel-level analysis. Useful for design workflows that need to pull a palette from a reference image.

## What It Does

- Loads an image and samples pixel colors across the frame
- Groups similar colors and identifies the most frequent values
- Outputs hex codes for the dominant colors

## Run

```bash
python main.py
```

Requires Python 3.8+.

## Tech

| Library | Role |
|---------|------|
| OpenCV | Image loading and pixel access |
| NumPy | Array operations and color grouping |

## License

MIT
