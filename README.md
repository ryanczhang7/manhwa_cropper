# Manhwa Panel Cropper

An automated tool to crop manhwa, manga, and comic panels from full-screen screenshots. This project uses computer vision techniques to detect and isolate the main vertical panel content, removing browser UI elements like the address bar and taskbar.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/manhwa-cropper.git](https://github.com/your-username/manhwa-cropper.git)
    cd manhwa-cropper
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  Place your screenshots in the `data/screenshots/` directory.

2.  Run the main script from the root of the project, specifying the input directory.

    **Example:**
    ```bash
    python src/main.py --input-dir data/screenshots/
    ```

3.  The cropped images will be saved to the `data/cropped_screenshots/` directory.
