Image Watermark Removal Tool 🖼️
A simple Python script to remove watermarks from images in bulk. Perfect for cleaning up scanned documents or photos with unwanted watermarks.
What Does It Do?
This tool processes images to remove watermarks and text overlays by:

Converting images to grayscale
Removing noise
Applying smart thresholding
Sharpening the final result

Requirements
Before running the script, make sure you have these installed:
bashpip install opencv-python numpy tqdm
How to Use
Basic Setup

Prepare your folders:

Put all your images in one folder (e.g., /content/P_0102)
Create or choose a destination folder (e.g., /content/drive/MyDrive/cleanimage)


Update the script:

python   my_photos = "/path/to/your/images"
   cleaned_photos = "/path/to/save/cleaned/images"
   cleanup_strength = 185

Run it:

bash   python watermark_remover.py
Adjusting the Sensitivity
The cleanup_strength parameter controls how aggressive the cleaning is:

160-170: Gentle - keeps more detail but might leave watermark traces
180-185: Balanced - good for most cases (default: 185)
190-200: Aggressive - removes more but might lose some text clarity

Tip: Start with 185. If watermarks remain, increase it. If text looks too thin, decrease it.
Supported File Types

PNG (.png)
JPEG (.jpg, .jpeg)
Works with both uppercase and lowercase extensions

Example Output
Found 1600 photos. Starting cleanup...
Processing images: 100%|██████████| 1600/1600 [05:23<00:00, 4.95it/s]

All done! ✨
  Cleaned successfully: 1598 photos
  Had issues with: 2 photos
  Saved to: /content/drive/MyDrive/cleanimage
Troubleshooting
"No photos found in folder"

Check if the folder path is correct
Make sure your images have supported extensions

Results not good enough?

Try adjusting the cleanup_strength value
Lower values preserve more detail
Higher values remove more aggressively

Some images failed

Check if those files are corrupted
Make sure you have read permissions
Verify the image format is supported

How It Works (Technical)

Grayscale Conversion: Simplifies the image to black and white
Denoising: Uses Non-local Means Denoising to clean up artifacts
Thresholding: Separates text from background based on pixel intensity
Sharpening: Enhances text edges for clearer output
