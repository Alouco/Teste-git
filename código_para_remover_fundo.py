from rembg import remove
from PIL import Image

input_imagem = 'transferir.jpeg'
remove_fundo = 'rato.png'

imagem = Image.open(input_imagem)
output_imagem = remove(imagem)

output_imagem.save(remove_fundo)