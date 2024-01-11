from PIL import Image
import os


def resize_images(input_folder, output_folder, max_width):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        # Create the full file path
        input_path = os.path.join(input_folder, file)

        # Open the image
        with Image.open(input_path) as img:
            # Calculate the proportional height based on the max width
            width_percent = max_width / float(img.size[0])
            height_size = int((float(img.size[1]) * float(width_percent)))

            # Resize the image
            resized_img = img.resize((max_width, height_size), Image.ANTIALIAS)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, file)
            resized_img.save(output_path)


# Example usage
input_folder = "./data/train/"
output_folder = "./resizing"
max_width = 800  # Set your desired maximum width

resize_images(input_folder, output_folder, max_width)
