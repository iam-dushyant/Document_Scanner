# src/pipeline.py

import os
from pathlib import Path

from scanner import scan_document
from utils import load_image, save_image

def main():
    print("Document & Signature Scanner Pipeline")

    # Define paths
    raw_image_path = Path("../data/raw/sample_doc.jpg")
    scanned_output_path = Path("../data/processed/scanned_doc.jpg")

    # Load raw image
    print(f"Loading raw image: {raw_image_path}")
    image = load_image(raw_image_path)

    # Scan document
    print("Running document scan...")
    scanned_doc = scan_document(image)
    save_image(scanned_output_path, scanned_doc)
    print(f"Scanned doc saved: {scanned_output_path}")

    print("Pipeline completed!")

if __name__ == "__main__":
    main()