import argparse
import os
from pathlib import Path
import sys

# We'll assume the ImageCropper class is defined in image_cropper.py
from image_cropper import ImageCropper

def main():
    """
    Main function to parse command-line arguments and run the image cropper.
    """
    parser = argparse.ArgumentParser(
        description="Automatically crop manhwa panels from screenshots."
    )
    
    # We will now only accept a single input directory
    parser.add_argument(
        "--input-dir", 
        type=str, 
        required=True,
        help="Path to a directory containing screenshot files to process."
    )

    args = parser.parse_args()

    input_dir_path = Path(args.input_dir)
    if not input_dir_path.is_dir():
        print(f"Error: Input directory '{input_dir_path}' not found.")
        sys.exit(1)

    # Define the output directory based on the user's request
    output_dir = Path("data") / "cropped_screenshots"
    output_dir.mkdir(exist_ok=True)

    cropper = ImageCropper()
    
    print(f"Processing images from: {input_dir_path}")
    
    # Get a list of supported image files in the directory
    image_files = [
        f for f in input_dir_path.iterdir()
        if f.is_file() and f.suffix.lower() in ['.jpg', '.jpeg', '.png']
    ]

    if not image_files:
        print("No supported image files found in the directory. Exiting.")
        sys.exit(0)

    # Loop through each image file and process it
    for i, file_path in enumerate(image_files, 1):
        print(f"  [{i}/{len(image_files)}] Processing {file_path.name}...")
        try:
            output_path = output_dir / f"cropped_{file_path.name}"
            cropper.crop_and_save(str(file_path), str(output_path))
            print(f"    -> Saved cropped image to: {output_path}")
        except Exception as e:
            print(f"    -> Error processing {file_path.name}: {e}")

    print("\nProcessing complete.")

if __name__ == "__main__":
    main()
