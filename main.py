import cv2
import numpy as np
from pathlib import Path
from tqdm import tqdm
import os

def clean_image(image_path, save_path, sensitivity=180):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Couldn't open: {image_path}")
            return False

        grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cleaned = cv2.fastNlMeansDenoising(grayscale, None, 10, 7, 21)
        _, binary = cv2.threshold(cleaned, sensitivity, 255, cv2.THRESH_BINARY)
        
        sharpen_filter = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]])
        final_image = cv2.filter2D(binary, -1, sharpen_filter)
        
        cv2.imwrite(save_path, final_image)
        return True
    except Exception as error:
        print(f"Problem with {image_path}: {error}")
        return False

def clean_all_images(source_folder, destination_folder, sensitivity=185):
    os.makedirs(destination_folder, exist_ok=True)
    
    source = Path(source_folder)
    photos = []
    
    for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG']:
        photos.extend(list(source.glob(f'*{extension}')))
    
    if not photos:
        print(f"No photos found in {source_folder}")
        return
    
    print(f"Found {len(photos)} photos. Starting cleanup...")
    
    successful = 0
    failed = 0
    
    for photo in tqdm(photos, desc="Cleaning images"):
        save_location = os.path.join(destination_folder, photo.name)
        if clean_image(str(photo), save_location, sensitivity):
            successful += 1
        else:
            failed += 1
    
    print(f"\nAll done! ✨")
    print(f"  Cleaned successfully: {successful} photos")
    if failed > 0:
        print(f"  Had issues with: {failed} photos")
    print(f"  Saved to: {destination_folder}")

if __name__ == "__main__":
    my_photos = "/content/P_0102"
    cleaned_photos = "/content/drive/MyDrive/cleanimage"
    cleanup_strength = 185
    
    clean_all_images(my_photos, cleaned_photos, sensitivity=cleanup_strength)