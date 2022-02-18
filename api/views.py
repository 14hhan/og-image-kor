from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.templatetags.static import static
import tempfile

# Create your views here.
class OpenGraphImageView(APIView):
    def get(self, request):
        title = request.query_params['title']
        author = request.query_params['author']
        static_root_path = str(settings.BASE_DIR)

        if request.GET.get('image_uri', None) != None:
            image_uri = request.query_params['image_uri']
            img_response = requests.get(image_uri)
            background_image = Image.open(BytesIO(img_response.content))
        else:
            image_path = static_root_path + static('ocean.jpg')
            background_image = Image.open(image_path)

        draw = ImageDraw.Draw(background_image)
      
        title_font = ImageFont.truetype(static_root_path + static('Pretendard-Black.ttf'), 120)
        draw.multiline_text((40, 30), title, fill='white', font=title_font, spacing=10)
        draw.text((45, 380), '—', fill='white', font=title_font)

        site_name_font = ImageFont.truetype(static_root_path + static('Pretendard-Bold.ttf'), 60)
        w, h = draw.textsize(author, font=site_name_font)
        draw.text((1160-w, 595-h), author, fill='white', font=site_name_font, align='right')

        image = tempfile.NamedTemporaryFile()
        background_image.save(image, background_image.format, quality=100)
        image.seek(0)

        response = HttpResponse(content=image)
        response['Content-Type'] = 'image/jpeg'
        response['Cache-Control'] = 'no-cache'

        return response
