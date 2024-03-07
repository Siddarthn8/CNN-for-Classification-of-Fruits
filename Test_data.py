import csv
import os

output_csv = 'Test.csv'
image_names = []

##apple_6
image_dir = r'\path\to\folder\Test\apple_6'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_6/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,0])
    else:
        continue

## apple_breaburn_1
image_dir = r'\path\to\folder\Test\apple_braeburn_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_braeburn_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,1])
    else:
        continue

## apple_crimson_snow_1
image_dir = r'\path\to\folder\Test\apple_crimson_snow_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_crimson_snow_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,2])
    else:
        continue

## apple_golden_1
image_dir = r'\path\to\folder\Test\apple_golden_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_golden_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,3])
    else:
        continue

## apple_golden_2
image_dir = r'\path\to\folder\Test\apple_golden_2'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_golden_2/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,4])
    else:
        continue

## apple_golden_3
image_dir = r'\path\to\folder\Test\apple_golden_3'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_golden_3/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,5])
    else:
        continue

## apple_granny_smith_1
image_dir = r'\path\to\folder\Test\apple_granny_smith_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_granny_smith_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,6])
    else:
        continue

## apple_hit_1
image_dir = r'\path\to\folder\Test\apple_hit_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_hit_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,7])
    else:
        continue

## apple_pink_lady_1
image_dir = r'\path\to\folder\Test\apple_pink_lady_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_pink_lady_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,8])
    else:
        continue

## apple_red_1
image_dir = r'\path\to\folder\Test\apple_red_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_red_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,9])
    else:
        continue

## apple_red_2
image_dir = r'\path\to\folder\Test\apple_red_2'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_red_2/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,10])
    else:
        continue

## apple_red_3
image_dir = r'\path\to\folder\Test\apple_red_3'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_red_3/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,11])
    else:
        continue

## apple_red_delicios_1
image_dir = r'\path\to\folder\Test\apple_red_delicios_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_red_delicios_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,12])
    else:
        continue

## apple_red_yellow_1
image_dir = r'\path\to\folder\Test\apple_red_yellow_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_red_yellow_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,13])
    else:
        continue

## apple_rotten_1
image_dir = r'\path\to\folder\Test\apple_rotten_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/apple_rotten_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,14])
    else:
        continue

## cabbage_white_1
image_dir = r'\path\to\folder\Test\cabbage_white_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/cabbage_white_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,15])
    else:
        continue

## carrot_1
image_dir = r'\path\to\folder\Test\carrot_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/carrot_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,16])
    else:
        continue

## cucumber_1
image_dir = r'\path\to\folder\Test\cucumber_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/cucumber_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,17])
    else:
        continue

## cucumber_3
image_dir = r'\path\to\folder\Test\cucumber_3'
prefix = '/path/to/folder/fruits-360-original-size/Test/cucumber_3/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,18])
    else:
        continue

## eggplant_violet_1
image_dir = r'\path\to\folder\Test\eggplant_violet_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/eggplant_violet_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,19])
    else:
        continue

## pear_1
image_dir = r'\path\to\folder\Test\pear_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/pear_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,20])
    else:
        continue

## pear_3
image_dir = r'\path\to\folder\Test\pear_3'
prefix = '/path/to/folder/fruits-360-original-size/Test/pear_3/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,21])
    else:
        continue

## zucchini_1
image_dir = r'\path\to\folder\Test\zucchini_dark_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/zucchini_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,22])
    else:
        continue

## zucchini_dark_1
image_dir = r'\path\to\folder\Test\zucchini_dark_1'
prefix = '/path/to/folder/fruits-360-original-size/Test/zucchini_dark_1/'

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
        image_names.append([prefix+filename,23])
    else:
        continue

with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    # writer.writerow(['ImagePath', 'Label'])  
    for row in image_names:

        writer.writerow(row)