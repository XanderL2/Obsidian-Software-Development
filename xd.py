import os;

imagesPath = './6. Images/';
os.chdir(imagesPath);

images = os.listdir();

for index, image in enumerate(images):
    
    print(f"Imagen numero: {index + 1} / {len(images)}")
    parsedImage = image.replace(" ", "\\ ");
    command = f'kitty +icat {parsedImage}';
    os.system(command);
    delete = input("Eliminar y/n: ");
    if(delete == "y"): os.remove(image);
