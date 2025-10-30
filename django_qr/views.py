from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            resturant_name = form.cleaned_data['resturant_name']
            url = form.cleaned_data['url']
            
            # Generate QR code
            qr = qrcode.make(url)
            file_name = resturant_name.replace(" ", "_").lower() + '_qr.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            img_url = os.path.join(settings.MEDIA_URL, file_name)
            # ✅ Return a response after saving
            return render(request, 'qr_result.html', {
                'qr_image': img_url,
                'resturant_name': resturant_name,
                'file_name': file_name,
            })
        else:
            return render(request, 'generate_qr_code.html', {'form': form})
    else:
        form = QRCodeForm()
        return render(request, 'generate_qr_code.html', {'form': form})