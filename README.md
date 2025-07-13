# Document scanner

## Introduction

## Project file structure
```
document-scanner/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/                # Raw scanned images or photos
│   ├── processed/          # Cropped/scanned/thresholded outputs
│   └── examples/           # Example results for testing
├── notebooks/
│   ├── EDA.ipynb           # Experiments: edge detection, contours
│   ├── SignatureExtraction.ipynb
├── src/
│   ├── __init__.py
│   ├── scanner.py          # Core functions: detect edges, crop, transform
│   ├── signature.py        # Extract signature region from doc
│   ├── utils.py            # Helpers: file I/O, plotting
│   ├── pipeline.py         # Runs full end-to-end: load -> scan -> extract
│   └── config.py           # Configs like thresholds
├── scripts/
│   ├── run_pipeline.sh     # Bash script to run whole pipeline
│   └── run_app.sh          # If you make a simple web or CLI app
├── app/
│   ├── app.py              # Optional: Flask or Streamlit app to test online
│   ├── templates/          # For web UI if needed
│   └── static/
├── tests/
│   ├── test_scanner.py
│   ├── test_signature.py
├── outputs/
│   ├── scans/              # Final scanned docs
│   └── signatures/         # Final extracted signatures
├── logs/
│   └── pipeline.log
└── ci/
    └── Jenkinsfile         # To test CI/CD (optional)
```

